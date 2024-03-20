from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data for products
products = [
    {"id": 1, "name": "Simple Glam", "price": 30000, "image_path": "images/simple_glam.jpg"},
    {"id": 2, "name": "Full Face Beat", "price": 50000, "image_path": "images/full_face_beat.jpg"},
    {"id": 3, "name": "Eye Glam", "price": 10000, "image_path": "images/eye_glam.jpg"}
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
    total_price = sum(product['price'] for product in cart)
    return render_template("checkout.html", cart=cart, total_price=total_price)

@app.route('/process_payment', methods=['POST'])
def process_payment():
    cart.clear()
    return render_template("process_payment.html")


if __name__ == '__main__':
    app.run(debug=True)
