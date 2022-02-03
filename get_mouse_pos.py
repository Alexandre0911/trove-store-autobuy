import os
import time
import pyautogui

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "positions.txt")    # Path to positions text file



def clear_textfile():
    with open(path, "r") as file:
        file.write('')

def write_positions():
    with open(path, "r") as file:
        line_count = 0
        lines = file.readlines()

        for x in lines:
            line_count += 1
        file.close()

        with open(path, "a") as file:
            file.write('Position Number {} >>> {}\n'.format(line_count + 1, mouse_pos))
            file.close()



print('Clear File --> 0\nRecord Mouse Position --> 1')
opt = int(input('Your choice >>> '))



if opt == 0:
    clear_textfile()

else:
    print('You now have 5 seconds to position your mouse to the position you want to know the coordinates')
    time.sleep(5)           # You have 5 seconds to position your mouse whereever you want on the screen
    mouse_pos = pyautogui.position()
    write_positions()