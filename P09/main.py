def pack(DL):#DefaultList 
    PKL = [] #PacKedList
    SL = []  #SplitList  
    
    for x in range(1,len(DL)):
        if DL[x] == DL[x-1]:
            SL.append(DL[x-1]) 
            
            if x == len(DL)-1:
                SL.append(DL[x])
                PKL.append(SL)
                  
        else:
            SL.append(DL[x-1])
            PKL.append(SL)
            SL = []
            
            if x == len(DL)-1:
                SL.append(DL[x])
                PKL.append(SL)

    return PKL
            
