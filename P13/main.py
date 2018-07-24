def encode_direct(receive_list):
    encoded_list = [] #回答用リスト
    element_amount = 0　#(個数、要素）の個数側
    target = 0　　　　　#要素側
    for reference in receive_list:
        if reference == target or element_amount == 0:
            element_amount+=1
        elif reference != target and element_amount == 1:
            encoded_list.append(target)
            target = reference
        else:
            encoded_list.append([element_amount,target])
            element_amount = 1
        target = reference
    else:#HACK:最後に取り残された要素の始末 XXX:最後の要素が単一だった場合は？ 
        encoded_list.append([element_amount,target]) 
    return encoded_list


  
