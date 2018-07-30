import random
import itertools
def group(split_group,members):
    SL = []
    for i in split_group: 
        SL.extend(list(itertools.combinations(members,i)));
        del members[0:i]
    GL = list(SL)              
    return list(set(GL))     
