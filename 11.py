import re
filepath = "regex_sum_1270935.txt"
file = open(filepath)
numlist = []
sum = 0
for line in file:
  numlist += re.findall('[0-9]+', line)
for num in numlist:
  sum += int(num)
print(sum)
