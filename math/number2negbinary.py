input_ = int(input())

def number2negbinary(num):
    if num == 0:
        return 0
    
    convert_list = []
    while num!= 0:
        mod = abs(num)%2
        convert_list.append(mod)
        if mod != 0:
            num //= -2
            num += 1
        else:
            num //= -2
        
    return ''.join([str(i) for i in convert_list][::-1])
    
print(number2negbinary(input_))
