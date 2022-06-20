import random
from tkinter import *
from random import choice, randint, shuffle
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/wiki.csv")
    vocab_list = original_data.to_dict(orient='records')
else:
    vocab_list = df.to_dict(orient='records')
current_card = {}

# ---------------------------- CLICK FUNCTION------------------------------- #

def check_click():
    vocab_list.remove(current_card)
    df = pd.DataFrame(vocab_list)
    df.to_csv("data/words_to_learn.csv", index=False)
    cross_click()

    # print(current_card)

def cross_click():
    global current_card, flip_timer
    # window.after_cancel(flip_timer)
    current_card = random.choice(vocab_list)

    rv_click()

def rv_click():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(title, text="Dutch", fill="black")
    canvas.itemconfig(word, text=current_card["Dutch"], fill="black")
    canvas.itemconfig(card_face, image=front_img)

    flip_timer = window.after(3000, func=flip_card)



    print(current_card)





def flip_card():
    eng_word = current_card["English"]
    canvas.itemconfig(card_face, image=back_img)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=eng_word, fill="white")







# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

back_img = PhotoImage(file="images/card_back.png")
front_img = PhotoImage(file="images/card_front.png")

canvas = Canvas(width=800, height = 526, highlightthickness=0)
card_face = canvas.create_image(400, 263, image=front_img)
title = canvas.create_text(400, 150, text="Language", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=3)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=check_click)
right_button.grid(row=1, column=2)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=cross_click)
wrong_button.grid(row=1, column=0)

rvw_img = PhotoImage(file="images/rv.png")
rvw_button = Button(image=rvw_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=rv_click)
rvw_button.grid(row=1, column=1)


cross_click()

window.mainloop()