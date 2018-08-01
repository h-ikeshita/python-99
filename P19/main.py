def rotate(Receive,Split,Answer=[]):
    return Receive[Split:] + Receive[:Split]


