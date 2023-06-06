"""
name1 = "aulad hossain "
name2 = 'ritu chowdory'
name3 =
aulad hossain 
ar boin ritu 

print (name1,name2)
for cher in name1:
    print(cher)

print(name2[3])
print(name2[1:6])
print(name1[::-1])
"""
"""
def multiple():
    return 3,4
print (multiple())
things = 'pen','watwer','sun_glass','charger','phone','web'
print(things)
print (type(things))
print(things[0])
print(things[3:6])
for item in things:
    print (item)
print(len(things))
"""

"""
import pyautogui
from time import sleep
sleep(5)
for i in range(0,3):
    pyautogui.write("i love you python!",interval=0.20)
    pyautogui.press("enter")
""" 
import cv2
cam = cv2.videoCapture(4)
while True:
    _,frame= cam.read()
    cv2.imshow("my cam",frame)
    cv2.waitkey(1)

 