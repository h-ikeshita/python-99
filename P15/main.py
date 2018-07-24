def duplicate(receive_list,duple_times):
    dupled_list = []
    for reference in receive_list:
        for order in range(0,duple_times):
            dupled_list.append(reference)
    return dupled_list 
