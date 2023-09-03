import urllib.request
from bs4 import BeautifulSoup

url = input('Enter URL:')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

count = int(input('Enter count:'))
position = int(input('Enter position:'))

name_list = []
for i in range(count):
    pos_loop = 1
    tags = soup('a')
    for tag in tags:
        if pos_loop == 1 and i == 0 :
            name_list.append(tag.contents[0])
            pos_loop += 1
        elif pos_loop < position:
            pos_loop += 1
            continue
        else:
            name_list.append(tag.contents[0])
            url_i = tag.get('href', None)
            html_i = urllib.request.urlopen(url_i).read()
            soup_i = BeautifulSoup(html_i, "html.parser")
            soup = soup_i
            break
print(name_list)