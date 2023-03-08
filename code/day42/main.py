from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    lablel_tick.config(text = "")
    lablel_timer.config(text="Timer")
    canvas.itemconfig(canvas_timer , text = "00:00")
    global reps
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    
    if reps % 8 == 0:
        lablel_timer.config(text = "Rest",fg=RED)
        count_down(LONG_BREAK_MIN*60)
    elif reps %2 == 0:
        lablel_timer.config(text = "Rest",fg=PINK)
        count_down(SHORT_BREAK_MIN*60)
    else:
        lablel_timer.config(text = "Work",fg=GREEN)
        count_down(WORK_MIN*60)        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    min = count//60
    sec = count % 60
    if  sec < 10:
        sec = f"0{sec}"
    if count >0:
        global timer
        canvas.itemconfig(canvas_timer , text = f"{min}:{sec}")
        timer = window.after(1000,count_down,count -1)
    else:
        marks = ""
        worksession = reps//2
        for i in range(worksession):
            marks +="✔"
        lablel_tick.config(text=marks) 
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)

# creating canvas
canvas = Canvas(width=200 , height=224 ,bg=YELLOW , highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image = tomato_img)
canvas_timer = canvas.create_text(100,130,text= "00:00" , fill="white", font =(FONT_NAME,35,"bold"))
canvas.grid(row=2,column=2)

# Lets create some label
#timer
lablel_timer = Label(text="Timer")
lablel_timer.config(font=(FONT_NAME,30,"bold") , fg=GREEN ,bg=YELLOW,highlightthickness=0)
lablel_timer.grid(row=1,column=2)
#tick
lablel_tick = Label(text="")
lablel_tick.config(fg=GREEN , bg=YELLOW, highlightthickness=0)
lablel_tick.grid(row=4,column=2)

##Button
start_button = Button(text="Start", command=start_timer)
start_button.grid(row=3,column=1)

reset_button = Button(text="Reset",command=reset_timer)
reset_button.grid(row=3,column=3)

window.mainloop()