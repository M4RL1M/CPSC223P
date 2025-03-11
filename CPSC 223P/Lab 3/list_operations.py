# Name: Matthew Lim
# Date: 02/13/25
# Module Purpose: Functions that allow user to print, add, modify and delete from a stack or queue

def append_item(list, item):
    list.append(item)
    return list

def insert_item(list, index, item):
    list.insert(index, item)
    return list

def remove_item(list, item):
    if item in list:
        list.remove(item)
    return list

def pop_item(list, index=-1):
    list.pop(index)
    return list

def clear_list(list):
    list.clear()
    return list

def sort_list(list):
    list.sort()
    return list

def reverse_list(list):
    list.reverse()
    return list

def index_of_item(list, item):
    if item in list:
        index = list.index(item)
    else:
        index = None
    return index

def count_item(list, item):
    count = list.count(item)
    return count

def slice_list(list, start, end):
    sliced = []
    sliced = list[start: end]
    return sliced