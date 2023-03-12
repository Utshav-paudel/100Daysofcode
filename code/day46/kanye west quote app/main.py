from tkinter import *
import requests


def get_quote():
    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    canvas.itemconfig(quote_text, text = f'{data["quote"]}')


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=400, height=400)
background_img = PhotoImage(file=r"C:\Users\utsha\OneDrive\Desktop\my learning\python fresh start\code\day46\kanye west quote app\background.png")
canvas.create_image(200, 207, image=background_img )
quote_text = canvas.create_text(200, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file=r"C:\Users\utsha\OneDrive\Desktop\my learning\python fresh start\code\day46\kanye west quote app\kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()