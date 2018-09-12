A, B = (int(x) for x in input().split())
pos_num = int(input())
numA = [int(x) for x in input().split()]

class BaseConversion:
    def __init__(self, A, B, numA):
        self.A = A
        self.B = B
        self.numA = numA
    
    def a2decimal(self):
        dec = 0
        for i in self.numA:
            dec *= self.A
            dec += i
        return dec
            
    def decimal2b(self):
        dec = self.a2decimal()
        systemnum_list = [i for i in range(9)] + [chr(i) for i in range(65,91)]
        target_system = systemnum_list[:self.B]
        
        convert_list = []
        while dec > 0:
            mod = dec % self.B
            dec //= self.B
            convert_list.append(mod)
        res = [str(x) for x in convert_list[::-1]]
        return res
        
    def __str__(self):
        res = self.decimal2b()
        return ' '.join(res)
        
convert = BaseConversion(A, B, numA)
print(convert)
