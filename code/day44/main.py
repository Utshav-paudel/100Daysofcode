from tkinter import *
from tkinter import messagebox
import json
window = Tk()

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
def get_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    entry_password.insert(0,string=f"{password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():
    website = entry_website.get()
    email = entry_email.get()
    password =entry_password.get()
    new_data = {website : {
        "email":email,
        "password":password
    }}
    if len(website) == 0 and len(password) == 0:
        messagebox.showerror(title="Error" , message="Please enter your details")
    else:
        try:
            with open("data.json", "r") as file1: 
                #reading
                data = json.load(file1)
        except FileNotFoundError:
            with open("data.json","w") as file1:
                json.dump(new_data,file1,indent=4)
        else:
            #updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as file1:
                #saving updated data
                json.dump(data , file1,indent = 4)
        finally:
            entry_email.delete(0,END)
            entry_website.delete(0,END)
            entry_password.delete(0,END)
def search_data():
    website = entry_website.get()
    try:
        with open ("data.json") as file1:
            data = json.load(file1)
    except FileNotFoundError:
        messagebox.showinfo(title=website , message="No data found")
    else:
        if website in data:
            email =data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=f"{website}" , message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"Data for {website} doesnot exist")
       
    
# ---------------------------- UI SETUP ------------------------------- #

# window
window.title("Password Manager")
window.config(padx=20 , pady =20)


#canvas
canvas = Canvas(height=200 , width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image = logo_img)
canvas.grid(row=0, column = 1)


# creating some widget

label_webiste = Label(text="Website:")
label_webiste.grid(row=1 ,column=0)

lablel_email = Label(text= "Email/Username:")
lablel_email.grid(row=2 , column=0)

label_password = Label(text="Password:")
label_password.grid(row=3, column=0)
#entry
entry_website = Entry(width=33)
entry_website.focus()
entry_website.grid(row=1 , column=1 )


entry_email = Entry(width=51)
entry_email.insert(END, "someone@gmail.com")
entry_email.grid(row=2 ,column=1,columnspan=2)


entry_password = Entry(width=33)
entry_password.grid( row=3, column=1)


# button
generate_pass_button = Button(text="Generate Password" , command=get_pass)
generate_pass_button.grid(row=3 , column=2)

add_button = Button(text="Add", width=43,command=add_data)
add_button.grid(row=4,column=1, columnspan=2)

search_button = Button(text="Search", width=14 ,command=search_data)
search_button.grid(row=1,column=2)
window.mainloop()


    
   