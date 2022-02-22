# Warning: Execute this code at your own risk. It automates activity in paladins and likely violates it's TOS.
# Key functionalities include determining screen resolution, the centermost pixel of a gui element(s) given an and
# degree of confidence, finding a pixel given coordinates, clicking a pixel, clicking and dragging, click drag release
# and screenshot.
import pyautogui
import time
# The script will print the resolution of the host device screen, and print the locations of several buttons
# then click the minimize button on the command prompt screen that opens when running this scripts


def reproportion(o_d, n_d, pixel):
    return round((n_d / o_d) * pixel)
# Remember that pyautogui discriminates images based on resolution. So scripts using images taken on other devices
# may fail even if very similar images are provided.

# Initial state: All apps but pycharm are minimized. Paladins Feb 2022 ver. app is installed and shortcut is on desktop.
# Also the monitor must be x=1920 by y=1080.
# If on another on monitor then for every dimension use rounded(your_dim/my_dim * dim)


if __name__ == '__main__':
    old_x = 1920
    old_y = 1080
    path = r'C:\Users\Kendrick\PycharmProjects\autogui\Images'
    print("Hello")
    pyautogui.PAUSE = 2.5
    pyautogui.FAILSAFE = True
    print("Current screen resolution", pyautogui.size())
    new_x = pyautogui.size()[0]
    new_y = pyautogui.size()[1]
    print("Current mouse position", pyautogui.position())
    print("Button found at", pyautogui.locateOnScreen(path + r'\pycharm_logo.PNG'))
    coord = pyautogui.locateOnScreen(path + r'\pycharm_logo.PNG')
    # Standard coordinates are composed of left, top, width, height pixel counts. Each accessible by coord[x] -1<x<4
    pyautogui.click(1778, 23, clicks=1, interval=1, button='left')
    print("pycharm Screen minimized")
    coord = pyautogui.locateOnScreen(path + r'\paladins_logo.PNG')
    pyautogui.click(x=reproportion(old_x, new_x, coord[0]), y=reproportion(old_y, new_y, coord[1]), clicks=2, interval=.25, button='left')
    print("paladins launched")
    time.sleep(180)
    coord = pyautogui.locateOnScreen(path + r'\reward_button.PNG')
    print("Found rewards", coord)
    pyautogui.click(x=reproportion(old_x, new_x, 200), y=reproportion(old_y, new_y, 585), clicks=1, interval=1, button='left')
    print("Clicked rewards")
    # coord = pyautogui.locateOnScreen(path + r'\watch_button')
    for num in range(0, 5):  # Paladins allows you to collect a reward for watching an advertisement at least 10 times.
        pyautogui.click(x=reproportion(old_x, new_x, 960), y=reproportion(old_y, new_y, 725), clicks=1, interval=1, button='left')
        time.sleep(45)
    pyautogui.click(x=reproportion(old_x, new_x, 1490), y=reproportion(old_y, new_y, 275), clicks=1, interval=1, button='left')  # Exiting reward screen
    pyautogui.click(x=reproportion(old_x, new_x, 1900), y=reproportion(old_y, new_y, 45), clicks=1, interval=1, button='left')  # Clicking the x button
    pyautogui.click(x=reproportion(old_x, new_x, 975), y=reproportion(old_y, new_y, 720), clicks=1, interval=1, button='left')  # Clicking "exit game"
    pyautogui.click(x=reproportion(old_x, new_x, 960), y=reproportion(old_y, new_y, 560), clicks=1, interval=1, button='left')  # Clicking the second "exit game" button to exit
    print("Script end")  # Hopefully now have 500 more gold now
    # Simply remembering the location of a button is sometimes better than searching for it since after an initial press
    # it's liable to change state and it's visual representation too. Making it unable to be found with the same image.
    # For some reason the gui not in the desktop can't be detected by pyautogui. So hard coding was used, unfortunately.

