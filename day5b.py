#Advent of Code 2025 puzzle #5 part 2 - CAFETERIA
# Lori Ramey, December 8, 2025

#----- CAFETERIA -----
from Assets.asset_d5 import fresh_ranges as f, ingredients

fresh_ranges= []
for n in f:    #unpack into series of lists (pairs) of start/end ranges
    start_str, end_str = n.split('-')
    fresh_ranges.append((int(start_str), int(end_str)))

fresh_ranges.sort(key=lambda x: x[0])  #now all our ranges are sorted by start

#merging all ranges to determine unique sets of fresh id's
merged = []  #setting up room for our united sets
for start, end in fresh_ranges:
    if not merged:   #base case
        merged.append([start, end])
        continue

    last_start, last_end = merged[-1]

    if start <= last_end +1:   #expand an existing range if there is overlap
        if end > last_end:
            merged[-1][1] = end
    else:                       #or append this new range
        merged.append([start, end])

total_fresh = 0 #final answer - how many potential fresh ingredients there are
for start, end in merged:
    total_fresh += end - start+1

print(total_fresh)