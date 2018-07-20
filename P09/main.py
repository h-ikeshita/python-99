def pack(receive_list):
    packed_list = []
    for i in receive_list:
        if len(packed_list) == 0 or i != packed_list[-1][0]:
            packed_list.append([i])
        else:
            packed_list[-1].append(i)
    return packed_list            

