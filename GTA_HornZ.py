import PySimpleGUI as sg
import time
import pydirectinput
import sys
from GTA_Buttons import Buttons   
from GTA_Save import Saves

key_press = Buttons() # Create Buttons

class ClsCarProp:
    def __init__(self, clsrow, carincls):
        self.clsrow = clsrow
        self.carincls = carincls

class Horn:
    def __init__(self, pageHornz, rowHornz):  # the specific horn
        self.pageHornz = pageHornz
        self.rowHornz = rowHornz

    def horn_select(self, horn_page, horn_updwn, horn_row):
        key_press.f6(); key_press.enter(); key_press.enter(); time.sleep(0.1)  # Open Menu

        if horn_page == None:
            pass
        elif horn_page >= 1:
            for _ in range(int(horn_page)):
                key_press.right()

        if horn_row == 0:
            pass
        elif horn_row != 0:
            if horn_updwn == None:  # None = 1st slot
                for _ in range(horn_row):
                    key_press.down()
            elif horn_updwn == True:  # True is down botton
                for _ in range(horn_row - 1):
                    key_press.down()
            elif horn_updwn == False:  # False is up botton
                for _ in range(horn_row):
                    key_press.up()
        key_press.enter()  # Enter horn menu
        Horn.horn_pick(self.pageHornz, self.rowHornz)  # picking the horn !!!!!!!!

    @staticmethod
    def horn_pick(page, row):
        for _ in range(int(page) - 1):
            key_press.right()
        for _ in range(int(row) - 1):
            key_press.down()
        key_press.enter()


ClassRow_and_ammount = { 
                        'Aqua': (1, 3),
                        'Bangers': (2, 12),
                        'Classic_Rally': (3, 4),
                        'Classic_Sport_A': (4, 9),
                        'Classic_Sport_B': (5, 15),
                        'Cruisers': (6, 18),
                        'Drag': (7, 5),
                        'Drift': (8, 17),
                        'Hot_Rods': (10, 9),
                        'Low_Riders': (12, 14),
                        'MEME': (13, 27),
                        'Mics': (14, 39),
                        'Modern_Muscle': (15, 6),
                        'Monster_Truck': (16, 6),
                        'Muscle': (17, 36),
                        'OFF_Road': (18, 32),
                        'Oval': (19, 4),
                        'Police': (20, 41),
                        'Prototypes': (21, 8),
                        'Racing_F1': (22, 8),
                        'Racing_GT': (23, 8),
                        'Racing_LMP': (24, 3),
                        'Racing_Touring': (25, 9),
                        'Raid': (26, 8),
                        'Rally': (27, 7),
                        'Retro_Supers': (28, 17),
                        'Rocket': (29, 6),
                        'Sedans': (30, 26),
                        'Special': (31, 44),
                        'Sport_Muscle': (32, 8),
                        'Sport_Sedan': (33, 18),
                        'Sport_A': (34, 26),
                        'Sport_B': (35, 25),
                        'Sport_Bike': (36, 2),
                        'Super_SUV': (38, 9),
                        'Super_Tuner': (39, 31),
                        'Supers': (40, 38),
                        'SUV': (41, 20),
                        'Testing': (42, 5),
                        'Time_Attack': (43, 5),
                        'Trucks': (44, 14),
                        'Tuners': (45, 32),
                        'Vans': (46, 12),
                        'Vintage':(47, 3)
                        }


