input_char = str(input())
order_num = int(input())

left_stack = [char for char in input_char]
right_stack = []

def processor(order_char, *args):
    if order_char == "L":
        try:
            right_stack.append(left_stack[-1])
            left_stack.pop(-1)
        except:
            pass
    elif order_char == "D":
        try:
            left_stack.append(right_stack[-1])
            right_stack.pop(-1)
        except:
            pass
    elif order_char == "B":
        try:
            left_stack.pop(-1)
        except:
            pass
    elif order_char == "P":
        left_stack.append(args[0])
    else:
        assert ValueError
        
for i in range(order_num):
    order_input = str(input()).split()

    if len(order_input) == 2:
        order_char_, letter_ = order_input
        processor(order_char_, letter_)
    else:
        order_char_ = order_input[0]
        processor(order_char_)
        
''.join(left_stack+right_stack[::-1])
