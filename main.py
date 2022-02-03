import time
import pyautogui


time.sleep(3)
working_time = 3   #int(input('Number of times you want to buy the item >>> '))

desired_item_button = [int(input('X coordinates of desired item')), int(input('Y coordinates of desired item'))]
confirm_button = [852, 558]
okay_button = [956, 558]

buttons = [desired_item_button[0], desired_item_button[1], confirm_button[0], confirm_button[1], okay_button[0], okay_button[1]]



def move_and_click(buttons_positions):
    global working_time

    a = 0
    b = 1

    for i in range(3):
        time.sleep(0.5)
        #print('Mouse Moved')         # Debugging
        pyautogui.moveTo(x = buttons_positions[a], y = buttons_positions[b])
        time.sleep(0.5)
        #print('Mouse Clicked\n')         # Debugging
        pyautogui.click()
        a += 2
        b += 2
        
    working_time -= 1



while working_time != 0:
    move_and_click(buttons)