def gcd(origin,division):
    while division != 0: 
        origin,division = division,origin%division
    return origin        
