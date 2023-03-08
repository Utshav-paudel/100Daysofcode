from tkinter import *

window = Tk()


# editing window
window.minsize(width= "300" , height= "300")
window.title("My first app")

# label
label = Label(text= "Hello")
label.config(text = "Welcome to facebook")
label.grid(column= 0 , row= 0)


# entry
#for email
email_box = Entry()
email_box.config(width=40)
email_box.insert(END , string= "someone@gmail.com")
email_box.get()
#print(email_box.get())
email_box.grid(column= 1 , row= 1)
#for passowrd
password_box = Entry()
password_box.config(width=40)
password_box.insert(END , string= "enter you password")
password_box.get()
#print(password_box.get())
password_box.grid(column= 1 , row= 2)



# button
def action():
    print("Button pressed")
    print(f"email:{email_box.get()}")
    print(f"password:{password_box.get()}")
button = Button(text= "Submit" ,command= action ,)
button.grid(column= 1 , row= 3)

# text boxt
text = Text(width = "30" , height=" 5")
text.focus()
text.insert(END,"write something about yourself")
print(text.get("1.0",END))
text.grid(column= 4 , row= 4)


window.mainloop()