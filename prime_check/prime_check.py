import math


def check_prime(num):
    if num < 2 :
        return False
    if num  == 2 :
        return True
    if num % 2 == 0 :
        return False
    if num >= 2 :
        for i in range(3, int(math.sqrt(num))+1,2) :
            if num % i == 0 :
                return False
        return True
    else:
        return False


