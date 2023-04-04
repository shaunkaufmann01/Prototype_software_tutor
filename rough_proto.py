import pyautogui, sys

# pyautogui.size()
# pyautogui.position()
# pyautogui.dragTo(100, 200, button='left')
# pyautogui.moveTo(100, 200)
# pyautogui.moveTo(100, 100, 2, pyautogui.easeInQuad)
# pyautogui.click()
# pyautogui.press('f1')

from tkinter import *
from tkinter import ttk


def lift_window(window):
    window.attributes("-topmost", True)
    window.update_idletasks()  # get window on top
    window.attributes("-topmost", False)  # prevent permanent focus
    window.focus_force()  # focus to the window


def ttk_message(text, x, y):
    root = Tk()
    root.overrideredirect(True)
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text=text).grid(column=0, row=0)
    root.geometry("%dx%d+%d+%d" % (300, 40, x, y))
    lift_window(root)
    root.mainloop()


def execute_step(list_steps):
    secs_between_keys = 0.5
    for step in list_steps:
        if step["type"] == "move_mouse":
            pyautogui.moveTo(step["x"], step["y"], 2, pyautogui.easeInQuad)
        elif step["type"] == "click":
            pyautogui.click(button=step["button"])
        elif step["type"] == "enter":
            pyautogui.typewrite(step["text"], interval=secs_between_keys)
        elif step["type"] == "message_user":
            ttk_message(step["message"], step["x"], step["y"])


if __name__ == "__main__":
    # steps = [{"type":"move_mouse", "x":300,"y":300},{"type":"click", "button":"left"}]
    steps = [
        {"type": "move_mouse", "x": 112, "y": 429},
        {"type": "click", "button": "left"},
        {
            "type": "enter",
            "text": [
                "=",
                "S",
                "U",
                "M",
                "(",
            ],
        },
        {
            "type": "message_user",
            "message": "Select the fields you wish to sum and hit enter",
            "x": 112,
            "y": 429,
        },
    ]
    execute_step(steps)
