from tkinter import *
from password_generator import gen_pass


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

# base windows for the ap   p
window = Tk()
# window.columnconfigure(0, weight=1)
# window.columnconfigure(1, weight=1)
# window.columnconfigure(2, weight=1)
# window.rowconfigure(0, weight=1)
# window.rowconfigure(1, weight=1)
# window.rowconfigure(2, weight=1)
# window.rowconfigure(3, weight=1)
# window.rowconfigure(4, weight=1)
window.title("Password Manager")
window.config(padx=20, pady=20, bg=YELLOW)
canvas = Canvas(width=200, height=200, highlightthickness=0, bg=YELLOW)
password_image = PhotoImage(file="pass_lock.png")
canvas.create_image(100, 100, image=password_image)
canvas.grid(row=0, column=1)

# label designs
website_l = Label(font=("Arial", 12, "bold"), text="Website", bg=YELLOW)
website_l.grid(column=0, row=1)
email_l = Label(font=("Arial", 12, "bold"), text="Email/Username", bg=YELLOW)
email_l.grid(column=0, row=2)
password_l = Label(font=("Arial", 12, "bold"), text="Password", bg=YELLOW)
password_l.grid(column=0, row=3)

# all entries here
website_entry = Entry(width=35, bg=YELLOW)
website_entry.grid(column=1, row=1, columnspan=2)
email_entry = Entry(width=35, bg=YELLOW)
email_entry.grid(column=1, row=2, columnspan=2)
pass_entry = Entry(width=21, bg=YELLOW)
pass_entry.grid(row=3, column=1)


# main functionality
def generator():
    pass_entry.insert(0, gen_pass())


# buttons
genpass_button = Button(text="Generate Password", command=generator, bg=YELLOW)
genpass_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, bd=1, bg=YELLOW)
add_button.grid(row=4, column=1, columnspan=2)

# main loop to run the app
window.mainloop()
