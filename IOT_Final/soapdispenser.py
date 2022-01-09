import cv2
from collections import Counter
from module import findnameoflandmark,findpostion,speak
import math
import asyncio
import os
import sys
from gpiozero import Servo
import time
from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory()

#servo1 = Servo(12, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)
#servo2 = Servo(18, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)
servo = Servo(17, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)


#Use CV2 Functionality to create a Video stream and add some values + variables
cap = cv2.VideoCapture(0)
tip=[8,12,16,20]
tipname=[8,12,16,20]
fingers=[]
finger=[]
up=0


async def runServo(servo):
    print('async start')
    servo.mid()
    print("middle")
    await asyncio.sleep(0.5)
    servo.mid()
    print("middle")
    await asyncio.sleep(0.8)
    servo.min()
    print("min")
    await asyncio.sleep(1)
    servo.mid()
    print("middle")
    await asyncio.sleep(1)
    print('async over')
    
mycount1 = 0

#Create an infinite loop which will produce the live feed to our desktop and that will search for hands
while True:
     ret, frame = cap.read() 
     #Unedit the below line if your live feed is produced upsidedown
     flipped = cv2.flip(frame, flipCode = 0)
     
     #Determines the frame size, 640 x 480 offers a nice balance between speed and accurate identification
     frame1 = cv2.resize(flipped, (640, 480))
    
    #Below is used to determine location of the joints of the fingers 
     a=findpostion(frame1)
     b=findnameoflandmark(frame1)
     
     #Below is a series of If statement that will determine if a finger is up or down and
     #then will print the details to the console
     if len(b and a)!=0:
        finger=[]
        if a[0][1:] < a[4][1:]: 
           finger.append(1)
           print ("hi", b[4])
          
        else:
           finger.append(0)   
        
        fingers=[] 
        for id in range(0,4):
            if a[tip[id]][2:] < a[tip[id]-2][2:]:
               print("!!!", b[tipname[id]])

               fingers.append(1)
    
            else:
               fingers.append(0)
     #Below will print to the terminal the number of fingers that are up or down          
     x=fingers + finger
     c=Counter(x)
     up=c[1]
     down=c[0]
     print('This many fingers are up - ', up)
     print('This many fingers are down - ', down)
     
     #Below shows the current frame to the desktop 
     cv2.imshow("Frame", frame1);
     cv2.waitKey(25)
     key = cv2.waitKey(1) & 0xFF
     
     if up == 5:
        if mycount1 == 3:
            asyncio.run(runServo(servo))
            count = 0
            while count<20:
                ret, frame = cap.read()
                frame1 = cv2.resize(frame, (640, 480))
                cv2.imshow("Frame", frame1);
                count+=1
            break
               
        mycount1+=1    
     
     #Below will speak out load when |s| is pressed on the keyboard about what fingers are up or down
     #if key == ord("q"):
      #  speak("you have"+str(up)+"fingers up  and"+str(down)+"fingers down") 
     
     #Below states that if the |s| is press on the keyboard it will stop the system
     if key == ord("s"):
       break

cap.release()
cv2.destroyAllWindows()
os.system("python3 soapdispenser.py")   


