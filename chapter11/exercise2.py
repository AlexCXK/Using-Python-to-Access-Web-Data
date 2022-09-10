# Exercise 2: Write a program to look for lines of the form:
# New Revision: 39772
# Extract the number from each of the lines using a regular expression
# and the findall() method. Compute the average of the numbers and
# print out the average as an integer.
# Enter file:mbox.txt
# 38549
# Enter file:mbox-short.txt
# 39756

import re
fileName = input("Enter file: ")
fHand = open(fileName)
rule = '^New Revision: ([0-9]+)'
count = 0
total = 0
for line in fHand:
    vList = re.findall(rule, line)
    if vList:
        count = count + 1
        total = total + int(vList[0])

print(int(total/count))


