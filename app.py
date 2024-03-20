from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data for products
products = [
    {"id": 1, "name": "Product 1", "price": 10},
    {"id": 2, "name": "Product 2", "price": 20},
    {"id": 3, "name": "Product 3", "price": 30}
]

# Cart to store selected products
cart = []

@app.route('/')
def home():
    return render_template('home.html', products=products)

@app.route('/product/<int:id>')
def product(id):
    product = next((p for p in products if p['id'] == id), None)
    if product:
        return render_template('product.html', product=product)
    return "Product not found"

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    product_id = int(request.form['product_id'])
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        cart.append(product)
    return redirect(url_for('home'))

@app.route('/remove_from_cart', methods=['POST'])
def remove_from_cart():
    product_id = int(request.form['product_id'])
    product = next((p for p in cart if p['id'] == product_id), None)
    if product:
        cart.remove(product)
    return redirect(url_for('view_cart'))  # Redirect to view_cart instead of cart

@app.route('/view_cart')
def view_cart():
    total_price = sum(product['price'] for product in cart)
    return render_template('cart.html', cart=cart, total_price=total_price)

@app.route('/checkout', methods=['POST'])
def checkout():
    # Process payment and delivery information here
    cart.clear()  # Clear the cart after successful checkout
    return "Checkout successful!"

if __name__ == '__main__':
    app.run(debug=True)
