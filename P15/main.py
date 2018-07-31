def duplicate(receive_list,duple_times):
    dupled_list = []
    for i in receive_list:
            dupled_list.extend([i]*duple_times)
    return dupled_list 
