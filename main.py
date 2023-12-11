from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters=[choice(letters) for char in range(randint(8, 10))]
    password_symbols=[choice(symbols) for char in range(randint(2, 4))]
    password_numbers=[choice(numbers) for char in range(randint(2, 4))]

    password_list=password_numbers+password_symbols+password_letters

    shuffle(password_list)
    password="".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website=web_var.get()
    e_mail=mail_var.get()
    password=password_var.get()

    if len(website)==0 or len(password)==0:
        messagebox.showwarning(title="Empty Spaces",message="Dont Leave Any Empty Spaces")
    else:
        is_okay = messagebox.askokcancel(title=website, message=f"E-Mail: {e_mail}\n"
                                                                f"Password: {password}\n"
                                                                f"Is It Okay to save?")
        if is_okay:
            with open("data.txt", mode="a") as file:
                file.write(f"{website} | {e_mail} | {password}\n")
                web_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()

window.title("Password Generator")
window.config(padx=50,pady=50)

logo=PhotoImage(file="logo.png")
canvas=Canvas(width=200,height=200)
canvas.create_image(100,100,image=logo)
canvas.grid(column=1,row=0)

web_label=Label(text="Website:")
web_label.grid(row=1,column=0)

name_label=Label(text="E-Mail/Username:")
name_label.grid(row=2,column=0)

password_label=Label(text="Password")
password_label.grid(row=3,column=0)

web_var=StringVar()
web_entry=Entry(width=55,textvariable=web_var)
web_entry.grid(row=1,column=1,columnspan=2)

mail_var=StringVar()
name_entry=Entry(width=55,textvariable=mail_var)
name_entry.grid(row=2,column=1,columnspan=2)
name_entry.insert(0,"berkay@mail.com")

password_var=StringVar()
password_entry=Entry(width=35,textvariable=password_var)
password_entry.grid(row=3,column=1)

generate_button=Button(text="Generate Password",command=generate_password)
generate_button.grid(row=3,column=2)


add_button=Button(text="Add",width=45,command=add_password)
add_button.grid(row=4,column=1,columnspan=2)




window.mainloop()