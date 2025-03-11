# Name: Matthew Lim
# Date: 02/20/25
# Description: This file imports functions from functions.py and tests them.

from functions import *

def test_functions():
    # Testing create_tuple
    print("create_tuple(1, 2, 3)")
    print(create_tuple(1, 2, 3))  
    # Expected: (1, 2, 3)
    
    # Testing unpack_tuple
    print("unpack_tuple((4, 5, 6))")
    print(unpack_tuple((4, 5, 6)))  
    # Expected: [4, 5, 6]
    
    # Testing tuple_details
    print("tuple_details((7, 8, 9))") 
    print(tuple_details((7, 8, 9)))  
    # Expected: {'length': 3, 'first': 7, 'last': 9}
    
    # Testing create_set
    print("create_set([1, 2, 2, 3])")
    print(create_set([1, 2, 2, 3]))
    # Expected: {1, 2, 3}
    
    # Testing set_operations
    print("set_operations({1, 2}, {2, 3})")
    print(set_operations({1, 2}, {2, 3}))
    
    # Testing unique_sorted
    print("unique_sorted([4, 2, 2, 1])")
    print(unique_sorted([4, 2, 2, 1]))  
    # Expected: [1, 2, 4]
    
    # Testing create_dictionary
    print("create_dictionary([('a', 1), ('b', 2)])")
    print(create_dictionary([('a', 1), ('b', 2)]))
    # Expected: {'a': 1, 'b': 2}
    
    # Testing update_dictionary
    d = {'x': 10}
    print("d: ", d)
    print("update_dictionary(d, 'y', 20)")
    print(update_dictionary(d, 'y', 20))  
    # Expected: {'x': 10, 'y': 20}
    
    # Testing delete_key
    print("delete_key(d, 'x')")
    print(delete_key(d, 'x'))  
    # Expected: {'y': 20}
    
    # Testing dict_comprehension_example
    print("dict_comprehension_example([2, 'hello'])")
    print(dict_comprehension_example([2, 'hello']))
    # Expected: {2: 4, 'hello': 5}
    
    # Testing merge_dictionaries
    print("merge_dictionaries([{'a': 1}, {'a': 2, 'b': 3}])") 
    print(merge_dictionaries([{'a': 1}, {'a': 2, 'b': 3}]))
    # Expected: {'a': [1, 2], 'b': [3]}

    # Testing iterate_dictionary
    print("iterate_dictionary({'a': 1, 'b': 2})") 
    print(iterate_dictionary({'a': 1, 'b': 2}))
    # Expected: ['a: 1', 'b: 2']

    # Testing enumerate_list
    print("enumerate_list(['x', 'y', 'z'])")
    print(enumerate_list(['x', 'y', 'z']))
    # Expected: [(0, 'x'), (1, 'y'), (2, 'z')]

    # Testing zip_lists
    print("zip_lists([1, 2], ['a', 'b'])")
    print(zip_lists([1, 2], ['a', 'b']))
    # Expected: [(1, 'a'), (2, 'b')]
    
    # Testing reverse_and_sort
    print("reverse_and_sort([3, 1, 2])")
    print(reverse_and_sort([3, 1, 2]))
    # Expected: [2, 1, 3], [1, 2, 3]
    
    # Testing check_membership
    print("check_membership([1, 2, 3], 2)")
    print(check_membership([1, 2, 3], 2))
    # Expected: True
    
    # Testing chained_comparison
    print("chained_comparison(1, 2, 2)")
    print(chained_comparison(1, 2, 2))  
    # Expected: True
    
    # Testing boolean_evaluation
    print("boolean_evaluation(True, False, False)")
    print(boolean_evaluation(True, False, False))
    # Expected: True
    
    # Testing compare_sequences
    print("compare_sequences([1, 2], [1, 3])")
    print(compare_sequences([1, 2], [1, 3]))  
    # Expected: -1
    

    # Testing is_strictly_increasing
    print("is_strictly_increasing([1, 2, 3])")
    print(is_strictly_increasing([1, 2, 3]))  
    # Expected: True
    print("is_strictly_increasing([3, 3, 4])")
    print(is_strictly_increasing([3, 3, 4]))  
    # Expected: False

if __name__ == "__main__":
    test_functions()
