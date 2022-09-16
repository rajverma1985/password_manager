from tkinter import *

# TO DO:
# password managed, UI , saving passwords
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

# base windows for the app
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200, highlightthickness=0)
password_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_image)
canvas.grid(row=0, column=1)

website_l = Label(font=("Arial", 12, "bold"), text="Website")
website_l.grid(column=0, row=1)
email_l = Label(font=("Arial", 12, "bold"), text="Email/Username")
email_l.grid(column=0, row=2)
password_l = Label(font=("Arial", 12, "bold"), text="Password")
password_l.grid(column=0, row=3)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
pass_entry = Entry(width=21)
pass_entry.grid(row=3, column=1)

genpass_button = Button(text="Generate Password")
genpass_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, bd=1)
add_button.grid(row=4, column=1, columnspan=2)

# main loop to run the app
window.mainloop()
