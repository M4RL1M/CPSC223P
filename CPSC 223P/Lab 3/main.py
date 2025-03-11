# Name: Matthew Lim
# Date: 02/13/25
# Module Purpose: Menu of functions that allow user to print, add, modify and delete from a list, stack or queue

import list_operations

def menu():
    list = []
    stack = []
    queue = []
    exitstatus = 0
    while exitstatus == 0:
        print("=============================")
        print("          Main Menu          ")
        print("=============================")
        print("1. List Operations")
        print("2. Stack Operations")
        print("3. Queue Operations")
        print("4. Exit")
        menuoption = int(input("Enter Menu Option: "))
        # List Operations
        while menuoption == 1:
            print("=============================")
            print("List Operations:")
            print("1. Append Item")
            print("2. Insert Item")
            print("3. Remove Item")
            print("4. Pop Item")
            print("5. Clear List")
            print("6. Sort List")
            print("7. Reverse List")
            print("8. Find Index of Item")
            print("9. Count Item")
            print("10. Slice List")
            print("11. Exit List Operations")
            print("=============================")
            option = int(input("Enter Menu Option: "))
            if option == 1:
                item = input("Enter the Item to be appended: ")
                list_operations.append_item(list, item)
                print(list)
            elif option == 2:
                item = input("Enter the Item to be inserted: ")
                index = int(input("Enter the Index: "))
                list_operations.insert_item(list, index, item)
                print(list)
            elif option == 3:
                item = input("Enter the Item to be removed: ")
                list_operations.remove_item(list, item)
                print(list)
            elif option == 4:
                # item = input("Enter the Item to be removed: ")
                list_operations.pop_item(list, index=-1)
                print(list)
            elif option == 5:
                list_operations.clear_list(list)
                print(list)
            elif option == 6:
                list_operations.sort_list(list)
                print(list)
            elif option == 7:
                list_operations.reverse_list(list)
                print(list)
            elif option == 8:
                item = input("Enter the Item to be found: ")
                index = list_operations.index_of_item(list, item)
                print("Index of Item: ", index)
            elif option == 9:
                item = input("Enter the Item to be counted: ")
                count = list_operations.count_item(list, item)
                print("Count of Item: ", count)
            elif option == 10:
                start = int(input("Enter the Start Index of the slice: "))
                end = int(input("Enter the End Index of the slice: "))
                # incrementing "end" is necessary for value at end index to actually be included
                end = end + 1
                slice = []
                slice = list_operations.slice_list(list, start, end)
                print(slice)
            else:
                menuoption = 0
        # Stack Operations
        while menuoption == 2:
            print("=============================")
            print("Stack Operations:")
            print("1. Push Item")
            print("2. Pop Top")
            print("3. Exit Stack Operations")
            print("=============================")
            option = int(input("Enter Action Option: "))
            if option == 1:
                item = input("Enter the Item to be pushed to the top of stack: ")
                stack.append(item)
                print(stack)
            elif option == 2:
                stack.pop()
                print(stack)
            else:
                menuoption = 0
        # Queue Operations
        while menuoption == 3:
            print("=============================")
            print("Queue Operations:")
            print("1. Queue Item")
            print("2. Deque")
            print("3. Exit Queue Operations")
            print("=============================")
            option = int(input("Enter Action Option: "))
            if option == 1:
                item = input("Enter an Item to queue: ")
                queue.append(item)
                print(queue)
            elif option == 2:
                from collections import deque
                queue = deque(queue)
                queue.popleft()
                print(queue)
            else:
                menuoption = 0
        # Exit Condition
        if menuoption == 4:
            exitstatus = 1
        

if __name__ == '__main__':
    menu()