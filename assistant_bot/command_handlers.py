"""
This module contains functions 
that handle the different commands that the assistant bot can receive.
"""
def add_contact(args, contacts):
    """
    Add a contact to the contacts dictionary.

    Args:
    args (list): A list containing the name and phone number of the contact.
    contacts (dict): A dictionary containing the contacts.

    Returns:
    str: A message indicating whether the contact was added successfully or not.
    """
    if len(args) != 2:
        return "Error: add command requires a name and a phone number."
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    """
    Change the phone number of an existing contact.

    Args:
    args (list): A list containing the name and new phone number of the contact.
    contacts (dict): A dictionary containing the contacts.

    Returns:
    str: A message indicating whether the contact was updated successfully or not.
    """
    if len(args) != 2:
        return "Error: change command requires a name and a new phone number."
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    return "Error: Contact not found."

def show_phone(args, contacts):
    """
    Show the phone number of a contact.

    Args:
    args (list): A list containing the name of the contact.
    contacts (dict): A dictionary containing the contacts.

    Returns:
    str: The phone number of the contact or an error message if the contact is not found.
    """
    if len(args) != 1:
        return "Error: phone command requires a name."
    name = args[0]
    if name in contacts:
        return f"{name}: {contacts[name]}"
    return "Error: Contact not found."

def show_all(contacts):
    """
    Show all contacts in the contacts dictionary.

    Args:
    contacts (dict): A dictionary containing the contacts.

    Returns:
    str: A formatted string containing all the contacts or a message if no contacts are found.
    """
    if not contacts:
        return "No contacts found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
