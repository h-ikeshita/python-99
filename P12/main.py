def decode(DL):
    AL = []
    for x in DL:
        if type(x) == list:
            for i in range(0,x[0]):
                AL.append(x[1])
        else:AL.append(x)
    return AL
