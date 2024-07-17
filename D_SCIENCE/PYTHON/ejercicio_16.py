

def odd_even_counter(numbers:list[int])->dict[str,int]:
    
    even_counter= 0
    odd_counter = 0

    for number in numbers:
        if(number%2==0):
            even_counter+=1
        else:
            odd_counter+=1
    
    return {'even': even_counter, 'odd': odd_counter}