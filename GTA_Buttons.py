import pyautogui
import time
import pydirectinput

class Buttons:
    def down(self):
        pydirectinput.press('down')
        # return time.sleep(0.00001)
    
    def up(self):
        pydirectinput.press('up') 
        # return time.sleep(0.00001)

    def right(self):
        pydirectinput.press('right')
        return time.sleep(0.00001)
    
    def left(self):
        pydirectinput.press('left') 
        return time.sleep(0.00001)

    def enter(self):
        pydirectinput.press('enter') 
        return time.sleep(0.00001)
    
    def backspace(self):
        pydirectinput.press('backspace')
        return time.sleep(0.00001)

    def f5(self):
        pydirectinput.press('f5')
        return time.sleep(0.00001)
    
    def f6(self):
        pydirectinput.press('f6')
        return time.sleep(0.00001)
    
    def f7(self):
        pydirectinput.press('f7')
        return time.sleep(0.00001)
                
if __name__ == '__main__':
    Buttons()