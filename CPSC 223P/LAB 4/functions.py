# Name: Matthew Lim
# Date: 02/20/25
# Description: This file demonstrates operations on data structures including tuples, sequences, sets, and dictionaries
#              using looping techniques, conditional and boolean statements.

# 1. Tuples and Sequences
# Function name: create_tuple
# Description: Pack the provided arguments into a tuple and return it.
# Arguments: *args : A variable number of arguments to be packed into a tuple.
# Return: A tuple containing all the provided arguments (*args)
def create_tuple(*args):
    return tuple(args)

# Function name: unpack_tuple
# Description: Unpack the tuple into individual variables and return them as a list. 
#              (Assume the tuple has a fixed, known number of elements.)
# Arguments: A tuple to be unpacked (t).
# Return: A list of the unpacked elements.
def unpack_tuple(t):
    return list(t)

# Function name: tuple_details
# Description: Return a dictionary containing details about the tuple such
#              as its length, the first element, and the last element.
# Handle the case of an empty tuple appropriately.
# Arguments: A tuple whose details are to be extracted (t).
# Return: A dictionary with keys such as 'length', 'first', and 'last'.
def tuple_details(t):
    if len(tuple(t)) == 0:
        dictionary = {'length': 0, 'first': None, 'last': None}
    else:
        dictionary = {'length': len(t), 'first': t[0], 'last': t[-1]}
    return dictionary


# 2. Set Operations 
# Function name: create_set
# Description: Create a set from the given iterable.
# Arguments: An iterable from which to create a set (iterable).
# Return: A set containing unique elements from the iterable.
def create_set(iterable):
    return set(iterable)

# Function name: set_operations
# Description: Given two sets, perform various set operations and return the results in a dictionary.
# Arguments: s1 (the first set) and s2 (the second set)
# Return: A dictionary with the following keys:
#     - 'union' : The union of s1 and s2.
#     - 'intersection' : The intersection of s1 and s2.
#     - 'difference' : The difference (elements in s1 but not in s2).
#     - 'symmetric_difference': The symmetric difference of s1 and s2.
def set_operations(s1, s2):
    dictionary = {
        'union': s1 | s2,
        'intersection': s1 & s2,
        'difference': s1 - s2,
        'symmetric_difference': s1 ^ s2
    }
    return dictionary

# Function name: unique_sorted
# Description: Returns a sorted list of unique elements from the provided iterable.
# Arguments: An iterable that may contain duplicate elements (iterable).
# Return: A sorted list of the unique elements.
def unique_sorted(iterable):
    return sorted(set(iterable))

# 3. Dictionary Operations
# Function name: create_dictionary
# Description: Create a dictionary from a list of key-value pair tuples.
# Arguments: A list of tuples, where each tuple is a key-value pair (pairs)
# Return: A dictionary constructed from the provided pairs.
def create_dictionary(pairs):
    return dict(pairs)

# Function name: update_dictionary
# Description: Update the dictionary with the provided key-value pair. If the key exists, its value is overwritten.
# Arguments: The dictionary to update (d), the key to update or add (key), and the value associated with the key (value).
# Return: The updated dictionary.
def update_dictionary(d, key, value):
    d[key] = value
    return d

# Function name: delete_key
# Description: Remove the specified key from the dictionary. If the key does not exist, 
#              return an error message or raise an exception.
# Arguments: The dictionary from which to delete a key (d) and the key to be removed (key)
# Return: The dictionary after removal of the key, or an error message if the key is not found
def delete_key(d, key):
    if key in d:
        del d[key]
        return d
    else:
        raise KeyError("Key not found.")

# Function name: dict_comprehension_example
# Description: Create a dictionary using comprehension that maps each element of the iterable 
#              to its square (if numeric) or its length (if a string).
# Arguments: An iterable containing numbers and/or strings (iterable).
# Return: A dictionary with each element as a key and its corresponding computed value.
def dict_comprehension_example(iterable):
    dictionary = {}
    for x in iterable:
        if isinstance(x, (int, float)):
            dictionary[x] = x ** 2
        else:
            dictionary[x] = len(x)
    return dictionary

# Function name: merge_dictionaries
# Description: Merge a list of dictionaries into a single dictionary. If the same key
#              appears in multiple dictionaries, combine their values into a list.
# Arguments: A list of dictionaries to merge (dicts)
# Return: A dictionary where each key maps to a list of all values associated with that key from the input dictionaries.
def merge_dictionaries(dicts):
    merged = {}
    for dict in dicts:
        for k, v in dict.items():
            merged.setdefault(k, []).append(v)
    return merged

# 4. Looping Techniques
# Function name: iterate_dictionary
# Description: Iterate over the dictionary and return a list of formatted strings showing key-value pairs.
# Arguments: The dictionary to iterate over (d).
# Return: A list of strings in the format "key: value".
def iterate_dictionary(d):
    list = []
    for k, v in d.items():
        list.append(f"{k}: {v}")
    return list

# Function name: enumerate_list
# Description: Enumerate over the list and return a list of tuples containing the index and the corresponding element.
# Arguments: The list to enumerate. (lst)
# Return: A list of tuples where each tuple is (index, element).
def enumerate_list(lst):
    return list(enumerate(lst))

# Function name: zip_lists
# Description: Pair elements from two lists using the zip function and return the resulting list of tuples.
# Arguments: The first list (lst1) and the second list (lst2)
# Return: A list of tuples, each containing one element from lst1 and the corresponding element from lst2.
def zip_lists(lst1, lst2):
    return list(zip(lst1, lst2))

# Function name: reverse_and_sort
# Description: Return both a reversed version of the list and a sorted version of the list.
# Arguments: The list to be processed (lst).
# Return: A tuple with two lists: The first is the reversed list and the second is the sorted list.
def reverse_and_sort(lst):
    return lst[::-1], sorted(lst)

# 5. Conditions and Sequence Comparisons
# Function name: check_membership
# Description: Check if a value exists within a sequence.
# Arguments: The sequence to search (sequence) and the value to check for (value)
# Return: True if the value is found, otherwise False.
def check_membership(sequence, value):
    return value in sequence

# Function name: chained_comparison
# Description: Evaluate the chained comparison a < b == c and return the result.
# Arguments: The first value (a), the second value (b), and the third value (c).
# Return: True if the comparison holds; otherwise, False.
def chained_comparison(a, b, c):
    return a < b == c

# Function name: boolean_evaluation
# Description: Evaluate the Boolean expression (a and not b) or c using short-circuit evaluation.
# Arguments: Three booleans or value evaluated in a Boolean context (a, b, c)
# Return: The result of the Boolean expression.
def boolean_evaluation(a, b, c):
    return (a and not b) or c

# Function name: compare_sequences
# Description: Compare two sequences lexicographically.
# Arguments: The first sequence (seq1) and the second sequence (seq2).
# Return: -1 if seq1 is less than seq2,  0 if they are equal, or 1 if seq1 is greater than seq2.
def compare_sequences(seq1, seq2):
    # if seq1 < seq2:
    #     return -1
    # if seq1 > seq2:
    #     return 1
    # else:
    #     return 0
    return (seq1 > seq2) - (seq1 < seq2)

# Function name: is_strictly_increasing
# Description: Check if a sequence of numbers is strictly increasing (i.e., each element is less than the next one).
# Arguments: A list or tuple of numbers (sequence)
# Return: True if the sequence is strictly increasing, otherwise False.
def is_strictly_increasing(sequence):
    return all(x < y for x, y in zip(sequence, sequence[1:]))