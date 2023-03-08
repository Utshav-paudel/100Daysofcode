from tkinter import *
window = Tk()

#window
window.minsize(width=60, height= 70)
window.title("Miles to km converter")
window.config(padx=20 ,pady=20)

# label
label_miles = Label(text= "Miles")
label_miles.grid(row=0,column=3)

label_km = Label(text="KM")
label_km.grid(row=2,column=3)

label_equal = Label(text= "is equals to")
label_equal.grid(row=2,column=0)
# function to convert miles to km
def convert():
    miles_input=float(entry_miles.get())
    km = 1.60934*miles_input
    label_km_display = Label()
    label_km_display.config(text=f"{km}")
    label_km_display.grid(row=2 , column=2)

# entry box to enter miles
entry_miles = Entry()
entry_miles.grid(row=0,column=2)

# button
button = Button()
button.config(text="Convert" , command=convert )
button.grid(row=3,column=2)

window.mainloop()