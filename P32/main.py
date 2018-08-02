def gcd(first,second):
    for i in range(first,0,-1):
        if first % i == 0:
            if second % i == 0:
                return i
