def decode(DL):
    AL = []
    for x in DL:
        if type(x) == list:
               AL.extend([x[1]] * x[0])
        else:AL.append(x)
    return AL
