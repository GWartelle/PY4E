import urllib.request, urllib.parse, urllib.error
import json

com_counts = []
url = input('Enter URL - ')
uh = urllib.request.urlopen(url)
data = uh.read()

dct = json.loads(data)
com_counts = []
for comment in dct['comments']:
    com_counts.append(int(comment['count']))
total_count = sum(com_counts)
print(total_count)