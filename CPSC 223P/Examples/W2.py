# stack: Last in First out (LIFO)
# initialize stack
stack = []

# add elements
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)

# find element at top
print("removing top element top: ", stack.pop())
print(stack)

from collections import deque
queue = deque(["A", "B", "C"])

print(queue)

# add elements
queue.append("D")
print(queue)
