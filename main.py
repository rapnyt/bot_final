# grid layout 2, default, width 940 height 528, remember
import PIL.ImageGrab
import pytesseract
import random
import win32con
import win32api
import time

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def alarm_bot():

    import PIL.ImageGrab
    import pyttsx3
    import pytesseract
    import time
    import datetime
    import PIL.Image
    import PIL.ImageChops
    import colorsys
    from playsound import playsound

    start_time = time.time()
    engine = pyttsx3.init()
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    player_quantity = (1950, 435, 1980, 460)
    img = PIL.ImageGrab.grab(player_quantity, include_layered_windows=False, all_screens=True)
    last_player_icon = (2177, 345, 2187, 355)
    wait_interval = 5
    h = 0
    s = 0
    v = 0

    while True:
        icon = PIL.ImageGrab.grab(last_player_icon, include_layered_windows=False, all_screens=True)
        icon.save('icon.jpg')
        icon = PIL.Image.open('icon.jpg').convert('RGB')
        # icon.show()
        icon = list(icon.getdata())

        for i in icon:
            h += (colorsys.rgb_to_hsv(i[0], i[1], i[2]))[0]
            s += (colorsys.rgb_to_hsv(i[0], i[1], i[2]))[1]
            v += (colorsys.rgb_to_hsv(i[0], i[1], i[2]))[2]
        h /= 100
        s /= 100
        v /= 100
        print(h, s, v)

        if 0.36 > h > 0.55 or v < 80:
            engine.say("Attention. Neutral or hostile player in the system")
            engine.runAndWait()
            playsound("Red Alert.mp3")
            print("Hostile ", datetime.datetime.now())
        else:
            print("Everything's alright ", datetime.datetime.now())
        h = 0
        s = 0
        v = 0
        time.sleep(wait_interval)
        print(time.time() - start_time)
        if time.time() - start_time > 840:
            engine.say("Mining cycle completed")
            engine.runAndWait()


def mouse_click(x,y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(random.uniform(0.05, 0.09))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def delay(x):
    time.sleep(random.uniform(0.5))


undock_icon = (2698, 193, 2780, 212)
overview_open_icon = (2775, 309, 2791, 322)
overview_type_icon = (2631, 43, 2698, 58)
overview_mining_type_icon = (2643, 406, 2728, 422)
mining_belt_icon = (2651, 78, 2725, 102)
warp_belt = (2457, 135, 2558, 163)
zoom_out = (2356, 455, 2376, 471)
second_ore_rock = (2646, 138, 2728, 150)
approach_ore_rock = (2471, 191, 2556, 211)
first_strip_miner_module = (2713, 485, 2739, 511)
second_strip_miner_module = (2768, 486, 2790, 508)
overview_station_type_icon = (2622, 209, 2736, 230)
ten_forward_station_icon = (2644, 81, 2715, 102)
dock_icon = (2467, 86, 2553, 108)
cargohold = (1937, 105, 1973, 118)
ore_hold = (1937, 411, 2066, 429)
select_all = (2583, 474, 2623, 509)
move_to = (1969, 119, 2071, 152)
item_hangar = (2239, 133, 2402, 166)
exit_inventory = (2780, 52, 2790, 64)

start_time = time.time()
# while time.time() - start_time < 100:
#     mouse_click(random.randint(undock_icon[0], undock_icon[2]), random.randint(undock_icon[1], undock_icon[3]))
#     time.sleep(0.5)
#     print(time.time() - start_time)

print(random.uniform(0.05, 0.09))

while True:
    mouse_click(random.randint(undock_icon[0], undock_icon[2]), random.randint(undock_icon[1], undock_icon[3]))

