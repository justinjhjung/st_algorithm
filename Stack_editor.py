from sys import stdin
from collections import deque

input_char = str(stdin.readline().split())
order_num = int(stdin.readline().split())

left_stack = deque(input_char)
right_stack = deque([])

def processor(order_char, *args)
    if order_char == "L":
        if left_stack:
            right_stack.appendleft(left_stack.pop()])
    elif order_char == "D":
        if right_stack:
            left_stack.append(right_stack.popleft())
    elif order_char == "B":
        if left_stack:
            left_stack.pop()
    elif order_char == "P":
        left_stack.append(args[0])
        
for i in range(order_num):
    order_input = str(stdin.readline().strip()).split()

    if len(order_input) == 2:
        order_char_, letter_ = order_input
        processor(order_char_, letter_)
    else:
        order_char_ = order_input[0]
        processor(order_char_)

left_stack.extend(right_stack)
print(''.join(left_stack))
