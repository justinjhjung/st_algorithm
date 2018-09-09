input_ = str(input())

def binary_calc(str_input):
    sum = 0
    for idx, i in enumerate(str_input):
        i = int(i)
        sum += i*2**idx
    return str(sum)

def binary2eight(input_):
    reversed_ = input_[::-1]
    length = len(reversed_)
    binary_list = [reversed_[i:i+3] for i in range(0,length,3)]
    
    converted = []
    for i in binary_list:
        converted.append(binary_calc(i))
    return ''.join(converted[::-1])
    
print(binary2eight(input_))
