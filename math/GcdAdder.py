test_num = int(input())

class GcdAdder:
    def __init__(self, length, inputs):
        self.length = length
        self.inputs = inputs
    
    def gcd_adder(self):
        combination = self.pick_two()
        sum_ = 0
        for [a, b] in combination:
            sum_ += self.gcd(a,b)
        return sum_
            
    def gcd(self, a, b):
        small = min(a,b)
        large = max(a,b)
        while True:
            mod = large%small
            if mod != 0:
                large = max(mod, small)
                small = min(mod, small)
            else:
                return small
                break
 
    def pick_two(self):
        combination = []
        for i in range(self.length):
            for j in range(i+1,self.length):
                if (i != j) :
                    combination.append([self.inputs[i],self.inputs[j]])
        return combination
    
    def __str__(self):
        sum = self.gcd_adder()
        return str(sum)
    
for i in range(test_num):
    inputs = [int(x) for x in input().split()]
    gcdadder = GcdAdder(inputs[0], inputs[1:])
    print(gcdadder)
