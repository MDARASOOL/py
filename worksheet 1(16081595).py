# simple RC program

# NOT  python 2 compactiblity USE python 3

from grobot import*

bill=NewRobot("bill", colour="green")

print("Welcome to grobot control program")

msg= ""

promt=" type: F= forward , R= Turn Right , L= turn Left. Then press return"


while msg!= "q" and msg!= "Q" :

    msg = input(promt)

    if msg == "f" or msg == "F" : bill.forward() # robot moves forward
    if msg == "l" or msg == "L" : bill.left() # robot turns left  
    if msg == "r" or msg == "R" : bill.right()   # robot moves forward

exit()
        
    
