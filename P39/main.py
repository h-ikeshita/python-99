def prime_numbers(range1,range2):
    answer = []
    if range1 < 2:
       range1 = 2
    if range2 < 2:
       range2 = 2  
    if range1 < range2:
        start = range1
        end   = range2
    elif range1 > range2:
        start = range2
        end   = range1
    for i in range(start,end):
        for p in range(2,i):
            if i % p == 0:
                break
        else:
            answer.append(i)
    return answer
