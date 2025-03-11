# functions.py

def append_item(lst, item):
    lst.append(item)
    print(f"Appended {item} to list: {lst}")

def insert_item(lst, index, item):
    lst.insert(index, item)
    print(f"Inserted {item} at index {index}: {lst}")

def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
        print(f"Removed {item} from list: {lst}")
    else:
        print(f"Item {item} not found in list.")

def pop_item(lst, index=-1):
    if lst:
        item = lst.pop(index)
        print(f"Popped item {item} from list: {lst}")
        return item
    print("List is empty.")
    return None

def clear_list(lst):
    lst.clear()
    print("Cleared the list.")

def sort_list(lst):
    lst.sort()
    print(f"Sorted list: {lst}")

def reverse_list(lst):
    lst.reverse()
    print(f"Reversed list: {lst}")

def index_of_item(lst, item):
    if item in lst:
        index = lst.index(item)
        print(f"Index of {item}: {index}")
        return index
    print(f"Item {item} not found in list.")
    return -1

def count_item(lst, item):
    count = lst.count(item)
    print(f"Count of {item}: {count}")
    return count

def slice_list(lst, start, end):
    sliced = lst[start:end]
    print(f"Sliced list from {start} to {end}: {sliced}")
    return sliced

# Stack operations
def push_stack(stack, item):
    stack.append(item)
    print(f"Pushed {item} onto stack: {stack}")

def pop_stack(stack):
    if stack:
        item = stack.pop()
        print(f"Popped {item} from stack: {stack}")
        return item
    print("Stack is empty.")
    return None

# Queue operations
def enqueue(queue, item):
    queue.append(item)
    print(f"Enqueued {item} to queue: {queue}")

def dequeue(queue):
    if queue:
        item = queue.pop(0)
        print(f"Dequeued {item} from queue: {queue}")
        return item
    print("Queue is empty.")
    return None
