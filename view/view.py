import tkinter as tk
from tkinter import messagebox

class Application(tk.Frame):
    def __init__(self, master=None, controller=None):
        super().__init__(master)
        self.master = master
        self.controller = controller
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.languages_abr_label = tk.Label(self, text="languages_abr")
        self.languages_abr_label.pack()
        self.languages_abr_entry = tk.Entry(self)
        self.languages_abr_entry.pack()

        self.languages_label = tk.Label(self, text="languages")
        self.languages_label.pack()
        self.languages_entry = tk.Entry(self)
        self.languages_entry.pack()

        self.create_button = tk.Button(self, text="Create", command=self.controller.create)
        self.create_button.pack()

        self.read_button = tk.Button(self, text="Read", command=self.controller.read)
        self.read_button.pack()

        self.update_button = tk.Button(self, text="Update", command=self.controller.update)
        self.update_button.pack()

        self.delete_button = tk.Button(self, text="Delete", command=self.controller.delete)
        self.delete_button.pack()

        self.result_label = tk.Label(self, text="", wraplength=300)
        self.result_label.pack()

    def show_message(self, message):
        messagebox.showinfo("Info", message)

    def display_data(self, data):
        self.result_label['text'] = '\n'.join([str(row) for row in data])
