def rotate(receive_list,rotate_distance):
    if rotate_distance > 0:
        for i in range(0,rotate_distance):
            receive_list.append(receive_list.pop(0))
    elif rotate_distance < 0:
        for i in range(0,rotate_distance,-1):
            receive_list.insert(0,receive_list.pop(-1))
    return receive_list
