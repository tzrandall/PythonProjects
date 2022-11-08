import re
from collections import Counter

fileDirectory = "log_scrubber_test.txt"

#------------------------------------------------------------------------------
messageSeparators = 'Test: ', '\n'

# initializing variables
listBeforeFormat = []
listAfterFormat = []
top20Errors = []

# open the file and read it
file = open(fileDirectory, 'r')
readLines = file.readlines()
file.close()

# use re package to combine 'messageSeparators' to use for split()
regexPattern = '|'.join(map(re.escape, messageSeparators))

# goes through every line in the file and splits by 'messageSeparators'
for line in readLines:
    tempList = re.split(regexPattern, line)
    # adds correct part of line to listBeforeFormat
    listBeforeFormat.append(tempList[1])

# this will count how many times a message occurs and slice it
# slice turns Counter({'x': 4, 'y': 3}) into 'x': 4, 'y': 3
counterStr = str(Counter(listBeforeFormat))[9:-2]
counterStrSplit = counterStr.split(", ")

# this is used to format counterStr to have each element print on its own line
for item in counterStrSplit:
    if ', "' in item:
        listAfterFormat += str(item).split(', "')
    else:
        listAfterFormat.append(item)

# this will print each line of listAfterFormat so it is easy to read
for index in range(len(listAfterFormat)):
    if index <= 19: 
        top20Errors.append(listAfterFormat[index])
        print(listAfterFormat[index])
