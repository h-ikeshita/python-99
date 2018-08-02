def drop(receive,drop_point):
    dropped_list = []
    for i in range(len(receive)):
        if (i+1) % drop_point != 0:   
            dropped_list.append(receive[i])
    return dropped_list
    
