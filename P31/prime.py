print ("Please Enter prime.prime_writer('Upper Limit Number','order')")
print ("order <<< If Need Prime Amount'y' /// Need Prime List'n'")    
def prime_writer(limit,order):
    box = []
    for i in range(2,limit):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
           box.append(i)
    if order == "n":return box
    elif order == "y":return len(box)

