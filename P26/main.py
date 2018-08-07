def combination(size,members,index_member=0,split_list=[]):
    stack = []
    for i in range(index_member, len(members)):
        add = split_list + [members[i]]
        if len(add) == size:
            stack = stack + [add]
        elif len(add) < size:
            stack = stack + combination(size,members,i+1,add)
    return stack
         
