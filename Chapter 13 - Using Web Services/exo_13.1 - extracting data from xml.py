import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

com_counts = []
url = input('Enter URL - ')
uh = urllib.request.urlopen(url)
data = uh.read()
tree = ET.fromstring(data)
results = tree.findall('.//count')

for count_elem in results:
    count_value = int(count_elem.text)
    com_counts.append(count_value)

total_com = sum(com_counts)
print(total_com)
