import gcd

def is_coprime(first,second):
    if gcd.gcd(first,second) == 1:
        return True
    return False    
