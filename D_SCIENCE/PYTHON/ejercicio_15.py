

def time_converter(minutes:int)->str:

    hours_count = minutes//60

    minutes_count = minutes%60

    return f'{minutes} are {hours_count} hours and {minutes_count} minutes'

