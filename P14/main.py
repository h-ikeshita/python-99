def duplicate(receive_list):
    dupled_list = []
    for i in receive_list:
        dupled_list.extend([i]*2)
    return sorted(dupled_list)

