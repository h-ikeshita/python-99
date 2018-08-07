import sys
sys.path.append('../')
from P33.main import is_coprime
from P32.main import gcd 

def totient_phi(receive):
    answer = []
    for i in range(1,receive):
        p = receive - i
        if i >= p:break
        if is_coprime(i,p) == True:
            answer.extend([i,p])
    return len(answer)
