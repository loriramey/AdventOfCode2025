# Advent of Code Day 1 Puzzle 1
# https://adventofcode.com/2025/day/1
# Code by Lori Ramey

#--- Day 1: Secret Entrance---
import csv

zeroCounter = 0   #to track number of times the dial hits zero

rotations = []   #list of rotations provided by AOC for the puzzle
with open("/Users/loriramey/PycharmProjects/PythonProject/AoC/Assets/AoC2025_day1.csv", newline="", encoding="utf-8-sig") as f:
    reader = csv.reader(f)
    for row in reader:
        token = row[0].strip()
        rotations.append(token)

print(repr(rotations[0]))

#setup the dial puzzle = 100 positions
SIZE = 100   #numbered 0 to 99
pos = 50  #dial starts on the position #50
current = pos

history = []   #track the history of positions as the code runs (for debugging)

index = 0
while index < len(rotations):
    combination = str(rotations[index])
    letter = combination[0]
    number = int(combination[1:])

    if letter == 'R':    #clockwise motion is adding (turn "right")
        pos = (pos + number) % SIZE
    elif letter == 'L':   #counterclockwise motion is subtraction (turn "left")
        pos = (pos - number) % SIZE

    current = pos
    history.append(current)
    print(current)

    if current == 0:
        zeroCounter += 1
        print("found a zero!")

    index += 1

print("Final count: " + str(zeroCounter))
