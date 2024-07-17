def calculate_discount(price:float)->float:

    discount_percentage = 20
    discount = (price * discount_percentage)/100

    return price -discount