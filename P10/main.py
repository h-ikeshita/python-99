def encode(DL):#DefaultList 
    JL = []  #JudgeList
    AL = []  #AnswerList
    for x in DL:
        if x in JL or len(JL) == 0:JL.append(x)
        else:
            SL = [len(JL),JL[0]]
            AL.append(SL)
            JL = [x]
    else:
        if len(JL) > 0:
            SL = [len(JL),JL[0]]
            AL.append(SL)
    return AL

                  
    
