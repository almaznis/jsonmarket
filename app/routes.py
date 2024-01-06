# app/routes.py
from flask import request, jsonify, render_template
from app import app, db
from app.models import Tshirt, Order

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/tshirts', methods=['GET'])
def get_tshirts():
    tshirts = Tshirt.query.all()
    return jsonify([{'id': t.id, 'type': t.type, 'color': t.color, 'price': t.price, 'tshirt_text': t.tshirt_text, 'image_url': t.image_url} for t in tshirts])

@app.route('/order', methods=['POST'])
def place_order():
    data = request.json
    new_order = Order(
        tshirt_id=data['tshirt_id'],
        tshirt_size=data['tshirt_size'],
        tshirt_text=data.get('tshirt_text'),  # Using get() as it's nullable and might not be present
        client_phone_number=data['client_phone_number'],
        client_city=data['client_city'],
        client_address=data['client_address'],
        order_date=datetime.utcnow()  # Assuming you want to set the order date to the current time
    )
    db.session.add(new_order)
    db.session.commit()
    return jsonify({'message': 'Order placed successfully!'})

@app.route('/add_tshirt', methods=['POST'])
def add_tshirt():
    data = request.json
    new_tshirt = Tshirt(price=data['price'], color=data['color'], type=data['type'], tshirt_text=data['tshirt_text'], image_url=data['image_url'])
    db.session.add(new_tshirt)
    db.session.commit()
    return jsonify({'message': 'New T-shirt added!'})
