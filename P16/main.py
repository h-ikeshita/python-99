def drop(RL,Di):
    dropped_list = []
    round = 1
    for EL in RL:
        if round % Di != 0:
            dropped_list.append(EL)
        round += 1
    return dropped_list
    
