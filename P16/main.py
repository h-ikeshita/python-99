def drop(RL,Di):
    dropped_list = []
    for i in RL:
        if (RL.index(i)+1) % Di == 0:
            continue
        dropped_list.append(i)
    return dropped_list
    
