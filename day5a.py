#Advent of Code 2025 puzzle #5 part 1 - CAFETERIA
# Lori Ramey, December 8, 2025

#----- CAFETERIA -----
from Assets.asset_d5 import fresh_ranges, ingredients
print(fresh_ranges)

fresh = []
for i in fresh_ranges:    #unpack into series of lists (pairs) of start/end ranges
    fresh.append(i.split("-"))

ingredient_IDs = []
for i in ingredients:
    ingredient_IDs.append(int(i))   #turn tngredient IOs into individual ints

total_fresh = 0 #final answer

for id in ingredient_IDs:
    for pair in fresh:
        start = int(pair[0])
        end = int(pair[1])
        if start <= id <= end:
            total_fresh += 1
            break

print(total_fresh)