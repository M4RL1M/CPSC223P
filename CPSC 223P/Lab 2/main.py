# Name: Matthew Lim
# Date: 02/06/25
# Module Purpose: Menu of functions that allow user to print, add, modify and delete from a list of contacts

import contacts

def menu():
    list = []
    exitstatus = 0
    while exitstatus == 0:
        print("=============================")
        print("TUFFY TITAN CONTACT MAIN MENU")
        print("=============================")
        print("1. Print Contacts")
        print("2. Add Contact")
        print("3. Modify Contact")
        print("4. Delete Contact")
        print("5. Exit")
        option = int(input("Enter Menu Option: "))
        if option == 1:
            contacts.print_list(list)
        elif option == 2:
            contacts.add_contact(list)
        elif option == 3:
            contacts.modify_contact(list)
        elif option == 4:
            contacts.delete_contact(list)
        else:
            exitstatus = 1

if __name__ == '__main__':
    menu()