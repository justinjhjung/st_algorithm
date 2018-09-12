start, stop = (int(x) for x in input().split())

class GetPrime:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        
    def prime_checker(self, num):
        if num == 1:
            return False
        elif num == 2:
            return True
        else:
            early_stop = round(num**.5)
            j = 2
            while j <= early_stop:
                if num % j != 0:
                    if j != early_stop:
                        j += 1
                    else:
                        return True
                        break
                else:
                    return False
                    break

    def get_prime(self):
        prime_list = []
        for i in range(self.start, self.stop+1):
            if self.prime_checker(i) == True:
                prime_list.append(i)
        return prime_list
    
    def __str__(self):
        prime_list = self.get_prime()
        prime_list_str = [str(x) for x in prime_list]
        return '\n'.join(prime_list_str)
    
primes = GetPrime(start, stop)
print(primes)
