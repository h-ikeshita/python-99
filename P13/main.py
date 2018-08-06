def encode_direct(receive,encoded = []):
    encoded.append(receive.pop(0))
    for i in receive:
        if type(encoded[-1]) == list:
            if i == encoded[-1][-1]:
                encoded[-1][0] += 1
            else:
                encoded.append(i)    
        else:
            if i == encoded[-1]:
                encoded[-1] = [2,i]
            else:
                encoded.append(i)
    return encoded


  
