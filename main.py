from tkinter import *

count = 5
text = ""
timer = None


def is_typing(event):
    global timer, text

    if timer is not None:
        window.after_cancel(timer)

    if event.char:
        text += event.char
        timer = window.after(1000, update_timer)

    return

def update_timer():
    global count, timer
    count -= 1
    label.config(text=f"{count} sec")
    if count > 0:
        timer = window.after(1000, update_timer)
    if count == 0:
        user_input.delete("1.0", "end")
        reset()


def reset():
    global count
    count = 5
    label.config(text=f"{count} sec")


window = Tk()
window.title("Disappearing Text")
window.geometry("700x700")
# window.config()
user_input = Text(window, width=70, height=20, font=("Courier", 14))
user_input.pack()
user_input.bind("<KeyPress>", is_typing)
label = Label(text=f"{count} sec", fg="black", font=("Courier", 20), wraplength=400)
label.pack()


window.mainloop()



