input_ = int(input())

class Factorization:
    def __init__(self, input_):
        self.input_ = input_
        
    def factorize(self):
        res = []
        i = 2
        while self.input_ > 1:
            if self.input_ % i == 0:
                res.append(i)
                self.input_ //= i
                i = 2
            else:
                i += 1
        return res
    
    def __str__(self):
        res = self.factorize()
        return '\n'.join([str(x) for x in res])

factorize = Factorization(input_)
print(factorize)
