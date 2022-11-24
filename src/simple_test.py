import re
from heapq import nlargest
import argparse
from collections import Counter
import json

parser = argparse.ArgumentParser(
    description='Лог парсер, на примере acces.log')

parser.add_argument('log_file', metavar='LOG_FILE', type=argparse.FileType('r'),
                    help='Укажите путь до файла с логом *.log')


parts = [
    r'(?P<ip>\S*)',
    r'(?P<remote_log_name>.*?)',
    r'(?P<userid>.*?)',
    r'\[(?P<time>.*?)\]',
    r'(?P<request>.*?)',
    r'(?P<path>.*?)',
    r'(?P<status>[0-9]+)',
    r'(?P<size>.*?)',
    r'"(?P<referrer>.*?)"',
    r'"(?P<agent>.*)"',
    r'(?P<time_micro>.*)',
]

pattern = re.compile(r'\s+'.join(parts)+r'\s*\Z')


args = parser.parse_args()
log_data = []
requests_metod_dict = {}
ips_dict = {}
top3_requests = []

for line in args.log_file:
    log_data.append(pattern.match(line).groupdict())


common_requests = len(log_data)
reques_method = Counter(x['request'] for x in log_data)
ips = Counter(x['ip'] for x in log_data)
lognest_requests = Counter(int(x['time_micro']) for x in log_data)
z = nlargest(3, lognest_requests)
group_files = (x for x in log_data if int(x['time_micro']) in z)


print(f"Всего запросов в лог файле: {common_requests}")

print("Количество запросов по HTTP-методам: ")
for x in reques_method.most_common():
    requests_metod_dict[x[0]] = x[1]
    print("\t%s Встречается %d раз" % x)

print("Top 3 IP адресов, с которых были сделаны запросы: ")
for x in ips.most_common(3):
    ips_dict[x[0]] = x[1]
    print("\t%s стучался к нам %d раз" % x)

print("Top 3 самых длительных запросов: ")
for x in sorted(group_files, reverse=False, key=lambda x: x['time_micro'])[:3]:
    top3_requests.append(x)
    print("\t%s" % x)


json_output = [{"requests count": common_requests,
                "requests by http": requests_metod_dict,
                "top 3 ips": ips_dict,
                "top 3 longest requests": top3_requests
                }]

with open("results.json", "w") as result:
    json.dump(json_output, result, indent=4)
