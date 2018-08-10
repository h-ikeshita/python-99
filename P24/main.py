import random
def rnd_select(lot_times,lotrange):
    list = range(lotrange+1)
    return random.sample(list,k=lot_times)
    
