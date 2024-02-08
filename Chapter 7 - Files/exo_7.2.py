# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
lcount = 0
conftot = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    confind = line.find('0.')
    consco = line[confind:]
    lcount = lcount + 1
    conftot = conftot + float(consco)
confavg = conftot/lcount
print("Average spam confidence:", confavg)