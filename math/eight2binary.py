input_ = str(input())

def number2binary(num):
    convert_list = []
    if num == 0:
        return '000'
    while num > 0:
        mod = num % 2
        num //= 2
        convert_list.append(mod)
    
    convert_list.extend([0,0])
    convert_list = [str(x) for x in convert_list]
    
    return ''.join(convert_list[:3][::-1])

def eight2binary(input_):
    res = []
    
    for i in input_:
        i = int(i)
        res.append(number2binary(i))
        
    res[0] = str(int(res[0]))
    return ''.join(res)
    
print(eight2binary(input_))
