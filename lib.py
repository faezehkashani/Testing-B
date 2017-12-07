import re

def email_validation(entry):
    if "@" not in entry:
        return False

    if not re.match("[a-z0-9\_\-\.]+@[a-z0-9\_\-\.]+\.[a-z]+", entry):
        return False

    return True

def number_validation(entry):
    if not str(entry).isdigit():
        raise ValueError("Invalid entry")
    return True
