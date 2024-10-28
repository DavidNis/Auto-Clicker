import pyautogui
import time
import keyboard

running = True
paused = False

def stop_prog():
    global running
    running = False
    print("Exiting program.")

def pause_prog():
    global paused
    paused = not paused
    print("Paused" if paused else "Resumed")

keyboard.add_hotkey('ctrl+q', stop_prog)
keyboard.add_hotkey('ctrl+s', pause_prog)

print("Press ctrl+q to stop the program")
print("Press ctrl+s to pause the program")
time.sleep(2)


while running:
    if not paused:
        pyautogui.click()
        print("Clicked!")
        
    for _ in range(300): 
        if not running:
            break
        time.sleep(1)
