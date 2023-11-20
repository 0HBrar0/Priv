import time
import pydirectinput as pd
import mouse
from ahk import AHK
import os
time.sleep(5)
ahk = AHK()

pd.press('e')
time.sleep(2.1)
mouse.move(209,235);time.sleep(1);ahk.click(209,235)
time.sleep(4.5)
pd.press('enter')
time.sleep(2.6)
mouse.move(1331, 415);time.sleep(1);ahk.click(1331, 415); time.sleep(2)
mouse.move(1257, 413);time.sleep(1);ahk.click(1257, 413); time.sleep(2.6)
pd.press('w')
pd.press('w')
pd.press('w')
pd.press('w')
pd.press('w')
pd.press('d')
pd.press('d')
mouse.move(1079, 679);time.sleep(1);ahk.click(1079, 679); time.sleep(2)
mouse.move(997, 685);time.sleep(1);ahk.click(997, 685); time.sleep(2.6)
