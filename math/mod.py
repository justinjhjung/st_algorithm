A, B, C = (int(x) for x in input().split())

class Mode:
    def __init__(self, A,B,C):
        self.a = A
        self.b = B
        self.c = C
        
    def direct_add(self):
        res = ( self.a + self.b ) % self.c
        return res
    
    def indirect_add(self):
        res = ( self.a % self.c + self.b % self.c ) % self.c
        return res
    
    def direct_mul(self):
        res = ( self.a * self.b ) % self.c
        return res
    
    def indirect_mul(self):
        res = ( ( self.a % self.c ) * ( self.b % self.c ) ) % self.c
        return res
    
    def __str__(self):
        res1 = self.direct_add()
        res2 = self.indirect_add()
        res3 = self.direct_mul()
        res4 = self.indirect_mul()
        return '\n'.join([str(i) for i in [res1, res2, res3, res4]])
    
mode = Mode(A, B, C)
print(mode)
