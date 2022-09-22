from tkinter import messagebox
from tkinter import *
from password_generator import gen_pass
from models import Passman
from databases import insert_info, get_info, remove_info, update_info

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

# base windows for the app
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200, highlightthickness=0)
password_image = PhotoImage(file="pass_lock.png")
canvas.create_image(100, 100, image=password_image)
canvas.grid(row=0, column=1)

# label designs
website_l = Label(font=("Arial", 12, "bold"), text="Website")
website_l.grid(column=0, row=1)
email_l = Label(font=("Arial", 12, "bold"), text="Email/Username")
email_l.grid(column=0, row=2)
password_l = Label(font=("Arial", 12, "bold"), text="Password")
password_l.grid(column=0, row=3)

# all entries here
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
pass_entry = Entry(width=21)
pass_entry.grid(row=3, column=1)


# main functionality
def generator():
    pass_entry.insert(0, gen_pass())


def save_password():
    # get all the data from the entry fields first
    website = website_entry.get()
    password = pass_entry.get()
    email = email_entry.get()
    entry_object = Passman(email, website, password)
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Entry Error", message="Please enter a valid website or password")
    else:
        # write stuff to the database
        insert_info(entry_object)
        website_entry.delete(0, END)
        email_entry.delete(0, END)
        pass_entry.delete(0, END)


# buttons
genpass_button = Button(text="Generate Password", command=generator)
genpass_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

# main loop to run the app
window.mainloop()
