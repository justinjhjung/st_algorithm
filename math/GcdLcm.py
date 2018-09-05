A, B = (int(x) for x in input().split())

class GcdLcm:
    def __init__(self, A, B):
        self.a = A
        self.b = B

    def GCD(self):
        large = max(self.a, self.b)
        small = min(self.a, self.b)

        while True:
            mod = large%small
            if mod != 0:
                large = max(mod, small)
                small = min(mod, small)
            else:
                if small != 0:
                    gcd = small
                else:
                    gcd = large
                return gcd
                break
    
    def LCM(self):
        gcd = self.GCD()
        lcm = self.a * self.b / gcd
        return lcm
    
    def __str__(self):
        gcd = self.GCD()
        lcm = self.LCM()
        return '{}\n{}'.format(str(gcd),str(int(lcm)))

gcd_lcm = GcdLcm(A,B)
print(gcd_lcm)
