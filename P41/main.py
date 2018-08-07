def goldbach_list(start,end,cut = 0):
    split_list = []
    for x in range(start,end+1):
        if x % 2 != 0 or x == 2:
            continue
        split_list.extend([[x] + goldbach(x)])
    return cut_back(split_list,cut)
        
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

def cut_back(receive_list,cut_range):
    cutted_list = []
    for i in receive_list:
        if i[1] > cut_range:
            cutted_list.append(i)        
    return cutted_list            
