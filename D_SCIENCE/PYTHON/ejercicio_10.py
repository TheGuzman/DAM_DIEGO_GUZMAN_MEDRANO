

def week_day_selector(day_number:int, language:str = 'es')->str:


    days_dictionary_EN: dict = {
        1:'Monday',
        2:'Tuesday',
        3:'Wednesday',
        4:'Thursday',
        5:'Friday',
        6:'Saturday',
        7:'Sunday',
    }
    
    days_dictionary_GER: dict = {
        1:'Montag',
        2:'Dienstag',
        3:'Mittwoch',
        4:'Donnerstag',
        5:'Freitag',
        6:'Samstag',
        7:'Sonntag',
    }

    days_dictionary_ES: dict = {
        1:'Lunes',
        2:'Martes',
        3:'Miércoles',
        4:'Jueves',
        5:'Viernes',
        6:'Sábado',
        7:'Domingo',
    }

    days_dictionary = {
        'es': days_dictionary_ES,
        'en': days_dictionary_EN,
        'ger': days_dictionary_GER
    }  


    if day_number > 7 or day_number <=0:
        raise ValueError('Introduce un número del 1 al 7')
    
    day = days_dictionary[language][day_number]
    return day
