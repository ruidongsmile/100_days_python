from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project

def generate_passord():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    pwd_ent.insert(0, password)
    pyperclip.copy(password)

    # print(f"Your password is: {password}")

# ---------------------------- CLEAR EVERYTHING ------------------------------- #
def clear_pwd():
    web_ent.delete(0, 'end')
    pwd_ent.delete(0, 'end')

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_pwd():
    web = web_ent.get()
    pwd = pwd_ent.get()
    usr = usr_ent.get()



    if (web != "") and (pwd != ""):
        is_ok = messagebox.askokcancel(title=usr, message=f"These are the details entered: \nWebsite: {web} "
                           f"\nPassword: {pwd} \nIs it OK to save?")
        if is_ok:
            f = open("data.txt", "a")
            f.write(web + " | " + usr + " | " + pwd + '\n')
            f.close()
        web_ent.delete(0,'end')
        pwd_ent.delete(0,'end')
    else:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty...")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, )  # bg='white', highlightthickness=0

canvas = Canvas(width=200, height=200, ) # bg="white"
pwd_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pwd_img)

canvas.grid(row=0, column=1)



# Label website:
web_lb = Label(text="Website: ", font=("Courier", 15, "bold"))
web_lb.grid(row=1, column=0)

# Label email/username:
usr_lb = Label(text="Email/Username: ", font=("Courier", 15, "bold"))
usr_lb.grid(row=2, column=0)

# Label password
pwd_lab = Label(text="Password: ", font=("Courier", 15, "bold"))
pwd_lab.grid(row=3, column=0)

# Entry website:
web_ent = Entry(width=40)
web_ent.grid(row=1, column=1, columnspan=2)
web_ent.focus()

# Entry username:
usr_ent = Entry(width=40)
usr_ent.grid(row=2, column=1, columnspan=2)
usr_ent.insert(0, "ruidongshuai@gmail.com")

# Entry password:
pwd_ent = Entry(width=21, )
pwd_ent.grid(row=3, column=1)


# Button Generate Password
pwd_button = Button(text="Generate Password", command=generate_passord)
pwd_button.grid(row=3, column=2)

# Button Add
add_button = Button(text="Add", width=38, command=save_pwd)
add_button.grid(row=4, column=1, columnspan=2)

# Button Clear
clear_button = Button(text="Clear", width=38, command=clear_pwd)
clear_button.grid(row=5, column=1, columnspan=2)



window.mainloop()