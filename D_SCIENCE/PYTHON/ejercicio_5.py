def calculate_sum_even_numbers(target_number: int)->int:
    counter = 0
    for number in range(0, target_number+1, 2):
        counter+=number
    
    return counter

