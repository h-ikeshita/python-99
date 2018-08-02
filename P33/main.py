def is_coprime(first,second):
    for i in range(first,1,-1):
        if first % i == 0 and second % i == 0:
            return False
        else:continue
    return True    
