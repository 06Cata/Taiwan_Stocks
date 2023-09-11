from flask import Flask, request, render_template, jsonify
from stock_functions import calculate_stock_buying_price, calculate_buying_fee, calculate_stock_selling_price, calculate_selling_fee, calculate_earning

import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index_stock.html')

@app.route('/buy')
def buy():
    return render_template('buy.html')

@app.route('/sell')
def sell():
    return render_template('sell.html')

@app.route('/earning')
def buy_sell():
    return render_template('earning.html')

@app.route('/calculate_buy', methods=['POST'])
def calculate_buy():
    buying_stock_price = float(request.form['buying_stock_price'])
    buying_quantity = int(request.form['buying_quantity'])
    discount = float(request.form['discount'])
    
    buying_price = calculate_stock_buying_price(buying_stock_price, buying_quantity)
    buying_fee = calculate_buying_fee(buying_stock_price, buying_quantity, discount)
    
    result = f"買入股票價格為: {buying_price} NTD\n買入手續費為: {buying_fee} NTD"
    
    return result

@app.route('/calculate_sell', methods=['POST'])
def calculate_sell():
    selling_stock_price = float(request.form['selling_stock_price'])
    selling_quantity = int(request.form['selling_quantity'])
    discount = float(request.form['discount'])
    
    selling_price = calculate_stock_selling_price(selling_stock_price, selling_quantity)
    selling_fee = calculate_selling_fee(selling_stock_price, selling_quantity, discount)
    
    result = f"賣出股票價格為: {selling_price} NTD\n賣出手續費為: {selling_fee} NTD"
    
    return result

@app.route('/calculate_earn', methods=['POST'])
def calculate_earning_route():
    buy_stock_price = float(request.form['buy_stock_price'])
    sell_stock_price = float(request.form['sell_stock_price'])
    quantity = int(request.form['quantity'])
    discount = float(request.form['discount'])

    earning_result, earning_money = calculate_earning(buy_stock_price, sell_stock_price, quantity, discount)

    result = f"{earning_result}, 獲利: {earning_money} NTD"
    
    return result

# 
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=10000, debug=True)
