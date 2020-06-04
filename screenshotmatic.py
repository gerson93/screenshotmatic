import pyautogui
from datetime import datetime, time, timedelta

def get_now_time ():
    now = datetime.now()
    return time(now.hour, now.minute, 0)

def add_delta (now, step):
    generated_date = datetime(1, 1, 1, now.hour, now.minute, 0)
    step = timedelta(minutes = step)
    result = generated_date + step
    return time(result.hour, result.minute, 0)

def screenshotmatic (endtime, step):
    time_next_screenshot = add_delta(get_now_time(), 1)
    number_of_cap = 0
    while (True):
        now = get_now_time()
        if (now == time_next_screenshot):
            print('sacar captura')
            screenshot = pyautogui.screenshot()
            screenshot.save("D:\ cap" + str(number_of_cap) + ".png")
            time_next_screenshot = add_delta (now, step)
            number_of_cap += 1
            print(time_next_screenshot)
        if (now > endtime):
            break

screenshotmatic(time(22, 0, 0), 5) #Until 22:00, every 5 minutes
