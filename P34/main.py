def totient_phi(receive):
    answer = []
    for i in range(1,receive):
        p = receive - i
        if i >= p:break
        for k in range(i,1,-1):
            if i % k == 0 and p % k == 0:
                break
            else:continue
        else:answer.extend([i,p])
    return len(answer)   
