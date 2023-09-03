import re
name = input("Enter file:")
handle = open(name)

total_list = []
for line in handle:
    if not re.search('[0-9]+', line) :
        continue
    numbers = re.findall('[0-9]+', line)
    for val in range(len(numbers)):
        numbers[val] = int(numbers[val])
    line_total = sum(numbers)
    total_list.append(line_total)
total = sum(total_list)
print('The total sum of all the numbers present in this document is :',total)