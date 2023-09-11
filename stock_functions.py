import math

def calculate_stock_buying_price(buying_stock_price, buying_quantity):
    buying_price = buying_stock_price * buying_quantity
    return math.ceil(buying_price)

def calculate_buying_fee(buying_stock_price, buying_quantity, discount):
    buying_fee = (buying_stock_price * buying_quantity) * (1.425/1000) * discount
    buying_fee = max(buying_fee, 20)
    return math.ceil(buying_fee)

def calculate_stock_selling_price(selling_stock_price, selling_quantity):
    price = selling_stock_price * selling_quantity
    return math.ceil(price)

def calculate_selling_fee(selling_stock_price, selling_quantity, discount):
    selling_fee = ((selling_stock_price * selling_quantity) * (1.425/1000) * discount) + ((selling_stock_price * selling_quantity) * (3/1000))
    selling_fee = max(selling_fee, 20)
    return math.ceil(selling_fee)

def calculate_earning(buy_stock_price, sell_stock_price, quantity, discount):
    sell_price = sell_stock_price * quantity 
    sell_fee = max((sell_stock_price * quantity * (1.425/1000) * discount), 20)
    buy_price = buy_stock_price * quantity
    buy_fee = max((buy_stock_price * quantity * (1.425/1000)*discount), 20)
    tax = sell_stock_price * quantity * (3/1000)
    
    earning_money = sell_price - (sell_fee + tax) - (buy_price + buy_fee)
    earning_result = "恭喜你賺錢" if earning_money > 0 else ("你賠錢了" if earning_money < 0 else "逃得真快~ 白忙一場，再加油好嗎?")
    
    return earning_result, math.floor(earning_money)