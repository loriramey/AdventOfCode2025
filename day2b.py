#Advent of Code 2025 puzzle #2 part 2 - GIFT SHOP
# Lori Ramey, December 2, 2025

#----- GIFT SHOP

input = "516015-668918,222165343-222281089,711089-830332,513438518-513569318,4-14,4375067701-4375204460,1490-3407,19488-40334,29275041-29310580,4082818-4162127,12919832-13067769,296-660,6595561-6725149,47-126,5426-11501,136030-293489,170-291,100883-121518,333790-431800,897713-983844,22-41,42727-76056,439729-495565,43918886-44100815,725-1388,9898963615-9899009366,91866251-91958073,36242515-36310763"
#print(len(input))   #there are 28 ranges in my list
inputs = input.split(",")

#setup function for the pattern recognition engine - periodic strings
total = 0

def is_periodic_string(sequence):
    L = len(sequence)
    half = len(sequence) // 2
    len_sub = 1  #the length of a substring, default value = 1

    for len_sub in range(1, half+1):  #check only half the string, as a pattern cannot be larger than half
        if len(sequence) % len_sub != 0:
            continue   #the pattern can't repeat within the available space

        w = str(sequence[0:len_sub])
        k = len(sequence) // len_sub #number of possible repeats in this string
        test_case = w * k
        if test_case == sequence:
            return True
    return False

#roll through the inputs and unpack into a list of lists
segments = []
for i in inputs:
    #wrangle the raw data into integers I can work with
    segments.append(i.split("-"))

for pair in segments:  #grab a list written in the form ['a', 'b']
    start = int(pair[0])
    end = int(pair[1])

    #create every possible number in between start and end
    #meanwhile, check for the square string shape using the function above
    #if true, add value to sum variable
    current = start
    while current <= end:
        if is_periodic_string(str(current)):
            total += current
        current += 1


print(total)