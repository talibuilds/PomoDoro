from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#06631d"
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
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps +=1
    work_sec= WORK_MIN*60
    sb_sec= SHORT_BREAK_MIN*60 
    lb_sec= LONG_BREAK_MIN*60

    if reps ==8:
        title_label.config(text="Long Break", font=("Arial", 35, "bold"), fg=RED, bg=YELLOW)
        count_down(lb_sec)

    elif reps %2 ==0:
        title_label.config(text="Short Break", font=("Arial", 35, "bold"), fg=GREEN, bg=YELLOW)
        count_down(sb_sec)
        
    else:
        title_label.config(text="Work", font=("Arial", 35, "bold"), fg=PINK, bg=YELLOW)
        count_down(work_sec)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(num):
    global timer
    count_min = math.floor(num/60)
    count_sec = num %60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if (num>0):
        timer = window.after(1000, count_down, num-1)
    else:
        start_timer()
        mark = 0
        if reps !=0 and reps%2 ==0:
            mark +="✓"
            check_marks.config(text=mark, font=("Arial", 25, "bold"), bg=YELLOW, fg=GREEN)






# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("PomoDoro")
window.config(padx=50, pady=50, bg=YELLOW)


canvas = Canvas(width=300, height=400, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(150, 200, image=img)
timer_text = canvas.create_text(150, 200, text="00:00", font=("Arial", 25, "bold"), fill ="white")
canvas.grid(row=2, column=1)
title_label = Label(text="Timer", font=("Arial", 35, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(row=1, column=1)


start_btn = Button(text="START", font=("Arial", 15, "bold"), fg=GREEN, command=start_timer)
start_btn.grid(row=3, column=0)

Reset_btn = Button(text="RESET", font=("Arial", 15, "bold"), fg=RED, command=reset_timer)
Reset_btn.grid(row=3, column=2)

check_marks =Label(font=("Arial", 25, "bold"), bg=YELLOW, fg=GREEN )
check_marks.grid(row=3, column=1)

window.mainloop()