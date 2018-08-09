def compress(receive):
    answer = []
    for i in receive:
        if len(answer) == 0 or answer[-1] != i:
            answer.append(i)
    return answer
    

 
        
