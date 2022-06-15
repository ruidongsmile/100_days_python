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
times = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(times)
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer")
    check.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global times
        times = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += check_mark
        check.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
check_mark = "✔"




canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1,  column=1)


# Label "Timer"
timer = Label(text="Timer",fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"), )
timer.grid(row=0, column=1)

# Label "Check mark"
check = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30))
check.grid(row=3, column=1)


# Button "Start"
start = Button(text="Start", command=start_timer)
start.grid(row=2, column=0)

# Button "Reset"
reset = Button(text="Reset", command=reset_timer)
reset.grid(row=2, column=2)








window.mainloop()