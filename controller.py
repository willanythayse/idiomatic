from model.model import Database
from view.view import Application
import tkinter as tk

class Controller:
    def __init__(self, root):
        self.db = Database('IDIOMA', 'welcome1', 'localhost/XE')
        self.app = Application(master=root, controller=self)
        self.app.mainloop()

    def create(self):
        languages_abr = self.app.languages_abr_entry.get()
        languages = self.app.languages_entry.get()
        if languages_abr and languages:
            self.db.create(languages_abr, languages)
            self.app.show_message("Record created successfully!")
        else:
            self.app.show_message("Please enter both languages_abr and languages.")

    def read(self):
        data = self.db.read()
        self.app.display_data(data)

    def update(self):
        id_languages = self.app.id_entry.get()
        languages_abr = self.app.languages_abr_entry.get()
        languages = self.app.languages_entry.get()
        if id_languages and languages_abr and languages:
            self.db.update(id_languages, languages_abr, languages)
            self.app.show_message("Record updated successfully!")
        else:
            self.app.show_message("Please enter id, languages_abr, and languages.")

    def delete(self):
        id_languages = self.app.id_entry.get()
        if id_languages:
            self.db.delete(id_languages)
            self.app.show_message("Record deleted successfully!")
        else:
            self.app.show_message("Please enter id.")

if __name__ == "__main__":
    root = tk.Tk()
    app = Controller(root)
