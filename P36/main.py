def prime_factors_multi(element):
    fact_list = []
    p = 2
    for i in range(2,element):
        if element % p == 0:
            if len(fact_list) == 0 or p != fact_list[-1][0]: 
                fact_list.append([p,1])
            elif fact_list[-1][0] == p:
                fact_list[-1][-1] += 1    
            element = element / p
            p = 2
        else:
            p += 1
    if len (fact_list) == 0:
        fact_list.append([element,1])
    return fact_list 
