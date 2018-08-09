import random
def rnd_select(lot_times,lotrange):
    randomlist = []
    for i in range(lotrange+1):
        randomlist.append(i)
    return random.sample(randomlist,k=lot_times)
    
