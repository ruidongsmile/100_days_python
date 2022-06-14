from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
# window.minsize(width=500, height=300)
window.config(padx=40, pady=40)

def mile_to_km():
    label4["text"] = str(round(float(input.get()) * 1.60934, 2))

# # Label0 "Blank"
# label0 = Label()
# label0.grid(column=0, row=0)

# Label1 "is equal to"
label1 = Label(text="is equal to ", font=("Arial", 12, "bold"))
label1.grid(column=0, row=1)


# Label2 "Miles"
label2 = Label(text=" Miles", font=("Arial", 12, "bold"))
label2.grid(column=2, row=0)

# Label3 "Km"
label3 = Label(text=" Km", font=("Arial", 12, "bold"))
label3.grid(column=2, row=1)


# Label4 result
label4 = Label(text="0", font=("Arial", 12, "bold"))
label4.grid(column=1, row=1)


# Input
input = Entry(width=10)
input.grid(column=1, row=0)


# Button "Calculate"
button = Button(text="Calculate", command=mile_to_km)
button.grid(column=1, row=2)













window.mainloop()