ALL_CARS_Dict = {
                 'Aqua': {
                            1: (None, None, 0), 2: (None, None, 0), 3: (1, None, 0)
            },
              'Bangers': {
                            1: (None, None, 1), 2: (None, None, 0), 3: (None, None, 2), 4: (None, None, 7), 5: (None, None, 0), 6: (None, None, 1), 
                            7: (None, None, 1), 8: (None, None, 2), 9: (None, None, 0), 10: (None, None, 1), 11: (None, None, 2), 12: (None, None, 0)
            },
        'Classic_Rally': {
                            1: (1, None, 0), 2: (None, False, 1), 3: (1, None, 0), 4: (None, None, 6)
            },
      'Classic_Sport_A': {
                            1: (None, None, 4), 2: (None, None, 8), 3: (None, None, 4), 4: (None, False, 1), 5: (None, False, 2), 6: (None, None, 0), 
                            7: (1, None, 0), 8: (None, None, 5), 9 : (1, None, 1)
            },
      'Classic_Sport_B': {
                            1: (None, False, 1), 2: (None, None, 4), 3: (None, False, 5), 4: (None, None, 0), 5: (None, False, 3), 6: (None, None, 5), 
                            7: (None, None, 2), 8: (None, None, 4), 9: (None, False, 2), 10: (None, None, 1), 11: (None, False, 2), 12: (1, None, 0),
                            13: (None, None, 1), 14: (None, None, 1), 15: (None, None, 6)     
            },
             'Cruisers': {
                            1: (None, None, 6), 2: (None, False, 5), 3: (None, False, 1), 4: (None, None, 1) , 5: (None, None, 1), 6: (None, False, 1), 
                            7: (None, False, 3), 8: (None, False, 4), 9: (None, None, 0), 10: (None, False, 4), 11: (None, None, 1), 12: (None, None, 1),
                            13: (None, None, 1), 14: (None, None, 1), 15: (None, False, 6), 16: (None, False, 5), 17: (None, None, 0), 18: (None, False, 6)
            },
                 'Drag': {
                            1: (None, None, 1), 2: (None, False, 6), 3: (None, None, 3), 4: (None, None, 0), 5: (None, None, 1)
            },
                'Drift': {
                            1: (1, None, 0), 2: (None, False, 4), 3: (1, None, 2), 4: (None, False, 3), 5: (None, None, 1), 6: (None, False, 2), 
                            7: (None, None, 3), 8: (None, False, 2), 9: (None, False, 3), 10: (None, None, 2), 11: (None, None, 0), 12: (1, None, 4),
                            13: (None, None, 1), 14: (None, None, 1), 15: (None, False, 5), 16: (None, False, 3), 17: (None, None, 4) 
            },
             'Hot_Rods': {
                            1: (None, None, 2), 2: (None, False, 6), 3: (None, None, 3), 4: (None, False, 3), 5: (None, None, 1), 6: (None, None, 5), 
                            7: (1, False, 2), 8: (None, None, 2), 9: (None, False, 3)
            },
           'Low_Riders': {
                            1: (1, False, 2), 2: (None, None, 4), 3: (None, None, 3), 4: (1, None, 5), 5: (1, False, 6), 6: (1, False, 4), 
                            7: (1, False, 5), 8: (1, False, 4), 9: (1, False, 3), 10: (1, None, 2), 11: (1, False, 3), 12: (2, None, 0),
                            13: (1, False, 4), 14: (1, False, 3)
            },
                 'MEME': {
                            1: (None, None, 0), 2: (None, None, 0), 3: (None, None, 1), 4: (None, None, 1), 5: (None, None, 2), 6: (None, None, 1), 
                            7: (None, None, 5), 8: (None, None, 1), 9: (None, None, 0), 10: (None, None, 5), 11: (None, None, 1), 12: (None, None, 1),
                            13: (None, None, 1), 14: (None, None, 1), 15: (None, None, 1), 16: (None, False, 2), 17: (None, None, 1), 18: (None, None, 1),
                            19: (None, None, 1), 20: (None, None, 1), 21: (None, None, 0), 22: (None, None, 1), 23: (None, None, 3), 24: (None, None, 1), 
                            25: (None, None, 1), 26: (None, None, 1), 27: (None, None, 1)
            },
                 'Mics': {
                            1: (None, None, 2), 2: (None, False, 3), 3: (None, None, 1), 4: (None, None, 5), 5: (None, None, 1), 6: (None, None, 1), 
                            7: (None, None, 0), 8: (None, None, 1), 9: (None, None, 1), 10: (None, False, 6), 11: (None, None, 0), 12: (None, None, 0),
                            13: (None, None, 2), 14: (None, None, 2), 15: (None, None, 0), 16: (None, None, 0), 17: (None, None, 1), 18: (None, None, 0),
                            19: (None, None, 1), 20: (None, None, 0), 21: (None, None, 5), 22: (None, None, 1), 23: (None, False, 6), 24: (None, None, 0), 
                            25: (None, None, 6), 26: (None, None, 2), 27: (None, None, 0), 28: (None, None, 0), 29: (None, None, 4), 30: (None, None, 1),
                            31: (None, None, 1), 32: (None, None, 1), 33: (None, None, 0), 34: (None, None, 2), 35: (None, None, 0), 36: (None, None, 1),
                            37: (None, None, 1), 38: (None, None, 1), 39: (None, None, 5)
            },
        'Modern_Muscle': {
                            1: (None, False, 3), 2: (None, None, 1), 3: (None, False, 2), 4: (None, None, 1), 5: (None, None, 1), 6: (None, None, 3)
            },
        'Monster_Truck': {
                            1: (None, None, 1), 2: (None, None, 0), 3: (None, None, 2), 4: (None, None, 4), 5: (None, None, 2), 6: (None, None, 0)
            },
               'Muscle': {
                            1: (None, None, 4), 2: (None, False, 5), 3: (None, False, 4), 4: (None, False, 6), 5: (None, False, 3), 6: (None, False, 6), 
                            7: (None, False, 3), 8: (None, False, 6), 9: (1, None, 0), 10: (None, None, 4), 11: (None, None, 1), 12: (1, None, 0),
                            13: (2, None, 2), 14: (None, False, 2), 15: (1, None, 0), 16: (None, False, 5), 17: (None, False, 4), 18: (None, False, 4),
                            19: (None, None, 1), 20: (None, None, 1), 21: (None, None, 1), 22: (None, None, 1), 23: (None, None, 5), 24: (None, False, 6), 
                            25: (None, None, 1), 26: (None, None, 0), 27: (None, False, 3), 28: (None, None, 1), 29: (None, False, 3), 30: (None, False, 6),
                            31: (None, False, 5), 32: (None, None, 0), 33: (None, False, 2), 34: (None, False, 6), 35: (None, False, 5), 36: (None, False, 6)
            },
             'OFF_Road': {
                            1: (None, None, 5), 2: (None, False, 5), 3: (None, False, 3), 4: (None, None, 1), 5: (None, None, 1), 6: (None, None, 1), 
                            7: (None, None, 5), 8: (None, None, 1), 9: (None, None, 2), 10: (None, None, 1), 11: (None, False, 3), 12: (None, False, 2),
                            13: (None, False, 2), 14: (None, None, 1), 15: (None, None, 0), 16: (None, False, 6), 17: (None, False, 1), 18: (None, None, 1),
                            19: (None, None, 1), 20: (None, None, 1), 21: (None, None, 1), 22: (None, None, 1), 23: (None, False, 4), 24: (None, None, 1), 
                            25: (None, None, 3), 26: (None, False, 6), 27: (None, False, 6), 28: (1, None, 1), 29: (None, False, 2), 30: (None, None, 0),
                            31: (2, None, 4), 32: (2, None, 0)
            },
                 'Oval': {
                            1: (None, None, 1), 2: (None, None, 1), 3: (None, None, 1), 4: (None, None, 1)
            },
               'Police': {
                            1: (None, None, 2), 2: (None, None, 2), 3: (None, None, 2), 4: (None, None, 2), 5: (None, None, 1), 6: (None, None, 2), 
                            7: (None, None, 2), 8: (None, None, 0), 9: (None, False, 3), 10: (None, None, 1), 11: (None, None, 2), 12: (None, None, 2),
                            13: (None, None, 2), 14: (None, None, 1), 15: (None, None, 0), 16: (None, None, 1), 17: (None, None, 0), 18: (None, None, 1),
                            19: (None, None, 0), 20: (None, None, 1), 21: (None, None, 2), 22: (None, False, 3), 23: (None, None, 2), 24: (None, None, 2), 
                            25: (None, None, 1), 26: (None, None, 2), 27: (None, None, 2), 28: (None, None, 2), 29: (None, None, 1), 30: (None, None, 2),
                            31: (None, None, 2), 32: (None, None, 1), 33: (None, None, 1), 34: (None, None, 2), 35: (None, None, 2), 36: (None, None, 2),
                            37: (None, None, 1), 38: (None, None, 1), 39: (None, None, 5), 40: (None, None, 2), 41: (None, None, 2)
            },
           'Prototypes': {
                            1: (None, False, 4), 2: (None, False, 6), 3: (None, False, 4), 4: (None, False, 6), 5: (None, None, 5), 6: (None, None, 5), 
                            7: (None, False, 6), 8: (None, None, 4)
            },
            'Racing_F1': {
                            1: (None, False, 6), 2: (None, False, 6), 3: (None, False, 2), 4: (None, None, 1), 5: (None, None, 4), 6: (None, False, 5), 
                            7: (None, False, 6), 8: (None, None, 2)
            },
            'Racing_GT': {
                            1: (None, False, 5), 2: (None, None, 3), 3: (None, None, 1), 4: (None, None, 1), 5: (None, False, 1), 6: (None, None, 3), 
                            7: (None, None, 2), 8: (None, None, 1)
            },
           'Racing_LMP': {
                            1: (None, None, 3), 2: (None, None, 4), 3: (None, False, 5)
            },
       'Racing_Touring': {
                            1: (None, None, 1), 2: (None, None, 1), 3: (None, None, 1), 4: (None, False, 6), 5: (None, None, 1), 6: (None, None, 1), 
                            7: (None, None, 2), 8: (None, False, 3), 9: (None, None, 1)
            },
                 'Raid': {
                            1: (None, None, 4), 2: (None, None, 2), 3: (None, False, 1), 4: (None, None, 2), 5: (None, None, 1), 6: (None, None, 1), 
                            7: (None, None, 2), 8: (None, False, 4)
            },
                'Rally': {
                            1: (None, None, 2), 2: (None, False, 1), 3: (None, None, 2), 4: (None, None, 2), 5: (None, None, 4), 6: (None, None, 4), 
                            7: (None, None, 2)
            },
         'Retro_Supers': {
                            1: (None, False, 4), 2: (None, False, 6), 3: (None, None, 0), 4: (None, False, 2), 5: (None, False, 3), 6: (None, False, 2), 
                            7: (None, False, 6), 8: (None, False, 1), 9: (None, False, 2), 10: (None, False, 2), 11: (None, False, 4), 12: (None, None, 1),
                            13: (None, None, 1), 14: (None, False, 2), 15: (None, False, 5), 16: (None, None, 2), 17: (None, False, 2)
            },
               'Rocket': {
                            1: (None, False, 4), 2: (None, None, 0), 3: (None, None, 1), 4: (None, None, 1), 5: (None, None, 1), 6: (None, None, 1)
            },
               'Sedans': {
                            1: (None, None, 1), 2: (None, False, 5), 3: (None, None, 1), 4: (None, None, 1), 5: (None, None, 1), 6: (None, None, 1), 
                            7: (None, False, 6), 8: (None, None, 1), 9: (None, False, 6), 10: (None, None, 2), 11: (None, None, 1), 12: (None, None, 0),
                            13: (None, None, 1), 14: (None, None, 5), 15: (None, None, 1), 16: (None, None, 2), 17: (None, False, 5), 18: (None, False, 3),
                            19: (None, None, 5), 20: (None, None, 1), 21: (None, None, 1), 22: (None, None, 1), 23: (None, None, 1), 24: (None, None, 5), 
                            25: (None, False, 2), 26: (None, None, 1)
            },
              'Special': {
                            1: (None, False, 6), 2: (None, False, 6), 3: (None, False, 6), 4: (None, None, 2), 5: (None, None, 0), 6: (None, None, 5), 
                            7: (None, None, 1), 8: (None, None, 0), 9: (None, None, 5), 10: (None, None, 1), 11: (None, False, 3), 12: (None, None, 0),
                            13: (None, None, 0), 14: (None, False, 5), 15: (None, False, 6), 16: (None, False, 5), 17: (None, None, 3), 18: (None, False, 5),
                            19: (None, False, 6), 20: (None, None, 3), 21: (None, None, 5), 22: (None, None, 1), 23: (None, None, 2), 24: (None, None, 1), 
                            25: (None, False, 6), 26: (None, None, 3), 27: (None, None, 0), 28: (None, None, 0), 29: (None, False, 2), 30: (None, False, 3),
                            31: (None, None, 1), 32: (None, None, 1), 33: (None, None, 1), 34: (None, None, 1), 35: (None, False, 5), 36: (None, False, 4),
                            37: (None, False, 2), 38: (None, None, 1), 39: (None, None, 1), 40: (None, None, 1), 41: (None, None, 0), 42: (None, None, 0),
                            43: (None, False, 5), 44: (None, None, 2)
            },
         'Sport_Muscle': {
                            1: (None, None, 4), 2: (None, False, 2), 3: (None, None, 2), 4: (None, False, 2), 5: (1, None, 0), 6: (None, None, 2), 
                            7: (None, False, 1), 8: (1, False, 3)
            },
          'Sport_Sedan': {
                            1: (None, None, 0), 2: (None, None, 1), 3: (None, False, 5), 4: (None, False, 6), 5: (None, False, 5), 6: (None, False, 1), 
                            7: (None, False, 2), 8: (None, None, 2), 9: (None, None, 1), 10: (None, None, 1), 11: (None, False, 6), 12: (None, None, 1),
                            13: (None, False, 5), 14: (None, None, 3), 15: (None, None, 2), 16: (1, None, 2), 17: (None, False, 1), 18: (1, None, 2)
            },
              'Sport_A': {
                            1: (None, False, 5), 2: (None, False, 3), 3: (None, False, 5), 4: (1, None, 0), 5: (None, False, 2), 6: (None, False, 1), 
                            7: (None, False, 6), 8: (None, None, 5), 9: (1, None, 1), 10: (None, False, 4), 11: (None, False, 5), 12: (None, False, 2),
                            13: (None, False, 4), 14: (None, False, 6), 15: (None, False, 1), 16: (None, False, 5), 17: (None, None, 5), 18: (None, False, 3),
                            19: (None, False, 4), 20: (1, None, 0), 21: (None, None, 3), 22: (None, False, 4), 23: (None, False, 6), 24: (None, False, 4), 
                            25: (None, None, 5), 26: (None, None, 4)
            },
              'Sport_B': {
                            1: (1, None, 0), 2: (None, False, 2), 3: (None, False, 6), 4: (None, None, 3), 5: (None, None, 5), 6: (None, None, 5), 
                            7: (None, None, 5), 8: (None, None, 5), 9: (None, None, 2), 10: (1, False, 6), 11: (None, None, 1), 12: (None, None, 1),
                            13: (None, None, 0), 14: (1, None, 3), 15: (None, None, 5), 16: (None, False, 4), 17: (None, False, 2), 18: (None, None, 5),
                            19: (None, False, 6), 20: (None, None, 1), 21: (None, False, 4), 22: (None, False, 6), 23: (None, False, 6), 24: (None, None, 4), 
                            25: (None, False, 6)
            },
           'Sport_Bike': {
                            1: (None, None, 2), 2: (None, None, 0)
            },
            'Super_SUV': {
                            1: (None, None, 1), 2: (None, None, 0), 3: (None, None, 4), 4: (None, False, 3), 5: (None, False, 4), 6: (1, None, 0), 
                            7: (None, None, 0), 8: (None, False, 2), 9: (None, None, 0)
            },
          'Super_Tuner': {
                            1: (None, None, 4), 2: (None, None, 0), 3: (1, False, 2), 4: (1, None, 2), 5: (None, False, 6), 6: (None, None, 0), 
                            7: (None, None, 2), 8: (1, None, 0), 9: (1, False, 3), 10: (None, None, 5), 11: (None, None, 0), 12: (None, False, 2),
                            13: (1, None, 0), 14: (None, False, 3), 15: (None, False, 2), 16: (None, None, 6), 17: (None, False, 1), 18: (None, False, 2),
                            19: (1, None, 2), 20: (None, None, 1), 21: (None, False, 5), 22: (None, False, 2), 23: (1, None, 0), 24: (1, None, 4), 
                            25: (1, None, 3), 26: (1, False, 6), 27: (None, None, 1), 28: (None, None, 0), 29: (None, None, 2), 30: (None, False, 3),
                            31: (1, None, 2)
            },
               'Supers': {
                            1: (None, False, 5), 2: (None, None, 1), 3: (None, None, 2), 4: (None, False, 1), 5: (None, None, 4), 6: (None, False, 2), 
                            7: (None, None, 1), 8: (None, False, 5), 9: (None, False, 6), 10: (None, None, 3), 11: (None, False, 2), 12: (None, None, 3),
                            13: (1, False, 2), 14: (None, False, 4), 15: (1, None, 0), 16: (None, False, 1), 17: (None, None, 1), 18: (None, None, 4),
                            19: (None, None, 4), 20: (None, False, 1), 21: (None, None, 4), 22: (1, None, 3), 23: (None, False, 5), 24: (None, None, 1), 
                            25: (None, None, 2), 26: (None, False, 2), 27: (None, False, 5), 28: (None, False, 3), 29: (None, False, 3), 30: (None, False, 2),
                            31: (None, False, 5), 32: (None, None, 4), 33: (None, None, 1), 34: (None, False, 6), 35: (None, False, 4), 36: (None, False, 3),
                            37: (None, None, 5), 38: (None, False, 5)
            },
                  'SUV': {
                            1: (None, None, 5), 2: (None, None, 1), 3: (None, None, 1), 4: (None, None, 4), 5: (None, None, 6), 6: (None, False, 2), 
                            7: (None, None, 1), 8: (None, None, 1), 9: (None, None, 1), 10: (None, False, 6), 11: (None, None, 1), 12: (None, None, 1),
                            13: (None, None, 5), 14: (None, None, 1), 15: (None, False, 5), 16: (None, None, 1), 17: (None, None, 1), 18: (None, None, 1),
                            19: (None, None, 1), 20: (None, False, 5)
            },
              'Testing': {
                            1: (None, False, 3), 2: (None, False, 2), 3: (None, None, 2), 4: (None, False, 3), 5: (None, False, 3)
            },
          'Time_Attack': {
                            1: (None, None, 5), 2: (None, None, 2), 3: (None, None, 2), 4: (None, None, 2), 5: (None, None, 1)
            },
               'Trucks': {
                            1: (None, None, 1), 2: (None, None, 1), 3: (None, None, 1), 4: (None, None, 1), 5: (None, None, 5), 6: (None, False, 4), 
                            7: (None, None, 1), 8: (None, None, 1), 9: (None, None, 1), 10: (None, None, 1), 11: (None, None, 1), 12: (None, None, 1),
                            13: (None, None, 1), 14: (None, None, 1)
            },
               'Tuners': {
                            1: (None, False, 1), 2: (None, False, 2), 3: (None, False, 6), 4: (None, False, 5), 5: (1, None, 4), 6: (None, False, 3), 
                            7: (None, False, 3), 8: (None, False, 3), 9: (1, None, 2), 10: (1, None, 3), 11: (None, False, 5), 12: (None, False, 6),
                            13: (None, None, 5), 14: (None, False, 1), 15: (None, False, 2), 16: (None, False, 4), 17: (None, None, 1), 18: (1, None, 1),
                            19: (None, False, 6), 20: (None, False, 5), 21: (1, None, 0), 22: (None, False, 1), 23: (None, False, 1), 24: (None, False, 4), 
                            25: (None, None, 1), 26: (1, None, 0), 27: (None, None, 1), 28: (None, None, 1), 29: (None, False, 3), 30: (1, None, 0),
                            31: (None, False, 3), 32: (None, False, 5)
            },
                 'Vans': {
                            1: (None, None, 1), 2: (None, False, 5), 3: (None, None, 1), 4: (None, None, 1), 5: (None, None, 0), 6: (None, None, 2), 
                            7: (None, None, 1), 8: (None, None, 2), 9: (None, None, 1), 10: (None, None, 0), 11: (None, False, 5), 12: (None, False, 5)
            },
              'Vintage': {
                            1: (None, None, 1), 2: (1, None, 2), 3: (None, None, 4)
            }
                
    } 


