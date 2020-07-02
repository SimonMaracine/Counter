import tkinter as tk
from typing import Callable


class SaveCount(tk.Frame):

    def __init__(self, top_level: tk.Toplevel, on_apply: Callable):
        super().__init__(top_level)
        self.top_level = top_level
        self.on_apply = on_apply
        self.pack(padx=10, pady=10, expand=True)

        self.top_level.title("Save")

        tk.Label(self, text="Name").grid(row=0, column=0)
        self.ent_name = tk.Entry(self)
        self.ent_name.grid(row=0, column=1, columnspan=2)
        tk.Button(self, text="Cancel", command=self.cancel).grid(row=1, column=1)
        tk.Button(self, text="Save", command=self.save_and_exit).grid(row=1, column=2)

    def save_and_exit(self):
        name = self.ent_name.get()
        if not name:
            messagebox.showerror("No Name", "The name is empty.", parent=self.top_level)
            return

        self.on_apply(name)
        self.top_level.destroy()

    def cancel(self):
        self.top_level.destroy()
