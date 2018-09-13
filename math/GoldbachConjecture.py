from sys import stdin
class GoldbachConjecture:
    def __init__(self, target):
        self.target = target
        
    def goldbach_selector(self):
        prime = 3
        while self.target//2 >= prime:
            if self.is_prime(prime):
                theother = self.target - prime 
                if self.is_prime(theother):
                    return prime, theother
                else:
                    prime += 2
            else:
                prime += 2
        return False
    
    def is_prime(self, num):
        if num == 3:
            return True
        i = 2
        while i*i <= num:
            if num % i == 0:
                return False
            i += 1
        return True
            
    
    def __str__(self):
        try:
            a, b = self.goldbach_selector()
            return '{} = {} + {}'.format(self.target, a, b)
        except:
            return "Goldbach's conjecture is wrong."
            
while True:
    input_ = int(stdin.readline().strip())
    if input_ != 0:
        goldbach = GoldbachConjecture(input_)
        print(goldbach)
    else:
        break    
