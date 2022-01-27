import string
import random
import tkinter
from tkinter import *


def gen(lenght):
    caratteri = list(string.ascii_letters + string.digits + "!@#$%^&*()")

    random.shuffle(caratteri)

    password = []
    for i in range(int(lenght)):
        password.append(random.choice(caratteri))

    random.shuffle(password)
    return "".join(password)


window = Tk()
window.title("Password Generator")
window.configure(width=300, height=100)
window.configure(bg='white')

# move window center
winWidth = window.winfo_reqwidth()
winwHeight = window.winfo_reqheight()
posRight = int(window.winfo_screenwidth() / 2 - winWidth / 2)
posDown = int(window.winfo_screenheight() / 2 - winwHeight / 2)
window.geometry("+{}+{}".format(posRight, posDown))

options = [8, 10, 12, 14, 16, 18, 20]
variable = StringVar(window)
variable.set(options[4])


def take_input():
    output.configure(state="normal")
    output.delete("insert linestart", "insert lineend")
    output.insert(INSERT, gen(variable.get()))
    output.configure(state="disabled")


inptdrpdown = OptionMenu(window, variable, *options)
output = Text(window, width=50, height=10, bg="light cyan")
btn = Button(window, width=15, height=2, text="Genera", command=lambda: take_input())

inptdrpdown.pack()
btn.pack()
output.pack()

window.mainloop()
