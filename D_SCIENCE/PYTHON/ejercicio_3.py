
def check_user_is_adult(age: int)-> bool:

    check_age_is_int_format  = isinstance(age, int)

    if not check_age_is_int_format:
        raise TypeError('Age should be an integer number')
    

    if(age<0):
        raise ValueError('Should be greater than 0')
    
  
    return age>=18