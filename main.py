from tkinter import *
from tkinter import messagebox


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier New"
WORK_MIN = 0
SHORT_BREAK_MIN = 0
LONG_BREAK_MIN = 0
reps = 1
timer = NONE
WORKING_SESSIONS = 8


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    global reps
    reps = 1
    timer_lbl.config(text="😴😴😴", fg=GREEN)
    check.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    w_time_scale.set(0)
    b_time_scale.set(0)
    lb_time_scale.set(0)
    working_session.delete(0, "end")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    if reps % WORKING_SESSIONS == 0:
        messagebox.showinfo(title="Enough for now", message=f"Take a rest for {LONG_BREAK_MIN} minutes")
        timer_lbl.config(text="Break🥱🥱", fg=RED)
        countdown(LONG_BREAK_MIN * 60)
        reps += 1
    elif reps % 2 == 0:
        messagebox.showinfo(title="Enough for now", message=f"Take a rest for {SHORT_BREAK_MIN} minutes")
        timer_lbl.config(text="Break🥱", fg=PINK)
        countdown(SHORT_BREAK_MIN * 60)
        reps += 1
    else:
        messagebox.showinfo(title="Enough for now", message=f"Start working for next {WORK_MIN} minutes")
        timer_lbl.config(text="Work!📖", fg=GREEN)
        countdown(WORK_MIN * 60)
        reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def set_working_time(value):
    global WORK_MIN
    WORK_MIN = int(value)


def set_break_time(value):
    global SHORT_BREAK_MIN
    SHORT_BREAK_MIN = int(value)


def set_long_break_time(value):
    global LONG_BREAK_MIN
    LONG_BREAK_MIN = int(value)


def set_working_sessions():
    global WORKING_SESSIONS
    WORKING_SESSIONS = 2 * int(working_session.get())


def countdown(count):
    global timer
    minutes = count // 60
    sec = count % 60
    if count > -1:
        if sec < 10:
            sec = "0" + str(sec)
        canvas.itemconfig(timer_text, text=f"{minutes}:{sec}")
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        work_sessions = (reps - 1) // 2
        marks = ""
        for _ in range(work_sessions):
            marks += "✔"
        check.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=10, pady=50, bg=YELLOW)

w_time_scale_label = Label(text="Working time: ", font=(FONT_NAME, 12, "normal"), bg=YELLOW, fg=RED)
w_time_scale_label.grid(column=1, row=1, sticky="e")
w_time_scale = Scale(from_=0, to=60, orient=HORIZONTAL, command=set_working_time)
w_time_scale.config(bg=YELLOW, highlightthickness=0)
w_time_scale.grid(column=2, row=1, sticky=EW)

w_time_scale_label = Label(text="Short break time: ", font=(FONT_NAME, 12, "normal"), bg=YELLOW, fg=RED)
w_time_scale_label.grid(column=1, row=2, sticky="e")
b_time_scale = Scale(from_=0, to=60, orient=HORIZONTAL, command=set_break_time)
b_time_scale.config(bg=YELLOW, highlightthickness=0)
b_time_scale.grid(column=2, row=2, sticky=EW)

w_time_scale_label = Label(text="Long break time: ", font=(FONT_NAME, 12, "normal"), bg=YELLOW, fg=RED)
w_time_scale_label.grid(column=1, row=3, sticky="e")
lb_time_scale = Scale(from_=0, to=60, orient=HORIZONTAL, command=set_long_break_time)
lb_time_scale.config(bg=YELLOW, highlightthickness=0)
lb_time_scale.grid(column=2, row=3, sticky=EW)

working_session_label = Label(text="Working sessions\n   for long break: ", font=(FONT_NAME, 12, "normal"), bg=YELLOW,
                              fg=RED)
working_session_label.grid(column=1, row=4, sticky="e")
working_session = Spinbox(from_=0, to=10, command=set_working_sessions, width=5)
working_session.grid(column=2, row=4, sticky="w")

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=5)

timer_lbl = Label(text="😴😴😴", font=(FONT_NAME, 50, "normal"))
timer_lbl.config(bg=YELLOW, fg=GREEN)
timer_lbl.grid(column=2, row=0)

st_button = Button(text="Start", font=(FONT_NAME, 11, "normal"))
st_button.config(padx=50, pady=3, highlightthickness=0, command=start_timer)
st_button.grid(column=1, row=6)

rst_button = Button(text="Reset", font=(FONT_NAME, 11, "normal"))
rst_button.config(padx=50, pady=3, command=reset_timer, highlightthickness=0)
rst_button.grid(column=3, row=6)

check = Label(fg=GREEN)
check.config(bg=YELLOW, font=("Segoe UI Symbol", 20, "bold"))
check.grid(column=2, row=7)

window.mainloop()
