
import functools

def sum_numbers_in_list(numbers:list[float])->float:
    return functools.reduce(lambda a,b:a+b,numbers,0)