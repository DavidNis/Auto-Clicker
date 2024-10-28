import pyautogui
import time
import keyboard
import threading

interval = 300  # 5 minutes
pause = threading.Event()
terminate = threading.Event()

def clicker():
    while not terminate.is_set():
        if not pause.is_set():
            pyautogui.click()
            print('Clicked')
        for _ in range(interval):
            if terminate.is_set():
                break
            time.sleep(1)

def key_listener():
    while not terminate.is_set():
        if keyboard.is_pressed('Ctrl + s'):
            if pause.is_set():
                print("Resumed")
                pause.clear()
            else:
                print("Paused")
                pause.set() # pause clicking
            time.sleep(1)
        if keyboard.is_pressed('Ctrl + q'):
            print("Terminated...Goodbye :)")
            terminate.set()
            break

print("Press 'Ctrl + s' to pause/resume clicking")
print("Press 'Ctrl + q' to terminate the program")

time.sleep(1)
clicker_thread = threading.Thread(target=clicker)
clicker_thread.start()

key_listener_thread = threading.Thread(target=key_listener)
key_listener_thread.start()

clicker_thread.join()
key_listener_thread.join()
