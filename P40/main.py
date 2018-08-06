def goldbach(receive):
    if receive < 4:
        return []
    for i in range(2,receive):
        if prime_checker(i) == True and prime_checker(receive-i) == True:
                return [i,receive-i]
            
def prime_checker(num):
    for p in range(2,num):
        if num % p == 0:
            return False
    return True
