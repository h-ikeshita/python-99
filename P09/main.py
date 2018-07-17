def pack(Li):
    SL = []
    PL = []
    for x in Li:
        if x in SL or len(SL) == 0:SL.append(x) 
        else:
            PL.append(SL)
            SL = []
            SL.append(x)
    else:
        if len(Li) > 0:PL.append(SL) 
    return PL

