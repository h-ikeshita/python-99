def pack(receive_list):
    packed_list = []
    target = 1
    element_amount = 0
    if len(receive_list)>0:
        for source in receive_list:
            if source != target:
                packed_list.append([target]*element_amount)
                element_amount = 0      
                target = source
            element_amount+=1
        else:
            packed_list.append([target]*element_amount)
    return packed_list

