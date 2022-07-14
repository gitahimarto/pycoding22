
import random



print ('Welcome to the Magic 8 Ball')
print ('       ')
print ('Kindly input your question')
print ('       ')

A = input () 

r = random.randint(1,8)
print (r)

if (r == 1):
    print(' It is certain.')
elif (r == 2):
    print( 'It is decidedly so')
elif (r == 3):
    print('WE DELIGHTED YOU HAD A GREAT EXPERIENCE')
elif (r == 4):
    print('WE DELIGHTED YOU HAD A GREAT EXPERIENCE')
elif (r == 5):
    print('WE DELIGHTED YOU HAD A GREAT EXPERIENCE')
elif (r == 6):
    print('WE DELIGHTED YOU HAD A GREAT EXPERIENCE') 
elif (r == 7):
    print('WE DELIGHTED YOU HAD A GREAT EXPERIENCE')
else:
     r = 8
     print('incorrect input')
cls


def get_age():
    print("How old are you ")
    try:
        age = int(input())
        return age
        
    except ValueError:
        return "That was not a valid input"