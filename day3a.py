#Advent of Code 2025 puzzle #3 part 1 - LOBBY
# Lori Ramey, December 3, 2025

#----- LOBBY

import csv

banks = []   #read in the raw problem data - 200 battery sequences
with open("/Users/loriramey/PycharmProjects/PythonProject/AoC/Assets/day3a.csv", newline='', encoding="utf-8-sig") as f:
    reader = csv.reader(f)
    for row in reader:
        token = row[0].strip()
        banks.append(token)

#print(banks)
#print(len(banks[0]))   #each bank is 100 digits

total = 0

batteries = []

for bank in banks:

    max_digit1 = -1  # tracking the two max digits
    max_digit2 = -1
    index = None  # tracking the index of that first max digit
    result = None

    for idx, char in enumerate(bank[:-1]):
        if int(char) > max_digit1:
            max_digit1 = int(char)
            index = idx

    for b in bank[index+1:]:
        if int(b) > max_digit2:
            max_digit2 = int(b)

    result = (max_digit1 * 10) + max_digit2   #mult digit 1 by 10 for proper math
    batteries.append(result)
    total += result #add result to the running total of joules

print(batteries)
print(total)
