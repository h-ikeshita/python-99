import sys
sys.path.append('../')
from P32.main import gcd
def is_coprime(first,second):
    return gcd(first,second) == 1
           
