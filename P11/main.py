def encode_modified(DL): #DefaultList
    AL = [] #AnswerList
    JL = [] #JudgeList
    for x in DL:
        if x in JL or len(JL) == 0:JL.append(x)
        else:
            if len(JL) == 1:
                AL.append(JL[0])
                JL = [x]
            else:
                SL = [len(JL),JL[0]]
                AL.append(SL)
                JL = [x]
    else:
       if len(JL) > 1:
           SL = [len(JL),JL[0]]
           AL.append(SL)
       else:AL.append(JL[0])
    return AL
