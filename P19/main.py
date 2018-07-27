def rotate(receive_list,rotate_distance):
    if rotate_distance > 0:
        receive_list.extend(receive_list[:rotate_distance])
        del receive_list[:rotate_distance]
    elif rotate_distance < 0:
        i = len(receive_list)
        receive_list.extend(receive_list[:rotate_distance])
        del receive_list[:rotate_distance+i]
    return receive_list


