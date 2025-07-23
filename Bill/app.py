from flask import Flask, render_template, request
from database import init_db, insert_bill_item

app = Flask(__name__)
init_db()  # Ensure DB is ready

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        items = request.form.getlist('item[]')
        quantities = request.form.getlist('quantity[]')
        prices = request.form.getlist('price[]')

        bill_items = []
        total = 0

        for i in range(len(items)):
            name = items[i]
            quantity = int(quantities[i])
            price = float(prices[i])
            amount = quantity * price
            total += amount
            bill_items.append({'name': name, 'quantity': quantity, 'price': price, 'amount': amount})
            insert_bill_item(name, quantity, price, amount)

        return render_template('bill.html', items=bill_items, total=total)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
