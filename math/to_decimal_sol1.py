a, b = input().split()
a = str(a)
b = int(b)

def to_decimals(a, b):
    system_numberlist = [str(i) for i in range(10)] + [chr(i+55) for i in range(10,36)]
    target_numberlist = system_numberlist[:b]
    tobe_converted = [target_numberlist.index(chr_) for chr_ in a]
    length = len(tobe_converted)
    
    target = 0
    for idx, i in enumerate(tobe_converted[::-1]):
        target += i*b**idx
    
    return target

print(to_decimals(a, b))
