import random
def rnd_select(lotset,lottery):
    lot_list = []
    for i in range(lottery):
        lot_list.append(random.choice(lotset))
    return lot_list
