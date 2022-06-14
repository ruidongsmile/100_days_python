import tkinter
from tkinter import *

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=40, pady=40)

def button_clicked():
    print("I got clicked!")
    my_label["text"] = input.get()

#Label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
# my_label.pack(side="bottom")

my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

#Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

# New button
# button2 = Button(text="New Button", )
# button2.grid(column=2, row=0)

#Entry

input = Entry(width=10)
input.grid(column=3, row=2)
print(input.get())
















window.mainloop()