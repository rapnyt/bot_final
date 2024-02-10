import PIL.ImageGrab
import PIL.Image
import random
import win32con
import win32api
import time
import datetime
import pyttsx3
import colorsys
from playsound import playsound

# Initialize text-to-speech engine
engine = pyttsx3.init()
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def alarm_bot(x):
    last_player_icon = (2190, 372, 2200, 382)
    v = 0
    start_time = time.time()
    counter = 0

    while time.time() - start_time < x:
        icon = PIL.ImageGrab.grab(last_player_icon, include_layered_windows=False, all_screens=True)
        icon.save('icon.jpg')
        icon = PIL.Image.open('icon.jpg').convert('RGB')
        icon = list(icon.getdata())

        for i in icon:
            h = (colorsys.rgb_to_hsv(i[0], i[1], i[2]))[0]
            if h > 0.9:
                enemy_notification()
                icon.show()
                return True
            v += (colorsys.rgb_to_hsv(i[0], i[1], i[2]))[2]
        if v / len(icon) < 80:
            counter += 1
        if counter > 40:
            enemy_notification()
            icon.show()
            return True
        v = 0
        print("Everything's alright ", datetime.datetime.now())
        if time.time() - start_time > 840:
            engine.say("Mining cycle completed")
            engine.runAndWait()

def enemy_notification():
    engine.say("Attention. Neutral or hostile player in the system")
    engine.runAndWait()
    playsound("Red Alert.mp3")
    print("Hostile ", datetime.datetime.now())

def mouse_click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(random.uniform(0.05, 0.09))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def mouse_scroll(x):
    win32api.SetCursorPos((random.randint(x[0], x[2]), random.randint(x[1], x[3])))
    time.sleep(random.uniform(1, 2))
    for i in range(1, 5):
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, random.randint(x[0], x[2]), random.randint(x[1], x[3]), random.randint(-600, -500), 0)
        time.sleep(random.uniform(0.4, 0.5))
    time.sleep(random.uniform(1, 2))

def mouse_sequence(x):
    mouse_click(random.randint(x[0], x[2]), random.randint(x[1], x[3]))
    time.sleep(random.uniform(0.8, 2.2))
    mouse_click(random.randint(x[0] + 940, x[2] + 940), random.randint(x[1], x[3]))
    time.sleep(random.uniform(0.8, 2.2))
    mouse_click(random.randint(x[0], x[2]), random.randint(x[1] + 528, x[3] + 528))
    time.sleep(random.uniform(0.8, 2.2))
    mouse_click(random.randint(x[0] + 940, x[2] + 940), random.randint(x[1] + 528, x[3] + 528))
    time.sleep(random.uniform(0.8, 2.2))

def delay(x, y):
    time.sleep(random.uniform(x, y))

# Define coordinates for various actions
undock_icon = (2698, 193, 2780, 212)
overview_open_icon = (2775, 309, 2791, 322)
overview_type_icon = (2664, 43, 2741, 58)
overview_mining_type_icon = (2663, 409, 2783, 425)
mining_belt_icon = (2651, 78, 2777, 99)
warp_belt = (2479, 133, 2608, 169)
zoom_out = (2356, 455, 2376, 471)
second_ore_rock = (2646, 138, 2728, 150)
approach_ore_rock = (2471, 191, 2556, 211)
first_strip_miner_module = (2713, 485, 2739, 511)
second_strip_miner_module = (2768, 486, 2790, 508)
overview_station_type_icon = (2662, 213, 2777, 235)
ten_forward_station_icon = (2665, 80, 2771, 99)
dock_icon = (2489, 86, 2596, 111)
cargohold = (1937, 105, 1973, 118)
ore_hold = (1937, 411, 2066, 429)
select_all = (2583, 474, 2623, 509)
move_to = (1969, 119, 2071, 152)
item_hangar = (2158, 133, 2338, 154)
exit_inventory = (2780, 52, 2790, 64)
player_list_field = (2080, 240, 2150, 360)

# Main loop
while True:
    delay(2, 3)
    mouse_scroll(player_list_field)
    delay(0.6, 1.2)
    if alarm_bot(10):
        break
    mouse_sequence(undock_icon)
    delay(35, 50)
    mouse_scroll(player_list_field)
    delay(0.6, 1.2)
    if alarm_bot(5):
        mouse_sequence(overview_open_icon)
        delay(0.6, 1.2)
        mouse_sequence(ten_forward_station_icon)
        delay(0.6, 1.2)
        mouse_sequence(dock_icon)
        break
    mouse_sequence(overview_open_icon)
    delay(0.6, 1.2)
    mouse_sequence(overview_type_icon)
    delay(0.6, 1.2)
    mouse_sequence(overview_mining_type_icon)
    delay(0.6, 1.2)
    mouse_sequence(mining_belt_icon)
    delay(0.6, 1.2)
    mouse_scroll(player_list_field)
    delay(0.6, 1.2)
    if alarm_bot(5):
        mouse_sequence(overview_type_icon)
        delay(0.6, 1.2)
        mouse_sequence(overview_station_type_icon)
        delay(1, 3)
        mouse_sequence(ten_forward_station_icon)
        delay(0.6, 1.2)
        mouse_sequence(dock_icon)
        break
    mouse_sequence(warp_belt)
    delay(0.6, 1.2)
    mouse_sequence(zoom_out)
    delay(50, 65)
    if alarm_bot(5):
        delay(1, 3)
        mouse_sequence(overview_type_icon)
        delay(0.6, 1.2)
        mouse_sequence(overview_station_type_icon)
        delay(0.6, 1.2)
        mouse_sequence(ten_forward_station_icon)
        delay(0.6, 1.2)
        mouse_sequence(dock_icon)
        break
    mouse_sequence(second_ore_rock)
    delay(0.6, 1.2)
    mouse_sequence(approach_ore_rock)
    delay(0.6, 1.2)
    mouse_mining_sequence(first_strip_miner_module, second_strip_miner_module)
    delay(0.6, 1.2)
    mouse_sequence(overview_type_icon)
    delay(0.6, 1.2)
    mouse_sequence(overview_station_type_icon)
    delay(0.6, 1.2)
    mouse_sequence(ten_forward_station_icon)
    if alarm_bot(860):
        delay(1, 5)
        mouse_sequence(dock_icon)
        break
    delay(10, 20)
    mouse_sequence(dock_icon)
    delay(90, 120)
    mouse_sequence(cargohold)
    delay(10, 20)
    mouse_sequence(ore_hold)
    delay(3, 5)
    mouse_sequence(select_all)
    delay(2, 7)
    mouse_sequence(move_to)
    delay(2, 8)
    mouse_sequence(item_hangar)
    delay(10, 20)
    mouse_sequence(exit_inventory)
    delay(6, 14)

    now = datetime.datetime.now()
    endgame = now.replace(hour=22, minute=0, second=0, microsecond=0)
    if now > endgame:
        break
