import math
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
counter = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global counter, reps
    if counter is not None:
        window.after_cancel(counter)
    reps = 0
    canvas.itemconfig(item_text, text="00:00")
    timer_label.config(text="Timer", foreground=GREEN)
    checkbox.config(text="")



# ---------------------------- TIMER MECHANISM ------------------------------- #
def restart_timer():
    global reps
    reps +=1

    work_timer = WORK_MIN * 60
    short_break_timer = SHORT_BREAK_MIN * 60
    long_break_timer = LONG_BREAK_MIN *60

    if reps % 8 == 0:
        count_down(long_break_timer)
        timer_label.config(text="Long break", foreground=RED)
    elif reps % 2 == 0:
        count_down(short_break_timer)
        timer_label.config(text="Short break", foreground=PINK)
    else:
        count_down(work_timer)
        timer_label.config(text="Work", foreground=GREEN)
        # checkbox.config(text="✔")



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(timer):
    time_min = math.floor(timer/60)
    time_sec = timer % 60
    if time_sec == 0 or time_sec < 10:
        time_sec = f"0{time_sec}"
    canvas.itemconfig(item_text, text=f"{time_min}:{time_sec}")
    if timer > 0:
        global counter
        counter = window.after(1000,count_down, timer-1)
    else:
        restart_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "✔"
        checkbox.config(text=marks)








# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# Photo image class to store image file
pomodoro_image = PhotoImage(file="tomato.png")

# Canvas Widget
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image = pomodoro_image)
item_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill= "white")
canvas.grid(column=2, row=2)

# label windows
timer_label= Label(text="Timer", foreground=GREEN, font=(FONT_NAME, 35, "bold"), background=YELLOW)
timer_label.grid(column=2, row=1)

checkbox = Label(background=YELLOW, foreground=GREEN)
checkbox.grid(column=2, row=4)

# Button windows
start_label = Button(text="Start", highlightthickness=0, command=restart_timer)
start_label.grid(column=1, row=3)

reset_label = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_label.grid(column=3, row=3)




window.mainloop()