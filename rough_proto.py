import pyautogui, sys
import keyboard

# pyautogui.size()
# pyautogui.position()
# pyautogui.dragTo(100, 200, button='left')
# pyautogui.moveTo(100, 200)
# pyautogui.moveTo(100, 100, 2, pyautogui.easeInQuad)
# pyautogui.click()
# pyautogui.press('f1')

import tkinter as tk


def lift_window(window):
    window.attributes("-topmost", True)
    window.update_idletasks()  # get window on top
    window.attributes("-topmost", False)  # prevent permanent focus
    window.focus_force()  # focus to the window

""" 
def ttk_message_old(text, x, y):
    root = tk.Tk()
    root.overrideredirect(True)
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    label=ttk.Label(frm, text=text).grid(column=0, row=0)
    label.config(bg= "gray51", fg= "white")
    root.geometry("%dx%d+%d+%d" % (300, 40, x, y))
    root.wm_attributes('-transparentcolor','#add123')
    lift_window(root)
    root.mainloop()
"""

def ttk_message(text, x, y):
    
    def close_window(event):
        root.destroy()

    root = tk.Tk()
    # set the window as a grab window
    root.grab_set_global()
    root.overrideredirect(True)
    label = tk.Label(root, text=text, font=("Helvetica", 12))
    label.config(bg="#66cee3")
    label.pack(fill=tk.BOTH, expand=True)
    root.geometry("%dx%d+%d+%d" % (400, 40, x, y))
    root.wm_attributes('-transparentcolor','#add123')
    root.after(4500,lambda:root.destroy())
    lift_window(root)
    
    # bind the Enter key to the close_window function
    root.bind('<Return>', close_window)
    
    
    root.mainloop()
    


def execute_step(list_steps):
    secs_between_keys = 0.3
    for step in list_steps:
        if step["type"] == "move_mouse":
            pyautogui.moveTo(step["x"], step["y"], step["speed"], step["Easing"])
        elif step["type"] == "click":
            pyautogui.click(button=step["button"])
        elif step["type"] == "enter":
            pyautogui.typewrite(step["text"], interval=secs_between_keys)
        elif step["type"] == "message_user":
            ttk_message(step["message"], step["x"], step["y"])


if __name__ == "__main__":
    mode = "run"
    #mode = "probe"
    
    if mode == "run":
        # steps = [{"type":"move_mouse", "x":300,"y":300},{"type":"click", "button":"left"}]
        # SUM FUNCTION
        steps = [
            {"type": "move_mouse", "x": 248, "y": 464,"speed": 2, "Easing": pyautogui.easeOutQuad},
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
                "x": 248,
                "y": 464+10,
            },
        ]

        steps1 = [
            {"type": "move_mouse", "x": 251, "y": 876,"speed": 2, "Easing": pyautogui.easeOutQuad},
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
                "x": 311,
                "y": 891,
            },
            {"type": "move_mouse", "x": 311, "y": 891,"speed": 2, "Easing": pyautogui.easeOutQuad},
            {
                "type": "message_user",
                "message": "Now drag to other columns if needed",
                "x": 311,
                "y": 895,
            },
        ]
        y_rnk = 903
        x_rnk = 251
        steps2 = [
            {"type": "move_mouse", "x": 251, "y": 903,"speed": 2, "Easing": pyautogui.easeOutQuad},
            {"type": "click", "button": "left"},
            {
                "type": "enter",
                "text": [
                    "=",
                    "R",
                    "A",
                    "N",
                    "K",
                    "(",
                ],
            },
            {
                "type": "message_user",
                "message": "Select the fields you wish to rank",
                "x": 251,
                "y": y_rnk+10,
            },
            {
                "type": "message_user",
                "message": "then type a comma (,)",
                "x": 251,
                "y": y_rnk+10,
            },
            {
                "type": "message_user",
                "message": "now select the fields you want to rank against and hit enter",
                "x": 251,
                "y": y_rnk+10,
            },
                        {
                "type": "message_user",
                "message": "remember to add $$ if you want to fix this field",
                "x": 251,
                "y": y_rnk+10,
            }
        ]
        steps3 = [
            {
                "type": "message_user",
                "message": "Select the fields you wish to format",
                "x": 994,
                "y": 724,
            },
            {"type": "move_mouse", "x": 328, "y": 168,"speed": 2, "Easing": pyautogui.easeOutQuad},
            {"type": "click", "button": "left"},
            {"type": "move_mouse", "x": 328, "y": 596,"speed": 2, "Easing": pyautogui.easeOutQuad},
            {"type": "click", "button": "left"},
            {"type": "move_mouse", "x": 1720, "y": 300,"speed": 2, "Easing": pyautogui.easeOutQuad},
            {"type": "click", "button": "left"},
            {"type": "move_mouse", "x": 1615, "y": 567,"speed": 2, "Easing": pyautogui.easeOutQuad},
            {"type": "click", "button": "left"},
            {"type": "move_mouse", "x": 1708, "y": 763,"speed": 2, "Easing": pyautogui.easeOutQuad},
            {"type": "click", "button": "left"},
            {"type": "move_mouse", "x": 1742, "y": 987,"speed": 2, "Easing": pyautogui.easeOutQuad},
            {"type": "click", "button": "left"},
            
        ]

        steps4 = [
            {"type": "move_mouse", "x": 89, "y": 170,"speed": 2, "Easing": pyautogui.easeOutQuad},
            {"type": "click", "button": "left"},
            {"type": "move_mouse", "x": 100, "y": 490,"speed": 2, "Easing": pyautogui.easeOutQuad},
            {"type": "move_mouse", "x": 621, "y": 487,"speed": 2, "Easing": pyautogui.easeOutQuad},
            {"type": "move_mouse", "x": 548, "y": 561,"speed": 2, "Easing": pyautogui.easeOutQuad},
        ]
        steps5 = [
            {"type": "move_mouse", "x": 1239, "y": 216,"speed": 2, "Easing": pyautogui.easeOutQuad}
        ]

        execute_step(steps1)
    elif mode == "probe":
        print(pyautogui.position())
