import re
import sys
from heapq import nlargest
import argparse
from collections import Counter

# Using argparse for reading arguments is pretty cool.
# We get defualt help, argument types, and a lot more done :-)
# Refer = http://docs.python.org/dev/library/argparse.html
parser = argparse.ArgumentParser(description='A very simple Apache access log parser')

# A readable log file is a required argument and the file is automagically read too.
parser.add_argument('log_file', metavar='LOG_FILE', type=argparse.FileType('r'),
                   help='Path to the Apache log file')


# Regex for the common Apache log format.
parts = [
    r'(?P<ip>\S*)',                   # host %h
    r'(?P<remote_log_name>.*?)',                             # indent %l (unused)
    r'(?P<userid>.*?)',                   # user %u
    r'\[(?P<time>.*?)\]',                # time %t
    r'(?P<request>.*?)',               # request "%r"
    r'(?P<path>.*?)'
    r'(?P<status>[0-9]+)',              # status %>s
    r'(?P<size>.*?)',                   # size %b (careful, can be '-')
    r'"(?P<referrer>.*?)"',              # referrer "%{Referer}i"
    r'"(?P<agent>.*)"',                 # user agent "%{User-agent}i"
    r'(?P<time_micro>.*)',
]
pattern = re.compile(r'\s+'.join(parts)+r'\s*\Z')

# Initiazlie required variables
args = parser.parse_args()
log_data = []

# Get components from each line of the log file into a structured dict
for line in args.log_file:
  log_data.append(pattern.match(line).groupdict())

# Using a counter to get stats on the status in log entries
# Refer = http://docs.python.org/2/library/collections.html#collections.Counter
common_requests = len(log_data)
reques_method = Counter(x['request'] for x in log_data)
ips = Counter(x['ip'] for x in log_data)
lognest_requests = Counter(x['time_micro'] for x in log_data)

# Printing the STATUS count sorted by highest to lowest count
print(f"Всего запросов в лог файле: {common_requests}")
print("Количество запросов по HTTP-методам: ")
for x in reques_method.most_common():
  print("\t%s Встречается %d раз" % x)
print("Top 3 IP адресов, с которых были сделаны запросы: ")
for x in ips.most_common(3):
  print("\t%s стучался к нам %d раз" % x)

for x in nlargest(3, lognest_requests):
  print("\t%s время выполнения" % x)
  print(x)