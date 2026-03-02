from tkinter import *

from form import ContactForm
from list import ContactList

root = Tk()
root.title("Contact List")
root.geometry("800x600")

contact_list = ContactList(root)
contact_list.pack(side=LEFT, fill=BOTH, expand=True)

contact_form = ContactForm(root)
contact_form.pack(side=RIGHT, fill=Y)

def add_contact():
    contact = contact_form.get_details()

    if contact:
        contact_list.insert(contact)
        contact_form.clear()

contact_form.bind_add(add_contact)

root.mainloop()