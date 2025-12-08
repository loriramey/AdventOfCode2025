#Advent of Code 2025 puzzle #4 part 1 - PRINTING DEPT
# Lori Ramey, December 8, 2025

#----- PRINTING DEPARTMENT-----
from Assets.asset_d4 import paper_rolls

data = paper_rolls
rows = len(data)
cols = len(data[0])

paper = '@'   #these symbols are used in the raw data
emtpy = '.'

#this function counts the number of paper rolls in all 8 surrounding positions
def count_neighbors(data,r,c,symbol=paper):
    count = 0

    for nr in range(max(0, r-1), min(rows, r+2)):
        for nc in range(max(0, c-1), min(cols, c+2)):
            if nr == r and nc == c:
                continue
            if data[nr][nc] == symbol:
                count += 1
    return count  #number of paper rolls that match the criteria

accessible_rolls = 0

for r in range(rows):
    for c in range(cols):
        if data[r][c] == paper and count_neighbors(data,r,c) < 4:
            accessible_rolls += 1

print(accessible_rolls)
