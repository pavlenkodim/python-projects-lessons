from tkinter import *

class ContactList(Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master)
        self.lb = Listbox(self, **kwargs)
        scroll = Scrollbar(self, command=self.lb.yview)

        self.lb.config(yscrollcommand=scroll.set)
        scroll.pack(side=RIGHT, fill=Y)
        self.lb.pack(side=LEFT, fill=BOTH, expand=1)


    def insert(self, contact, index=END):
        text = "{}, {}, {}, {}".format(contact.last_name, contact.first_name, contact.email, contact.phone)
        self.lb.insert(index, text)

    def delete(self, index):
        self.lb.delete(index, index)

    def update(self, contacts, index):
        self.delete(index)
        self.insert(contacts, index)

    def bind_double_click(self, callback):
        def handler(_):
            print('double click')
            selection = self.lb.curselection()
            if selection:
                callback(selection[0])
        self.lb.bind("<Double-Button-1>", handler)