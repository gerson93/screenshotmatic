import pyautogui
from datetime import datetime, time, timedelta

time_next_screenshot = time(21, 36, 0)
now = datetime.now()
now = time(now.hour, now.minute, 0)
number_of_cap = 0

def get_now_time ():
    now = datetime.now()
    return time(now.hour, now.minute, 0)

def add_delta (now, step):
    generated_date = datetime(1, 1, 1, now.hour, now.minute, 0)
    step = timedelta(minutes = step)
    result = generated_date + step
    return time(result.hour, result.minute, 0)

while (True):
    now = get_now_time()
    if (now == time_next_screenshot):
        print('sacar captura')
        screenshot = pyautogui.screenshot()
        screenshot.save("D:\ cap" + str(number_of_cap) + ".png")
        time_next_screenshot = add_delta (now, 5)
        number_of_cap += 1
        print(time_next_screenshot)
    if (now > time(21, 38, 0)):
        break
