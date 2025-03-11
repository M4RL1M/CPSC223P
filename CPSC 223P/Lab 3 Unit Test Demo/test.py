# test.py
import unittest
import functions

class Testfunctions(unittest.TestCase):

    def setUp(self):
        """Initialize test cases."""
        self.lst = [1, 2, 3, 4, 5]
        self.stack = []
        self.queue = []

    # List operations tests
    def test_append_item(self):
        functions.append_item(self.lst, 6)
        self.assertIn(6, self.lst)

    def test_insert_item(self):
        functions.insert_item(self.lst, 2, 99)
        self.assertEqual(self.lst[2], 99)

    def test_remove_item(self):
        functions.remove_item(self.lst, 3)
        self.assertNotIn(3, self.lst)

    def test_pop_item(self):
        item = functions.pop_item(self.lst)
        self.assertEqual(item, 5)

    def test_clear_list(self):
        functions.clear_list(self.lst)
        self.assertEqual(self.lst, [])

    def test_sort_list(self):
        unsorted_list = [3, 1, 4, 2]
        functions.sort_list(unsorted_list)
        self.assertEqual(unsorted_list, [1, 2, 3, 4])

    def test_reverse_list(self):
        functions.reverse_list(self.lst)
        self.assertEqual(self.lst, [5, 4, 3, 2, 1])

    def test_index_of_item(self):
        index = functions.index_of_item(self.lst, 3)
        self.assertEqual(index, 2)

    def test_count_item(self):
        self.lst.append(2)
        count = functions.count_item(self.lst, 2)
        self.assertEqual(count, 2)

    def test_slice_list(self):
        sliced = functions.slice_list(self.lst, 1, 4)
        self.assertEqual(sliced, [2, 3, 4])

    # Stack operations tests
    def test_push_stack(self):
        functions.push_stack(self.stack, 10)
        self.assertEqual(self.stack[-1], 10)

    def test_pop_stack(self):
        functions.push_stack(self.stack, 20)
        item = functions.pop_stack(self.stack)
        self.assertEqual(item, 20)

    # Queue operations tests
    def test_enqueue(self):
        functions.enqueue(self.queue, 15)
        self.assertEqual(self.queue[0], 15)

    def test_dequeue(self):
        functions.enqueue(self.queue, 30)
        item = functions.dequeue(self.queue)
        self.assertEqual(item, 30)

if __name__ == '__main__':
    unittest.main()
