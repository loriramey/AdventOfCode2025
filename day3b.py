# Advent of Code 2025 puzzle #3 part 2 - LOBBY
# Lori Ramey, December 3, 2025

#----- LOBBY

import csv

banks = []   #read in the raw problem data - 200 battery sequences
with open("/Users/loriramey/PycharmProjects/PythonProject/AoC/Assets/day3a.csv", newline='', encoding="utf-8-sig") as f:
    reader = csv.reader(f)
    for row in reader:
        token = row[0].strip()
        banks.append(token)

total = 0

batteries = []

for bank in banks:

    counter = 12   #count down the remaining digits that must be left over for the later batteries
    result = ""

    while counter > 0:
        max_digit = -1  # tracking the max digit in this loop
        index = 0  # tracking the index of that max digit

        limit = len(bank) - counter + 1
        for idx, char in enumerate(bank[:limit]):
            if int(char) > max_digit:
                max_digit = int(char)
                index = idx
        result = result + str(max_digit)
        bank = bank[index+1:]  #we don't need to search to the left of where this digit was found
        counter -=1

    batteries.append(result)

#sum up all the batteries
for b in batteries:
    total += int(b)

print(batteries)
print(total)
