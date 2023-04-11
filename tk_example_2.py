import tkinter as tk

# create the main window
root = tk.Tk()
root.title("Purple Message")

# create a label with the message
message_label = tk.Label(root, text="Hello, world!", font=("Helvetica", 24))

# set the background color to purple
message_label.config(bg="purple")

# pack the label into the window
message_label.pack(fill=tk.BOTH, expand=True)

# start the event loop
root.mainloop()