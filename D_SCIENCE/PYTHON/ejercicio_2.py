
def calculate_tip(check: float)->float:
    base_tip = 15


    if(check<=0):
        raise ValueError('Only positive numbers are allowed')

    return (check * base_tip) / 100