'''
in a team of members 20, some numbers are taken
and want to display the numbers that are not taken
so others don't pick the picked numbers
'''

# taken numbers
numTaken = [3,5,7,11,13]
print("Available numbers")
# loop
for i in range(1,21):
    if i in numTaken:
        continue
    print(i)


