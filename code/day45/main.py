from tkinter import *
import pandas as pd  
import random
current_card = {}
try:
    data=pd.read_csv(r"C:\Users\utsha\OneDrive\Desktop\my learning\python fresh start\code\day45\data\word_tolearn.csv")
except FileNotFoundError:
    data = pd.read_csv(r"C:\Users\utsha\OneDrive\Desktop\my learning\python fresh start\code\day45\data\french_words.csv")
finally:
    new_data = data.to_dict(orient="records")
    print(new_data)

BACKGROUND_COLOR = "#B1DDC6"

# window setup
window = Tk()
window.config(padx=50 , pady=50 , bg=BACKGROUND_COLOR)
window.title(string="Flash card app")


#next card function
def next_card():
    global current_card , flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(new_data)
    french_word = current_card["French"]
    english_word = current_card["English"]
    canvas.itemconfig(canvas_title , text = "French" , fill = "black")
    canvas.itemconfig(canvas_text,text = f"{french_word}" , fill = "black" )
    canvas.itemconfig(canvas_img, image = front_img)
    flip_timer = window.after(3000, func= flip_card)

def flip_card():
    global current_card
    english_word = current_card["English"]
    canvas.itemconfig(canvas_img, image = back_img)
    canvas.itemconfig(canvas_title , text = "English" , fill = "white")
    canvas.itemconfig(canvas_text , text = f"{english_word}" , fill = "white")
    
def remove_known():
    global current_card
    new_data.remove(current_card)
    print(len(new_data))
    data = pd.DataFrame(new_data)
    data.to_csv("data/word_tolearn.csv")
    next_card()



# creating timer to filp the card
flip_timer = window.after(3000, func= flip_card)

#creating canvas for image
canvas = Canvas(width=800 , height=526)
front_img = PhotoImage(file=r"C:\Users\utsha\OneDrive\Desktop\my learning\python fresh start\code\day45\images\card_front.png")
back_img = PhotoImage(file=r"C:\Users\utsha\OneDrive\Desktop\my learning\python fresh start\code\day45\images\card_back.png")

canvas_img = canvas.create_image(400,263 , image = front_img)
canvas_title =canvas.create_text(400,150,text="Title", font=("Arial",40,"italic"))
canvas_text = canvas.create_text(400,263,text="text", font=("Arial",60,"bold"))
canvas.config(bg= BACKGROUND_COLOR , highlightthickness=0)
# canvas.grid(row=0 , column=0, columnspan=2)
canvas.grid(row=0 ,column=0,columnspan=2)

#creating tick and croos button
#tick button
tick_img = PhotoImage(file=r"C:\Users\utsha\OneDrive\Desktop\my learning\python fresh start\code\day45\images\right.png")
button_tick = Button(image=tick_img , highlightthickness=0, command=remove_known)
button_tick.grid(row=1, column=0)

#cross_button
cross_img = PhotoImage(file=r"C:\Users\utsha\OneDrive\Desktop\my learning\python fresh start\code\day45\images\wrong.png")
button_cross = Button(image=cross_img , highlightthickness=0 , command=next_card)
button_cross.grid(row=1, column=1)
next_card()








window.mainloop()