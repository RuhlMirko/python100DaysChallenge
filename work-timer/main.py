from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#1a0"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    window.after_cancel(timer)
    label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    print(reps)
    work = WORK_MIN * 60
    short = SHORT_BREAK_MIN * 60
    long = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long)
        label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short)
        label.config(text="Break", fg=PINK)
    else:
        count_down(work)
        label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    # print(count)
    global reps
    minutes = int(count/60)
    seconds = count % 60

    if seconds < 10:
        seconds = f"0{seconds}"
    if minutes < 10:
        minutes = f"0{minutes}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark=""
        work_sessions = int(reps/2)
        for i in range(work_sessions):
            mark += "✔"
            check_mark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


label = Label(text="Timer", font=("Segoe UI", 35, "bold"), fg=GREEN)
label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

# count_down(5)

canvas.grid(column=1, row=1)

button_start = Button(text="Start", padx=10, highlightthickness=0, command=start_timer)
button_start.grid(column=0, row=3)

button_reset = Button(text="Reset", padx=10, highlightthickness=0, command=reset_timer)
button_reset.grid(column=2, row=3)

# text="✔"
check_mark = Label(font=("Segoe UI", 15, "bold"), fg=GREEN)
check_mark.grid(column=1, row=4)



window.mainloop()
