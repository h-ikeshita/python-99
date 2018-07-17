def pack(Li):
    SL = []
    PL = []
    st = 0
    for x in Li:
        if x in SL or len(SL) == 0:
            SL.append(x) 
        else:
            PL.append(SL)
            SL = []
            SL.append(x) 
        st+=1
        if st == len(Li):
            PL.append(SL) 
    return PL

