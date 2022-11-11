# In this assignment you will read through and parse a file with text
# and numbers. You will extract all the numbers in the file and compute'
# the sum of the numbers.
import re

fileName = input('Enter file name: ')
while True:
    try:
        fileHandle = open(fileName)
        break
    except:
        print('File not found.')
        fileName = input('Enter file name: ')

total = 0
for line in fileHandle:
    nums = re.findall('[0-9]+', line)
    nums = [int(num) for num in nums]
    total += sum(nums)

print(total)