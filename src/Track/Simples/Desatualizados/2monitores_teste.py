from screeninfo import screeninfo
import pyautogui as pa

pa.FAILSAFE = False

pa.moveTo(75,300)
pa.moveTo(-100, -300, duration=2)