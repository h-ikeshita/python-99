def encode(DL):#DefaultList 
    FXL = [] #FiXedList
    SL = []  #SplitList  
    MTlength = 1
    for x in range(1,len(DL)):
        if DL[x] == DL[x-1]:
            MTlength+=1 
            
            if x == len(DL)-1:
                SL.insert(0,MTlength)
                SL.append(DL[x])
                FXL.append(SL)
                  
        else:
            SL.insert(0,MTlength)
            SL.append(DL[x-1])
            FXL.append(SL)
            SL = []
            MTlength = 1
            
            if x == len(DL)-1:
                SL.insert(0,MTlength)
                SL.append(DL[x])
                FXL.append(SL)

    return FXL
