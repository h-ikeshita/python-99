def prime_factors(element):
    fact_list = []
    p = 2
    for i in range(2,element):
        if element % p == 0:
            fact_list.append(p)
            element = element / p
            p = 2
            continue
        p += 1
    if len (fact_list) == 0:
        fact_list.append(element)
    return fact_list           
