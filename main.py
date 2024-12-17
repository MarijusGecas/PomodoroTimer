from tkinter import *
import math
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
started = False

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps, started
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    window.after_cancel(timer)
    title.config(text="Timer")
    checkmark.config(text="")
    started = False

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps, started
    if not started:
        started = True
        reps += 1
        work_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60
        if reps % 8 == 0:  # Long break
            count_down(long_break_sec)
            title.config(text="Long Break", fg=RED)
        elif reps % 2 == 0:  # Short break
            count_down(short_break_sec)
            title.config(text="Short Break", fg=PINK)
        else:  # Work session
            count_down(work_sec)
            title.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        work_sessions = math.floor(reps/2)
        marks = ""
        for _ in range(work_sessions):
            marks += "✓"
        checkmark.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

title = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
title.grid(row=0, column=1)

start = Button(text="Start", font=(FONT_NAME, 12, "bold"), bg=YELLOW, command=start_timer)
start.grid(row=2, column=0)

reset = Button(text="Reset", font=(FONT_NAME, 12, "bold"), bg=YELLOW, command=reset_timer)
reset.grid(row=2, column=2)

checkmark = Label(text="✓", font=(FONT_NAME, 15, "bold"), fg=GREEN, bg=YELLOW)
checkmark.grid(row=3, column=1)







window.mainloop()