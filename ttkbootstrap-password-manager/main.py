import random
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pyperclip
import json
import ttkbootstrap as tb

TXT_DIRECTION = "passwords.txt"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # Password Generator Project

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for letter in range(nr_letters)]
    password_list += [random.choice(symbols) for symbol in range(nr_symbols)]
    password_list += [random.choice(numbers) for num in range(nr_numbers)]

    random.shuffle(password_list)

    password = ''.join(password_list)
    pyperclip.copy(password)

    print(f"Your password is: {password}")
    password_input.delete(0, END)
    password_input.insert(0, string=f"{password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_new():
    website = website_input.get()
    email = email_input.get()
    username = email_text_input.get()
    password = password_input.get()
    
    input_list = [website, email, username, password]
    new_line = ' | '.join(input_list)


    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Password Manager", message="Required fields empty")
    else:
        with open("passwords.txt", "a") as passwords:
            passwords.write(f"\n{new_line}")
            website_input.delete(0, END)
            email_text_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = tb.Window(themename="darkly")
window.title("Password manager")
window.geometry('500x400')

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Labels
label_website = Label(text="Website:", font=("Century Gothic", 12, "bold"), padx=10)
label_website.grid(column=0, row=1)
label_email = Label(text="Email:", font=("Century Gothic", 12, "bold"), padx=10)
label_email.grid(column=0, row=2)
label_username = Label(text="Username:", font=("Century Gothic", 12, "bold"), padx=10, pady=10)
label_username.grid(column=0, row=3)
label_password = Label(text="Password:", font=("Century Gothic", 12, "bold"), padx=10)
label_password.grid(column=0, row=4)

# Entries
website_input = Entry(width=36)
website_input.grid(column=1, row=1, columnspan=2, sticky="EW")
website_input.focus()
# email_input = Entry(width=36, font=("Century Gothic", 10, "normal"))
# email_input.insert(0, string="ruhlmirkojoel@gmail.com")
email_input = ttk.Combobox(
    state="readonly",
    values=["ruhlmirkojoel@gmail.com", "mirkaapo.709@gmail.com", "thrallclassicwc3@gmail.com",
            "mirkaapo.709@hotmail.com", "N/A"],
    font=("Century Gothic", 10, "normal")
)
email_input.current(0)
email_input.grid(column=1, row=2, columnspan=2, sticky="EW")

email_text_input = Entry(width=36, font=("Century Gothic", 10, "normal"))
email_text_input.grid(column=1, row=3, columnspan=2, sticky="EW")

password_input = tb.Entry(width=21, show="*")
password_input.grid(column=1, row=4, sticky="EW")

# Buttons
# , "normal"),
style = tb.Style()
button_style = 'danger.Outline.TButton'
style.configure(button_style, font=("Century Gothic", 10))
button = tb.Button(text="Generate Password",
                command=generate_password,
                bootstyle="success",
                style=button_style
                   )
button.grid(column=2, row=4)


important = 'danger.TButton'
style.configure(important, font=("Century Gothic", 12, "bold"))
add = tb.Button(text="Add", command=add_new, style=important)
add.grid(column=1, row=5, columnspan=2, sticky="EW", pady=(10, 0))

# delete button WORK IN PROGRESS
# delete = Button(text="🗑 prev", font=("Century Gothic", 10, "normal"))
# delete.grid(column=0, row=5, sticky="EW")

window.mainloop()
