## worksheet 2 MAze solving Robot by left hand rule and initialize automatically

  
from grobot import*

lin = NewRobot("lin",colour="Red")

lookdata=[]

print ("ctrl+c to stop")

while True:

    lookdata  =  lin.look()
    
    if lookdata[0] == None:
        lin.left()     # to take a left turn
        lin.forward()

    elif lookdata[2]==None:
        lin.forward() # to move forward

    elif lookdata[4] == None:
         lin.right()  # to take a right turn

    else:
         
        lin.init()  # to initialize

    
