from tkinter import *
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
FONT = "Arial"
current_word = {}

# ---------------------------- DATA ------------------------------- #
try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("data/french_words.csv")
    words = df.to_dict(orient="records")
else:
    words = df.to_dict(orient="records")
# ---------------------------- NEXT CARD ------------------------------- #
def next_card():
    global current_word, flip_card
    window.after_cancel(flip_card)
    current_word = choice(words)

    canvas.itemconfig(flashcard, image=front_card_img)
    canvas.itemconfig(lang_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_word["French"], fill="black")

    flip_card = window.after(3000, card_flip)

# ---------------------------- CARD FLIP ------------------------------- #
def card_flip():
    canvas.itemconfig(flashcard, image=back_card_img)
    canvas.itemconfig(lang_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_word["English"], fill="white")


# ---------------------------- REMOVE CARD ------------------------------- #
def remove_card():
    global df
    df = df[df.French != current_word["French"]]
    df.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy Flashcard")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_card = window.after(3000, card_flip)

# Flashcard Image
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

front_card_img = PhotoImage(file="images/card_front.png")
back_card_img = PhotoImage(file="images/card_back.png")
flashcard = canvas.create_image(400, 263, image=front_card_img)

lang_text = canvas.create_text(400, 150, text="", fill="black", font=(FONT, 40, "italic"))
word_text = canvas.create_text(400, 263, text="", fill="black", font=(FONT, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
right_btn_img = PhotoImage(file="images/right.png")
right_btn = Button(image=right_btn_img, highlightthickness=0, command=remove_card)
right_btn.grid(column=1, row=1)

wrong_btn_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_btn_img, highlightthickness=0, command=next_card)
wrong_btn.grid(column=0, row=1)


next_card()
print(df[df.French == "pardon"])




















window.mainloop()

