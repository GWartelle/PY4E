name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = {}
for line in handle:
    if not line.startswith('From ') :
        continue
    words = line.split()
    mail = words[1]
    counts[mail] = counts.get(mail, 0) + 1

bigmail = None
bigcount = None
for mail,count in counts.items() :
    if bigcount is None or count > bigcount :
        bigmail = mail
        bigcount = count

print(bigmail, bigcount)