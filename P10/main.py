def encode(receive_list):
    packed_list =[]
    for i in receive_list:
       if len(packed_list) == 0 or i != packed_list[-1][-1]:
           packed_list.append([1,i])
       else:
           packed_list[-1][0]+=1
    return packed_list

                  
    
