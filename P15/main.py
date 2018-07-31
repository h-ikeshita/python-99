def duplicate(receive_list,duple_times):
    dupled_list = []
    for i in range(duple_times):
            dupled_list.extend(receive_list)
    return sorted(dupled_list) 
