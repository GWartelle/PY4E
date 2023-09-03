name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = {}
for line in handle:
    if not line.startswith('From '):
        continue
    words = line.split()
    time1 = words[5]
    time2 = time1.split(':')
    hour = time2[0]
    counts[hour] = counts.get(hour, 0) + 1

lst = []
for k,v in counts.items():
    lst.append((k,v))

lst = sorted(lst)
for k,v in lst:
    print(k,v)