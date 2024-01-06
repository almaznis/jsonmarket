from app import db
from datetime import datetime

class Tshirt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    color = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    tshirt_text = db.Column(db.String(200), nullable=False)
    image_url = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Tshirt {self.type} - {self.color}>'

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tshirt_id = db.Column(db.Integer, db.ForeignKey('tshirt.id'), nullable=False)
    tshirt_size = db.Column(db.String(50), nullable=False)
    tshirt_text = db.Column(db.String(50), nullable=True)
    client_phone_number = db.Column(db.Integer, nullable=False)
    client_city = db.Column(db.String(50), nullable=False)
    client_address = db.Column(db.String(100), nullable=False)
    order_date = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        return f'<Order {self.id} - Tshirt ID: {self.tshirt_id}>'