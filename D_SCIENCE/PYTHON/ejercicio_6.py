

def palindrome_checker(word: str)-> bool:
    word = word.replace(" ","")
    lenth = len(word)
    iterations = int(lenth/2)
    for iteration in range(iterations):
            if not compare_characters(iteration, (lenth-iteration-1), word.lower()):
                return False 
    return True




def compare_characters(first_index:int, last_index:int, word:str)->bool:
    char1 = word[first_index]
    char2 = word[last_index]
    if(char1!=char2):
        return False
    return True
