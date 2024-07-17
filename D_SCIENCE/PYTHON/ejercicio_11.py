import datetime

def calculate_age(date:str)->int:
   user_birth_day_year =  datetime.datetime.strptime(date, "%d/%m/%Y").year
   current_time_year = datetime.datetime.now().year

   age = current_time_year - user_birth_day_year
   
   return age

calculate_age('31/01/1994')