sg.theme('DefaultNoMoreNagging')
def main():
    layout = [
        [sg.Txt('  ==== FiveM === ►', font=('Arial 18'), text_color= '#FF8C00'), sg.Txt(' PLACED IN 5TH SLOT ON TASKBAR', text_color= '#C83200', font=('Arial', 11))],
        [sg.Txt('')], # BLANK 
        [sg.Txt('******************************', text_color= '#660066'),
         sg.Txt('BEFORE the FIRST USE', font=('Arial 10') , text_color= '#660066'),
         sg.Txt('******************************', text_color= '#660066')],
        [sg.Txt('(# 1)    Get Into  ANY CAR', font=('Arial 10') , text_color= '#660066')],
        [sg.Txt('(# 2)    Open F6 Menu & Select Vehicle ', font=('Arial 10') , text_color= '#660066'),
         sg.Txt('(Second Menu)', font=('Arial 10') , text_color= '#C83200')],
        [sg.Txt('(# 3)    EXIT That Menu', font=('Arial 10') , text_color= '#660066')],
        [sg.Txt(' ' * 35), sg.Txt('Windowed Mode is Recommended', font=('Arial 10') , text_color= '#660066', justification= "center")],
        [sg.Txt('*' * 89, text_color= '#660066')],
        [sg.Txt('                ! ! !   NO MUNE\'s OPEN BEFORE RUNING   ! ! !', text_color= '#C83200', font=('Arial', 12))],
        [sg.Txt('')],  # BLANK
        [sg.Txt('I ► FIRST CLASS               II ► THEN PAGE & ROW                III ►  RUN IT', text_color= 'black', font=('times', 11))],
        [sg.Txt('')],  # BLANK
        [sg.Txt('=' * 15, text_color= '#660066'),sg.Txt('CLASS' , text_color= 'black', font=('times', 11)),
                                         sg.Combo(['Aqua', 'Bangers', 'Classic_Rally', 'Classic_Sport_A', 'Classic_Sport_B', 'Cruisers', 'Drag', 'Drift', 'Hot_Rods', 
                                                   'Low_Riders', 'MEME', 'Mics', 'Modern_Muscle', 'Monster_Truck', 'Muscle', 'OFF_Road', 'Oval', 'Police', 'Prototypes',
                                                   'Racing_F1', 'Racing_GT', 'Racing_LMP', 'Racing_Touring', 'Raid', 'Rally', 'Retro_Supers', 'Rocket', 'Sedans',
                                                   'Special', 'Sport_Muscle', 'Sport_Sedan', 'Sport_A', 'Sport_B', 'Sport_Bike', 'Super_SUV', 'Super_Tuner', 'Supers',
                                                   'SUV', 'Testing', 'Time_Attack', 'Trucks', 'Tuners', 'Vans', 'Vintage' ], 
                                                   key='-CLASS-', default_value= 'Aqua', tooltip='CLASS', readonly= True, size=(17, 1), 
                                                   background_color= None, text_color= None, font=('times', 12)), 
                                                   sg.Txt('=' * 19, text_color= '#660066')],
        
        [sg.Text(('PAGE' + ' ►'), text_color= 'black', font=('times', 11)),sg.Slider(range=(1,5), default_value=1, size=(10,13), orientation='horizontal',
                                  tooltip='PAGE', key= '-PAGE-', relief= 'solid', text_color= 'black', background_color= '#ffb84d', font=('times', 11)),sg.Txt('    '),
         sg.Text(('ROW' + ' ►'), text_color= 'black', font=('times', 11)),sg.Slider(range=(1,12), default_value=1, size=(16,13), orientation='horizontal',
                                  tooltip='ROW', key= '-ROW-', relief= 'solid', text_color= 'black', background_color= '#ffb84d', font=('times', 11) ), 
         sg.Txt('     '), sg.Button('RUN', button_color=('black', '#ffad33'), size=(4,5), font=('times', 12))],

        [sg.Txt('')], # BLANK
        [sg.ProgressBar(1, orientation='h', size=(57, 20), key='PROGBAR', bar_color=['#660066', '#ffcc80'], style= 'xpnative', relief= 'solid')],
        [sg.Txt('')], # BLANK
        [sg.Txt('=' * 62, text_color= '#660066' )],
        
            ]   

    window = sg.Window('Project HORNZ CHANGE', layout, icon= 'GasIcon.ico', finalize=True, size= (654,680))

    progress_bar = window.FindElement('PROGBAR')

    while True:  # Event loop
        event, values = window.read(timeout = 1)
        

        if event in (sg.WIN_CLOSED, 'Exit'):
            sys.exit()
            break
             

        elif event == 'RUN':

            pydirectinput.doubleClick(272, 1055); progress_bar.UpdateBar(0, 0); time.sleep(0.2)  # !!! 5TH SLOT IN TASKBAR !!! # reset PROGBAR  # Sleep

            user_horn_page = values['-PAGE-'] ; user_horn_row = values['-ROW-']
            userHornSelect = Horn(user_horn_page, user_horn_row)

            if values['-CLASS-'] in iter(ALL_CARS_Dict.keys()):  # Creates a dict from picked class
                CarsDict = ALL_CARS_Dict[values['-CLASS-']]

            if values['-CLASS-'] in iter(ClassRow_and_ammount.keys()):  # Makes ClassCarProp from picked class
                CarsPropClass = ClassRow_and_ammount[values['-CLASS-']]

            This_class = ClsCarProp(CarsPropClass[0], CarsPropClass[1])

            class_of_car = This_class.clsrow             # !!! The class you are choing, remeber - 1 from in game !!!
            cars_in_class = This_class.carincls          # !!! How many cars in a class                           !!!
            curent_dikt = CarsDict                       # !!! Create dict for the function                       !!!

            curent_car = 0 ; cars_done = 0 ; Bar = 1
            while cars_done != cars_in_class:

                key_press.f7(); key_press.enter(); key_press.enter(); time.sleep(0.0001)  # Spawn Menu Select

                window.Refresh()
                if class_of_car <= 24:
                    for _ in range(class_of_car - 1):
                        key_press.down()
                elif class_of_car > 24:
                    for _ in range(48 - class_of_car):
                        key_press.up()

                key_press.enter(); time.sleep(0.0001)  # enter selected class  # time for game to catch up
                
                window.Refresh()
                if curent_car <= (cars_in_class / 2):
                    for _ in range(curent_car):
                        key_press.down()
                elif curent_car > (cars_in_class / 2):
                    for _ in range(cars_in_class - curent_car):
                        key_press.up()
            
                time.sleep(0.2); key_press.enter(); time.sleep(0.3)

                Hornz = curent_dikt.get(curent_car + 1)
                Horn.horn_select(userHornSelect, Hornz[0], Hornz[1], Hornz[2])

                key_press.enter(); Saves.save(); time.sleep(0.1)

                for _ in range(cars_in_class):
                    progress_bar.UpdateBar(Bar, cars_in_class)


                curent_car += 1; cars_done += 1; Bar += 1
            

            sg.popup_quick_message((values['-CLASS-']) + '  DONE', text_color= '#C83200')
           

    window.close()


if __name__ == "__main__":
    main()


