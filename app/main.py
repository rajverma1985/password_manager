from tkinter import messagebox
from tkinter import *
from password.password_generator import gen_pass
from db.models import Passman
from db.databases import insert_info, get_info
from tkinter import ttk

# import pyperclip   >>> ADD copy functionality to the app
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

# base windows for the app
window = Tk()
window.title("Password Manager")
# window.resizable(False, False)
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
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
pass_entry = Entry(width=21)
pass_entry.grid(row=3, column=1)


# main functionality
def generator():
    pass_entry.delete(0, END)
    pass_entry.insert(0, gen_pass())


def save_info():
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


def search():
    information = get_info(website_entry.get())
    if len(website_entry.get()) == 0:
        messagebox.showinfo(title="Blank Search", message="Blank Search")
    elif len(information) == 0:
        messagebox.showinfo(title="Blank Search", message="No results found!")
    else:
        for i in range(0, len(information)):
            messagebox.showinfo(title="Results",
                                message=f"Your info from {information[i][2]} is\n "
                                        f"email:{information[i][1]}\n password:{information[i][-1]}\n")


def table_create():
    table_frame = Frame(window)
    table_frame.grid(row=0, column=3)
    table = ttk.Treeview(table_frame)
    table['columns'] = ('id', 'email', 'website', 'password')

    table.column("#0", width=0, stretch=NO)
    table.column("id", anchor=CENTER, width=20, )
    table.column("email", anchor=CENTER, width=80)
    table.column("website", anchor=CENTER, width=100)
    table.column("password", anchor=CENTER, width=80)

    table.heading("#0", text="", anchor=CENTER)
    table.heading("id", text="ID", anchor=CENTER)
    table.heading("email", text="Email/UserName", anchor=CENTER)
    table.heading("website", text="Website", anchor=CENTER)
    table.heading("password", text="Password", anchor=CENTER)
    information = get_info(website_entry.get())
    if len(website_entry.get()) == 0:
        messagebox.showinfo(title="Blank Search", message="Blank Search")
    elif len(information) == 0:
        messagebox.showinfo(title="No results", message="No results found!")
    else:
        for i in range(0, len(information)):
            table.insert(parent='', index='end', iid=f'{i}', text='',
                         values=(f'{information[i][0]}', f'{information[i][1]}', f'{information[i][2]}',
                                 f'{information[i][3]}'))
    table.grid(row=0, column=5)


# buttons
search_button = Button(text="Search", width=13, command=table_create)
search_button.grid(row=1, column=2)
genpass_button = Button(text="Generate Password", command=generator)
genpass_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save_info)
add_button.grid(row=4, column=1, columnspan=2)

# main loop to run the app
window.mainloop()
