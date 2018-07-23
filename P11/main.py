def encode_modified(receive_list):
    encoded_list = []
    for i in receive_list:
        if encoded_list == [] or i != encoded_list[-1][-1]:
            encoded_list.append([1,i])
        else:
            encoded_list[-1][0] += 1
    for i in encoded_list:
        if i[0] == 1:
            encoded_list[encoded_list.index(i)] = i[1]
    return encoded_list                    
