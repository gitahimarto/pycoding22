
print ('Hello')
print ('whats your total bill')

TB = int(input())

#tip = 0.15 * TB #TCB = TB + tip #print (TCB)

print ('How was your service expirience') 
print ('For GOOD press 1') 
print ('For GREAT press 2') 
print ('For TERRIBLE press 3') 

service = int(input())

if (service == 1):
    tip = 0.15 * TB 
    print('WE DELIGHTED YOU ENJOYED THE SEFVICE')
    print('WE HOPE U WILL DINE WITH US AGAIN')
elif (service == 2):
    tip = 0.2 * TB
    print('WE DELIGHTED YOU HAD A GREAT EXPERIENCE')
    print('WE HOPE U WILL DINE WITH US AGAIN')
elif(service == 3):
    tip = 0
    print('WE ARE SORRY TO HEAR YOU HAD A TERRIBLE EXPERIENCE')
else:
     tip = 0
     print('incorrect input')
 
TCB = TB + tip 

print ('Your Total Cost BIll is:' , TCB)




