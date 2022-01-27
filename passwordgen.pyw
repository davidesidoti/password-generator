import string
import random
import tkinter
from tkinter import *

caratteri = list(string.ascii_letters + string.digits + "!@#$%^&*()")

lunghezza = 16

random.shuffle(caratteri)

password = []
for i in range(lunghezza):
    password.append(random.choice(caratteri))

random.shuffle(password)

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

text = Text(window, width=50, height=10)
text.pack()
text.insert(tkinter.END, "".join(password))
text.configure(state="disabled")

window.mainloop()
