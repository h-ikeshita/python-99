def duplicate(receive_list):
    dupled_list = []
    dupled_list.extend(receive_list)
    for origin in receive_list:
            dupled_list.insert(dupled_list.index(origin),origin)
    return dupled_list

