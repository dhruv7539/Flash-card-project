import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"

windows = Tk()
windows.title("Flash card ")
windows.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

# -----------------------------------------make dictionary---------------------------------------------
to_learn={}
current_card={}

try:
    data=pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data=pandas.read_csv("data/french_words.csv")
    to_learn=original_data.to_dict(orient='records')
else:
    to_learn=data.to_dict(orient="records")


def next_card():
    global current_card,flip_timer
    windows.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_txt,text="French",fill='black')
    canvas.itemconfig(word_txt,text=current_card["French"],fill="black")
    canvas.itemconfig(card_background,image=card_front_img)
    flip_timer=windows.after(3000,flip_card)

def is_known():
    to_learn.remove(current_card)
    data=pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn",index=False)
    next_card()

def flip_card():
    canvas.itemconfig(card_background, image=back_card_img)
    canvas.itemconfig(title_txt,text="English",fill="white")
    canvas.itemconfig(word_txt,text=current_card["English"],fill="white")

# -----------------------------------------text---------------------------------------------

# -----------------------------------------text---------------------------------------------


# -----------------------------------------text---------------------------------------------
flip_timer=windows.after(3000,next_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_background=canvas.create_image(400, 263, image=card_front_img)
back_card_img = PhotoImage(file='images/card_back.png')
title_txt=canvas.create_text(400, 150, text="Title", font=("ariel", 40, "italic"))
word_txt=canvas.create_text(400, 263, text="Word", font=("ariel", 40, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

next_card()
# -----------------------------------------button---------------------------------------------

right_img = PhotoImage(file="images/right.png")
right_btn = Button(image=right_img, bg=BACKGROUND_COLOR, highlightthickness=0,command=is_known)
right_btn.grid(row=1, column=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_img, bg=BACKGROUND_COLOR, highlightthickness=0,command=next_card)
wrong_btn.grid(row=1, column=0)

windows.mainloop()
