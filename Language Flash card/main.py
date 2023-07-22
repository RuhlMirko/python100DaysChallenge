BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random

data = pandas.read_csv("./data/german_words.csv")
to_learn = data.to_dict(orient="records")

def next_word():
    canvas.itemconfig(canvas_image, image=card_front)

    current_card = random.choice(to_learn)
    canvas.itemconfig(title_text, text="German")
    canvas.itemconfig(word_text, text=current_card["German"])

    window.after(3000, english_word, current_card)

def english_word(current_word):
    canvas.itemconfig(canvas_image, image=card_back)

    current_card = current_word
    canvas.itemconfig(title_text, text="English")
    canvas.itemconfig(word_text, text=current_card["English"])

    window.after(3000, next_word)


window = Tk()
window.title("Flash card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)



canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)
title_text = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, highlightthickness=0)
right_button.grid(row=1, column=1)

next_word()

window.mainloop()
