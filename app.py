from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data for products
products = [
    {"id": 1, "name": "Simple Glam", "price": 30000, "image_path": "images/simple_glam.jpg", "description": "A simple glam makeup look involves a flawless base with foundation and concealer, defined brows, neutral eyeshadow shades, winged eyeliner, mascara-coated lashes, a touch of blush, and a nude lipstick or gloss for a polished finish."},
    {"id": 2, "name": "Full Face Beat", "price": 50000, "image_path": "images/full_face_beat.jpg", "description": "A full face beat entails flawless complexion with foundation, concealer, and powder, sculpted brows, defined eyes with eyeshadow, liner, and mascara, contoured cheeks, highlighted features, and a statement lip color, finished with setting spray for longevity and a flawless finish."},
    {"id": 3, "name": "Eye Glam", "price": 10000, "image_path": "images/eye_glam.jpg", "description":"Eye glam features intricate eyeshadow blending, dramatic eyeliner (winged or smoked), voluminous mascara, and optional false lashes for added drama. Sparkling or metallic shades enhance the lids, while dark hues deepen the crease. Highlighter on the inner corner brightens, completing the mesmerizing look."}
]

# Cart to store selected products
cart = []

@app.route('/')
def home():
    cart_count = len(cart)
    return render_template('home.html', products=products, cart_count=cart_count)

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
    if len(cart) == 0:  # Check if the cart is empty
        return redirect(url_for('home'))  # Redirect to home if cart is empty
    else:
        total_price = sum(product['price'] for product in cart)
        return render_template("checkout.html", cart=cart, total_price=total_price)

@app.route('/process_payment', methods=['POST'])
def process_payment():
    cart.clear()
    return render_template("process_payment.html")


if __name__ == '__main__':
    app.run(debug=True)
