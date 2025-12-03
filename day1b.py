# Advent of Code Day 1 Puzzle 2
# https://adventofcode.com/2025/day/2
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

#setup the dial puzzle = 100 positions
SIZE = 100   #numbered 0 to 99
pos = 50  #dial starts on the position #50

history = []   #track the history of positions as the code runs (for debugging)

index = 0
while index < len(rotations):
    combination = str(rotations[index])
    letter = combination[0]
    number = int(combination[1:])

    hits = number // SIZE  #catch full revoluations from large rotations
    zeroCounter += hits
    print("Added these hits: " + str(hits))

    remainder = number % SIZE

    if letter == 'R':    #clockwise motion is adding (turn "right")
        new_pos = (pos + remainder) % SIZE
        distance_forward_to_zero = SIZE - pos
        if distance_forward_to_zero > 0:
            if distance_forward_to_zero <= remainder:
                zeroCounter +=1
                print("We just slid past a zero!")

    if letter == 'L':   #counterclockwise motion is subtraction (turn "left")
        new_pos = (pos - remainder) % SIZE
        if pos == 0:
            distance_backward_to_zero = SIZE
        else:
            distance_backward_to_zero = pos
        if distance_backward_to_zero > 0:
           if distance_backward_to_zero <= remainder:
                zeroCounter +=1
                print("We just moved past a zero!")

    pos = new_pos
    history.append(pos)
    print(pos)

    '''
    if pos == 0:
        zeroCounter += 1
        print("found a zero!")
    '''

    index += 1

print("Final count: " + str(zeroCounter))
