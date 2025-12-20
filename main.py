import subprocess
import tkinter as tk
number = 1
def channel_selection(channel_number):
    with open('channels_links', 'r') as file:
        channel_listing = [line.strip() for line in file]

    channel = channel_listing[channel_number]
    return channel
def channel_names(channel_number):
    with open('channel_names', 'r') as file:
        channel_names = [line.strip() for line in file]
    channel = channel_names[channel_number]
    return channel
def channel_run():
    global number
    url = channel_selection(number)
    subprocess.Popen([
        "mpv",
        url
    ])
def numbering(sign):
    global number
    if sign == 1:
        number += 1
    elif sign == 0:
        number -= 1
    display.config(text=channel_names(number))


def clear():
    display.destroy()
window = tk.Tk()
window.title("BaBaTV")
window.geometry("500x500")
display = tk.Label(window, text=channel_names(number))
display.place(x=200, y=200)

button = tk.Button(window, text="start", command=channel_run)
button.place(x=50, y=100)
button2 = tk.Button(window, text="+", command= lambda:numbering(1))
button2.place(x=200, y=100)
button3 = tk.Button(window, text="-", command= lambda:numbering(0))
button3.place(x=200, y=150)
notice = tk.Label(window, text='Please do not spam click the start button after  clicking it once,it take time to load')
notice.place(x=0, y=300)
window.mainloop()



window.mainloop()


