import tkinter as tk
from tkinter import ttk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple App")

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        frame = InputForm(self)
        frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        frame2 = InputForm(self)
        frame2.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

class InputForm(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.entry = ttk.Entry(self)
        self.entry.grid(row=0, column=0, sticky="ew")

        self.entry.bind("<Return>", self.text_entry)

        self.entry_btn = ttk.Button(self, text="Add", command=self.text_entry)
        self.entry_btn.grid(row=0, column=1)

        self.entry_lst = tk.Listbox(self)
        self.entry_lst.grid(row=1, column=0, columnspan=2, sticky="nsew")

    def text_entry(self, event=None):
        text = self.entry.get()
        if text:
            self.entry_lst.insert(tk.END, text)
            self.entry.delete(0, tk.END)

if __name__ == "__main__":
    app = Application()
    app.mainloop()