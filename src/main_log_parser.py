import re
from collections import Counter


regex = r"^(\S*).*\[(.*)\]\s\"(\S*)\s(\S*)\s([^\"]*)\"\s(\S*)\s(\S*)\s\"([^\"]*)\"\s\"([^\"]*)\"\s(\S*)$"

test_str = ("46.72.177.4 - - [12/Dec/2015:18:31:08 +0100] \"POST /administrator/index.php HTTP/1.1\" 200 4494 \"http://almhuette-raith.at/administrator/\" \"Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0\" 3924\n"
            "83.167.113.100 - - [12/Dec/2015:18:31:25 +0100] \"GET /administrator/ HTTP/1.1\" 200 4263 \"-\" \"Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0\" 4743\n"
            "83.167.113.100 - - [12/Dec/2015:18:31:25 +0100] \"POST /administrator/index.php HTTP/1.1\" 200 4494 \"http://almhuette-raith.at/administrator/\" \"Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0\" 8566\n"
            "95.29.198.15 - - [12/Dec/2015:18:32:10 +0100] \"GET /administrator/ HTTP/1.1\" 200 4263 \"-\" \"Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0\" 3005\n"
            "95.29.198.15 - - [12/Dec/2015:18:32:11 +0100] \"POST /administrator/index.php HTTP/1.1\" 200 4494 \"http://almhuette-raith.at/administrator/\" \"Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0\" 9865\n"
            "109.184.11.34 - - [12/Dec/2015:18:32:56 +0100] \"GET /administrator/ HTTP/1.1\" 200 4263 \"-\" \"Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0\" 7890\n"
            "109.184.11.34 - - [12/Dec/2015:18:32:56 +0100] \"POST /administrator/index.php HTTP/1.1\" 200 4494 \"http://almhuette-raith.at/administrator/\" \"Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0\" 4743\n"
            "91.227.29.79 - - [12/Dec/2015:18:33:51 +0100] \"GET /administrator/ HTTP/1.1\" 200 4263 \"-\" \"Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0\" 2508\n"
            "91.227.29.79 - - [12/Dec/2015:18:33:52 +0100] \"POST /administrator/index.php HTTP/1.1\" 200 4494 \"http://almhuette-raith.at/administrator/\" \"Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0\" 6525\n"
            "90.154.66.233 - - [12/Dec/2015:18:36:16 +0100] \"GET /administrator/ HTTP/1.1\" 200 4263 \"-\" \"Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0\" 7178\n"
            "90.154.66.233 - - [12/Dec/2015:18:36:16 +0100] \"POST /administrator/index.php HTTP/1.1\" 200 4494 \"http://almhuette-raith.at/administrator/\" \"Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0\" 1899\n"
            "95.140.24.131 - - [12/Dec/2015:18:38:42 +0100] \"GET /administrator/ HTTP/1.1\" 200 4263 \"-\" \"Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0\" 5144\n"
            "95.140.24.131 - - [12/Dec/2015:18:38:42 +0100] \"POST /administrator/index.php HTTP/1.1\" 200 4494 \"http://almhuette-raith.at/administrator/\" \"Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0\" 4225\n")

# closures = re.finditer(regex, test_str, re.MULTILINE)

# for matchNum, match in enumerate(closures, start=1):
#         z = match.groups()[0]

    
    
    # for groupNum in range(0, len(match.groups())):
    #     groupNum = groupNum + 1
        
        # print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))
    # print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))

# def search_matches(matches, index):
#     for match in matches:
#         yield match.group(index)

# def requests_start(matches, index):
#     return sum((1 for _ in search_matches(matches, index)))

# def requests_count(matches, index):
#     return sum((1 for _ in search_matches(matches, index)))

	# print(i[3])


# print(requests_count(closures, 1))

# print(requests_start(closures, 3))


matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    # print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        group = match.group(groupNum)
        print(group)
        # print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))