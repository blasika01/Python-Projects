

# !!!! There is an intentional bug with the "text_entry" function that is fixed in the tkinter practice with classes !!!!




import tkinter as tk

#changes the looks of the components depending on the os.
from tkinter import ttk

# Creating the main window and giving it a title.
root = tk.Tk()
root.title("Exercise")

# Configuring different columns or rows of the root window so the parts resize to the size of the window.

# Weight determines how much space a certain part should take up in relations to the other one.
# In the example the first and second column have a sum weight of 4, 3 for the second and 1 for the first.
# So the first will take up aprox. 25% of the entire window while the other 75%. (Doesn't take the base size into consideration.)
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

# Command for the entry element. Saves the text in entry to a text variable.
# If there is text it inserts it at the end of the list, then deletes the text in entry. (From the character at index 0 till the end)
def text_entry(event=None):
    text = entry.get()
    if text:
        entry_lst.insert(tk.END, text)
        entry.delete(0, tk.END)

# Creating a frame in a grid at row=0 and column=0. Good idea if we would reuse the content.
# Added padding to the element. Also sticky which determines which sides it should stick to (North, South, East, West)
frame = ttk.Frame(root)
frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

frame.columnconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)

# Creating an entry element where text can be inserted.
entry = ttk.Entry(frame)
entry.grid(row=0, column=0, sticky="ew")

# Binding text_entry function to a key (Enter) in the entry element. I can insert text to the list by pressing Enter.
entry.bind("<Return>", text_entry)

# Creating a button, with the text_entry command. By pressing it i can add the text in entry to the list.
entry_btn = ttk.Button(frame, text="Add", command=text_entry)
entry_btn.grid(row=0, column=1)

# Creating box for the list of items added by text_entry.
entry_lst = tk.Listbox(frame)
entry_lst.grid(row=1, column=0, columnspan=2, sticky="nsew")

# Creating another frame based on the first one in a different column.
frame2 = tk.Frame(root)
frame2.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

frame2.columnconfigure(0, weight=1)
frame2.rowconfigure(1, weight=1)

entry = tk.Entry(frame2)
entry.grid(row=0, column=0, sticky="ew")

entry.bind("<Return>", text_entry)

entry_btn = tk.Button(frame2, text="Add", command=text_entry)
entry_btn.grid(row=0, column=1)

entry_lst = tk.Listbox(frame2)
entry_lst.grid(row=1, column=0, columnspan=2, sticky="nsew")

# def on_click():
#     print("Hello World")
#
# lbl = tk.Label(root, text="Label 1")
# lbl.grid(row=0, column=0)
#
# btn = tk.Button(root, text="Button 1", command=on_click)
# btn.grid(row=0, column=1)


# Keeps the application running, doesn't close immediately.
root.mainloop()