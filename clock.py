import tkinter as tk
import time
from PIL import ImageFont

def updateTime():
      
	currentTime = time.strftime("%H:%M") 
	currentSecond = time.strftime("%S")
	dayName = time.strftime("%a")  #%A for Full day name (e.g., "Monday"), %a for short name(e.g., "Mon")
	today = time.strftime("%Y/%m/%d")  #Date in yyyy-mm-dd format

	dateLabel.config(text = f"{today} | {dayName}")
	timeLabel.config(text = currentTime)
	secondLabel.config(text = currentSecond)
    
	root.after(1000, updateTime)


windowWidth = 1024
windowHeight = 600

root = tk.Tk()
root.title("ClockPage") 
root.geometry(f"{windowWidth}x{windowHeight}")	#setting windowsize for testing 
#root.attributes("-fullscreen", True)	#make the soft fullscreen
canvas = tk.Canvas(root, width = windowWidth, height = 2)
canvas.create_line(0, 0, windowWidth, 0, fill = "#600000")

fontPath = "../font/CaviarDreams_Bold.ttf"

dateLabel = tk.Label(
    root,
    foreground = "#600000",
    font = ImageFont.truetype(fontPath, 40),
    pady = 50
)

timeLabel = tk.Label(
    root,
    foreground = "#600000",
    font = ImageFont.truetype(fontPath, 250),
    pady = 0
)

secondLabel = tk.Label(
    root,
    foreground = "#600000",
    font = ImageFont.truetype(fontPath, 50)
)

dateLabel.pack()
canvas.pack()
timeLabel.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER)
secondLabel.place(relx = 0.9, rely = 0.725, anchor = tk.SW) #increase x => going rigiht, increase y => going down

#def close_window(event = None):
#    root.attributes('-fullscreen', False)  
#    root.destroy()

#root.bind('<Escape>', close_window)
updateTime()
root.mainloop()