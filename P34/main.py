import sys
sys.path.append('../')
from P33.main import is_coprime 

def totient_phi(receive):
    answer = 0
    for i in range(1,receive):
        p = receive - i
        if i >= p:
            break
        if is_coprime(i,p):
            answer += 2
    return answer
