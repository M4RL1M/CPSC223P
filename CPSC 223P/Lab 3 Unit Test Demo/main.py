# main.py
import functions

def main():
    lst = []
    stack = []
    queue = []

    while True:
        print("\nMenu:")
        print("1. List Operations")
        print("2. Stack Operations")
        print("3. Queue Operations")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nList Operations:")
            print("a. Append")
            print("b. Insert")
            print("c. Remove")
            print("d. Pop")
            print("e. Clear")
            print("f. Sort")
            print("g. Reverse")
            print("h. Index")
            print("i. Count")
            print("j. Slice")
            print("k. Back to Main Menu")

            sub_choice = input("Choose an operation: ")

            if sub_choice == 'a':
                item = input("Enter item to append: ")
                functions.append_item(lst, item)
            elif sub_choice == 'b':
                index = int(input("Enter index: "))
                item = input("Enter item to insert: ")
                functions.insert_item(lst, index, item)
            elif sub_choice == 'c':
                item = input("Enter item to remove: ")
                functions.remove_item(lst, item)
            elif sub_choice == 'd':
                functions.pop_item(lst)
            elif sub_choice == 'e':
                functions.clear_list(lst)
            elif sub_choice == 'f':
                functions.sort_list(lst)
            elif sub_choice == 'g':
                functions.reverse_list(lst)
            elif sub_choice == 'h':
                item = input("Enter item to find index: ")
                functions.index_of_item(lst, item)
            elif sub_choice == 'i':
                item = input("Enter item to count: ")
                functions.count_item(lst, item)
            elif sub_choice == 'j':
                start = int(input("Enter start index: "))
                end = int(input("Enter end index: "))
                functions.slice_list(lst, start, end)
            elif sub_choice == 'k':
                continue
            else:
                print("Invalid choice.")

        elif choice == '2':
            print("\nStack Operations:")
            print("a. Push")
            print("b. Pop")
            print("c. Back to Main Menu")

            sub_choice = input("Choose an operation: ")

            if sub_choice == 'a':
                item = input("Enter item to push: ")
                functions.push_stack(stack, item)
            elif sub_choice == 'b':
                functions.pop_stack(stack)
            elif sub_choice == 'c':
                continue
            else:
                print("Invalid choice.")

        elif choice == '3':
            print("\nQueue Operations:")
            print("a. Enqueue")
            print("b. Dequeue")
            print("c. Back to Main Menu")

            sub_choice = input("Choose an operation: ")

            if sub_choice == 'a':
                item = input("Enter item to enqueue: ")
                functions.enqueue(queue, item)
            elif sub_choice == 'b':
                functions.dequeue(queue)
            elif sub_choice == 'c':
                continue
            else:
                print("Invalid choice.")

        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
