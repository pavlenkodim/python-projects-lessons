from tkinter import *
from tkinter import messagebox as mb
from contact import Contact

class ContactForm(LabelFrame):
    fields = ("First Name", "Last Name", "Email", "Phone Number")
    def __init__(self, master, **kwargs):
        super().__init__(master, text="Contact", padx=10, pady=10, **kwargs)
        self.frame = Frame(self)
        self.entries = list(map(self.create_field, enumerate(self.fields)))
        self.frame.pack()
        self.btn = Button(self, text="Add contact", pady=5, padx=5)
        self.btn.pack(side=LEFT, fill=BOTH, expand=1)

    def create_field(self, field):
        position, text = field

        label = Label(self.frame, text=text)
        entry = Entry(self.frame, width=25)

        label.grid(row=position, column=0, pady=5)
        entry.grid(row=position, column=1, pady=5)

        return entry

    def load_details(self, contact):
        values = (contact.first_name, contact.last_name, contact.email, contact.phone_number)

        for entry, value in zip(self.entries, values):
            entry.delete(0, END)
            entry.insert(0, value)

    def get_details(self):
        values = [e.get() for e in self.entries]

        try:
            return Contact(*values)
        except ValueError as e:
            mb.showerror("Error", e)

    def clear(self):
        for entry in self.entries:
            entry.delete(0, END)

    def bind_add(self, callback):
        self.btn["command"] = callback
