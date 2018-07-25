import random
def rnd_select(lot_times,lotrange):
    lottery_box = range(lotrange)
    lot_result = []
    for i in range(lot_times):
        lot_result.append(random.choice(lottery_box))
    return lot_result
    
