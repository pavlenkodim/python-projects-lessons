import re

class Contact(object):

    email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
    phone_regex = re.compile(r"\([0-9]{3}\)\s[0-9]{7}")

    def __init__(self, first_name, last_name, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email