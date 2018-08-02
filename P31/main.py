def is_prime(receive):
    if receive <2:return False
    for i in range(2,receive):
        if receive % i == 0:return False
        else:continue
    return True
