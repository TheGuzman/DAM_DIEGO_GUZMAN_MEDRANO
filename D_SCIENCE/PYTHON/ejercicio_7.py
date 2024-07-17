

def calculator(first_number:float, operation:str, second_number:float)->float:
    actions_dictionary = {'+':addition(first_number,second_number),'-':substraction(first_number,second_number),'*':multiplication(first_number,second_number),'/':division(first_number,second_number), }
    return actions_dictionary[operation]

def addition(first,second)->float:
    return first+second

def substraction(first,second)->float:
    return first-second

def multiplication(first,second)->float:
    return first*second

def division(first,second)->float:
    return first/second



def main():
    operations = ['+','-','*','/']

    while True :   
        first_numer = int(input('Introduce un número: '))
        operation = input('Introduce una operación: ')
        if operation not in operations:
            operation = input('Introduce una operación válida:  ')
    
        second_numer = int(input('Introduce otro número: '))
        result = calculator(first_numer, operation, second_numer)
        print(f'resultado: {result}')

