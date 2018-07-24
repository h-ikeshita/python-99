def duplicate(receive_list):
    dupled_list = []
    for origin in receive_list:
        for x in range(0,2):
            dupled_list.append(origin)
    return dupled_list
