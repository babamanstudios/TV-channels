import subprocess
import tkinter as tk
number = 1
def channel_selection(channel_number):
    channel_listing = ["https://www.youtube.com/watch?v=gCNeDWCI0vo",
                       "https://www.youtube.com/watch?v=YDvsBbKfLPA",
                       "https://www.youtube.com/watch?v=pykpO5kQJ98",
                       "https://www.youtube.com/watch?v=Ap-UM1O9RBU",
                       "https://www.youtube.com/watch?v=-cmNZazWqcI",
                       "https://www.youtube.com/watch?v=iipR5yUp36o",
                       "https://www.youtube.com/watch?v=LuKwFajn37U",
                       "https://www.youtube.com/watch?v=daqB3i9WYIY",
                       "https://www.youtube.com/watch?v=1YHUvehHbVs",
                       "https://www.youtube.com/watch?v=2PzfL3zrE-o",]
    channel = channel_listing[channel_number]
    return channel
def channel_names(channel_number):
    channel_names = ['Aljazeera',
                     'skynews',
                     'euronews',
                     'france24',
                     'trt english',
                     'abc news',
                     'dw',
                     'love nature',
                     'river monsters',
                     'spiderman']
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
pluss = str('+')
minuss = str('-')
button2 = tk.Button(window, text="+", command= lambda:numbering(1))
button2.place(x=200, y=100)
button3 = tk.Button(window, text="-", command= lambda:numbering(0))
button3.place(x=200, y=150)
window.mainloop()



window.mainloop()


