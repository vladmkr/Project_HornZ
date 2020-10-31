import pyautogui
import time
import pydirectinput


# pydirectinput.doubleClick(707,1055) 
# time.sleep(0.2)
class Saves():
    @staticmethod
    def save():
        pydirectinput.press('f7')                                           
        time.sleep(0.00001)
        pydirectinput.press('enter')
        time.sleep(0.00001)
        pydirectinput.press('down')
        time.sleep(0.00001)
        pydirectinput.press('enter')
        time.sleep(0.00001)


if __name__ == '__main__':
    Saves()


