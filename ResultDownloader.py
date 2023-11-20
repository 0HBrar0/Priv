import time
import pydirectinput as pi
import keyboard as kb
import pyautogui as pg

path = "C:\\Users\\HBrar04\\Desktop\\RESULTS\\UMANG\\+2_ 2023_ Results"
rn = 13689501
scn = 20458
num = rn - 13689438
time.sleep(3)
while rn < 13689561:

    time.sleep(1.5)
    pi.click(420, 320)
    pg.typewrite(str(rn), 0.008)
    pi.press('tab')
    pg.typewrite(str(scn), 0.008)
    pi.press('tab')
    pi.click(960, 20)
    time.sleep(0.75)
    if rn > 13689438:
        pi.press('down')
    time.sleep(1)
    kb.send('ctrl+c')
    pi.click(414, 379)
    time.sleep(1)
    kb.send('ctrl+v')
    pi.press('enter')
    time.sleep(1.25)
    pi.rightClick(383, 431)
    pi.click(423, 275)
    time.sleep(1.5)
    pg.typewrite(str(rn), 0.008)
    pi.press('enter')
    time.sleep(0.5)
    pi.click(124, 295)
    pi.press('tab')
    time.sleep(0.5)
    pi.press('enter')
    rn = rn + 1
    if rn == 13689487:
        rn = rn + 1
    time.sleep(0.5)




