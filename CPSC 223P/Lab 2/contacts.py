# Name: Matthew Lim
# Date: 02/06/25
# Module Purpose: Functions to allow user to print, add, modify and delete from a list of contacts

def print_list(contacts):
    print("======== Contacts =======")
    print("Index   First        Last")
    for index in range(len(contacts)):
        name = list(contacts[index])
        first = name[0]
        last = name[1]
        print(index, "     ", first, "     ", last)
        index = index + 1
    

def add_contact(contacts):
    name = []
    first = input("Enter the first name: ")
    last = input("Enter the last name: ")
    name.append(first)
    name.append(last)
    contacts.append(name)
    return contacts

def modify_contact(contacts):
    index = int(input("Enter the index of the value to be modified: "))
    if (index < 0) or (index >= len(contacts)):
        print("Invalid index: ", index)
        return contacts
    mod = input("Enter the new name: ")
    first, last = mod.split()
    name = []
    name.append(first)
    name.append(last)
    contacts[index] = name
    return contacts


def delete_contact(contacts):
    index = int(input("Enter the index of the value to be deleted: "))
    if (index < 0) or (index >= len(contacts)):
        print("Invalid index: ", index)
        return contacts
    contacts.pop(index)
    return contacts
