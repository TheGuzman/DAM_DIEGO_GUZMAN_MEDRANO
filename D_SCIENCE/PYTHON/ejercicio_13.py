

def is_prime_number(number:int)->bool:

    if number == 1:
       return False
    elif number > 1:
        flag = True
        for i in range(2,number):
            if (number % i) == 0:
                flag = False
                break
        return flag
    
