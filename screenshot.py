import time
import pyautogui
import tkinter as tk

def screenshot():
    name = int(round(time.time() * 1000))
    name = 'C:/Users/Amin/Desktop/ScreenShotAppProject/screenshots data//{}.png'.format(name)
    time.sleep(2)
    img = pyautogui.screenshot(name)
    img.show()
    
screenshot()    
    
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(
    frame,
    text = "Take screenshot",
    command = screenshot
)    

button.pack(side = tk.LEFT)
close = tk.Button(
    frame,
    text = "Quit",
    command = quit
)

close.pack(side = tk.LEFT)
close = tk.Button(
    frame,
    text = "Quit",
    command = quit
)

root.mainloop()