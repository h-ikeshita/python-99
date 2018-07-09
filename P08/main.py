def compress(L):
     
    for x in range(1,len(L)):
        if L[x-1] == L[x]:
           L[x-1] = ("empty")
           
    
    while ("empty") in L:
            L.remove("empty")
    return L
 
        
