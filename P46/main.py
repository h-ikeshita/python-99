def AND(matter1,matter2):
    if matter1 == True and matter2 == True:
        return True
    return False

def OR(matter1,matter2):
    if matter1 == True or matter2 == True:
        return True
    return False

def NAND(matter1,matter2):
    if matter1 == False or matter2 == False:
        return True
    return False

def NOR(matter1,matter2):
    if matter1 == False and matter2 == False:
        return True
    return False

def XOR(matter1,matter2):
    if matter1 != matter2:
        return True
    return False

def IMP(matter1,matter2):
    if matter1 > matter2:
        return False
    return True

def EQ(matter1,matter2):
    if matter1 == matter2:
        return True
    return False

