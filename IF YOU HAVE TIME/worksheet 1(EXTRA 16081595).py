# simple RC program
# prog to initialize Automatically
# NOT  python 2 compactiblity USE python 3

from grobot import*

bill=NewRobot("bill", colour="green")

lookdata = [] ;

print("Welcome to grobot control program")

msg= ""

promt=" type: F= forward , R= Turn Right , L= turn Left. Then press return"



while msg!= "q" and msg!= "Q" :
    lookdata = bill.look()
    msg = input(promt)
   
    if msg == "f" or msg == "F" : bill.forward() # robot moves forward
    if msg == "l" or msg == "L" : bill.left() # robot turns left  
    if msg == "r" or msg == "R" : bill.right()   # robot moves forward
    if msg == "i" or msg == "I" : bill.init()   # robot gets initialised
    
if lookdata [4]== Broken:
    print ("your robot has been crashed press i to init")
    msg = input(promt)
    if msg == "i" or msg == "I" : bill.init()   # robot gets initialised
