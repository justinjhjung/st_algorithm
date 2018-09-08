a, b = (int(x) for x in input().split())

def system_transformer(a, b):
    system_numberlist = [i for i in range(10)] + [chr(i+55) for i in range(10,36)]
    target_system = system_numberlist[:b]
    res = []
    while a > 0:
        number = a%b
        converted = target_system[number]
        res.append(str(converted))
        a = a//b
        
    return ''.join(res[::-1])

print(system_transformer(a, b))
