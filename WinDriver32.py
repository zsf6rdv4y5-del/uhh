
import tkinter as tk
from tkinter import messagebox

# Demonstration PIN — change this before using.
TEACHER_PIN = "2468"

root = tk.Tk()
root.title("Uh-Oh!")
root.configure(bg="black")
root.attributes("-fullscreen", True)
root.attributes("-topmost", True)

# Keep the window fullscreen without standard title-bar buttons.
# This is a visual deterrent, not a security boundary.
root.overrideredirect(True)

# Main layout
main = tk.Frame(root, bg="black")
main.place(relx=0.5, rely=0.5, anchor="center")

# Draw the red prohibition symbol.
canvas = tk.Canvas(
    main, width=150, height=150,
    bg="black", highlightthickness=0
)
canvas.pack(pady=(0, 20))

canvas.create_oval(
    15, 15, 135, 135,
    outline="#ff2020", width=9
)
canvas.create_line(
    35, 115, 115, 35,
    fill="#ff2020", width=10,
    capstyle=tk.ROUND
)

# Alert text
title = tk.Label(
    main,
    text="oops! you have been hacked!",
    font=("Arial", 32, "bold"),
    fg="#ff2020",
    bg="black"
)
title.pack(pady=10)

subtitle = tk.Label(
    main,
    text="All your files have been encrypted! They will be destroyed in 30:00",
    font=("Arial", 14),
    fg="white",
    bg="black"
)
subtitle.pack(pady=(0, 28))

# Teacher PIN field
pin_label = tk.Label(
    main,
    text="Fix-My-Shit code",
    font=("Arial", 11, "bold"),
    fg="#bbbbbb",
    bg="black"
)
pin_label.pack(pady=(0, 8))

pin_entry = tk.Entry(
    main,
    show="*",
    font=("Arial", 20),
    justify="center",
    width=16,
    bg="#202020",
    fg="white",
    insertbackground="white",
    relief="flat"
)
pin_entry.pack(ipady=8)
pin_entry.focus_set()

status = tk.Label(
    main, text="", font=("Arial", 11),
    fg="#ff4040", bg="black"
)
status.pack(pady=10)


def unlock(event=None):
    entered_pin = pin_entry.get()

    if entered_pin == TEACHER_PIN:
        root.overrideredirect(False)
        root.destroy()
    else:
        status.config(text="Nope")
        pin_entry.delete(0, tk.END)
        pin_entry.focus_set()


def emergency_exit(event=None):
    # Recovery shortcut for authorised testing.
    if messagebox.askyesno(
        "Emergency exit",
        "Exit?"
    ):
        root.overrideredirect(False)
        root.destroy()


unlock_button = tk.Button(
    main,
    text="UNLOCK",
    font=("Arial", 12, "bold"),
    fg="white",
    bg="#b00000",
    activebackground="#e02020",
    activeforeground="white",
    relief="flat",
    width=16,
    command=unlock
)
unlock_button.pack(pady=10, ipady=6)

pin_entry.bind("<Return>", unlock)

# Keep fullscreen for the demo.
root.bind("<F11>", lambda event: root.attributes(
    "-fullscreen", True
))

# Explicit emergency recovery shortcut.
root.bind("<Control-Shift-q>", emergency_exit)
root.bind("<Control-Shift-Q>", emergency_exit)

root.mainloop()
