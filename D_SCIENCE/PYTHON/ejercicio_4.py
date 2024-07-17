def vowel_counter(word:str)->int:

    vowels = ['a','e','i','o','u']

    vowel_counter = 0
    for letter in word:
        if(letter.lower() in vowels):
            vowel_counter+=1
    
    return vowel_counter