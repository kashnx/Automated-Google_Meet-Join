from time import sleep
import pyautogui as auto
import schedule, webbrowser

link = "meet.google.com/hkb-hxjd-jps"

time = "23:32" 


def join():
    webbrowser.open_new_tab('https://' + link)
    sleep(7)
    auto.hotkey('ctrl', 'd')
    auto.hotkey('ctrl', 'e')
    # auto.hotkey('command', 'd')
    # auto.hotkey('command', 'e')
    auto.click(1346, 591)


schedule.every().day.at(time).do(join)

while True:
    schedule.run_pending()
    sleep(1)
