import pyautogui

def piramid(n):
    for i in range(1,n+1):  
        pyautogui.write("#"*i, interval=0.001)  
        pyautogui.press('enter')

n = int(input())
piramid(n)

