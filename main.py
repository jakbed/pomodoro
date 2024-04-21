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
CHECKMARK = "☑"
reps = 0
timer = None
marks = ""

# ---------------------------- TIMER RESET ------------------------------- # 
def pomidoro_reset():
    window.after_cancel(timer)
    title.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    checkmarks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM -------------------------------
work_sec = WORK_MIN *60
short_break_sec = SHORT_BREAK_MIN * 60
long_break_sec = LONG_BREAK_MIN * 60
def start_timer():
    global reps
    reps+=1

    if reps % 8 == 0:
        time = long_break_sec
        title.config(text="LONG BREAK", fg=RED)
    elif reps % 2 == 0:
        time = short_break_sec
        title.config(text="BREAK", fg=PINK)
    else:
        time = work_sec
        title.config(text="WORK", fg=GREEN)

    pomidoro_start(time)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def pomidoro_start(count):
    count_min = math.floor(count /60)
    count_sec = count % 60
    if count_sec <10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, pomidoro_start, count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += CHECKMARK
        checkmarks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomidoro")
window.config(padx=100, pady=50, bg=YELLOW)
canvas=Canvas(width="200", height="224", bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)

timer_text = canvas.create_text(100, 132, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

canvas.grid(row=1, column=1)


title = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40))
title.grid(row=0, column=1)

start = Button(text="Start", highlightbackground=YELLOW, font=(FONT_NAME), command=start_timer)
start.grid(row=2, column=0)

reset = Button(text="Reset", highlightbackground=YELLOW, command=pomidoro_reset)
reset.grid(row=2, column=2)

checkmarks = Label(text=f"{CHECKMARK*reps}", fg="GREEN", bg=YELLOW)
checkmarks.grid(row=3, column=1)

copyright_fi = Label(text="by JB\n from Dr.Angela UDEMY Course", fg="black", bg=YELLOW, font=(FONT_NAME, 14, "italic")).grid(row=6, column=1)



window.mainloop()