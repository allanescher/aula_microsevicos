import os
import sys
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql://postgres:postgres@db:5432/postgres')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'<Item {self.name}>'

@app.route('/items', methods=['POST'])
def add_item():
    data = request.get_json()
    new_item = Item(name=data['name'])
    db.session.add(new_item)
    db.session.commit()
    return jsonify({'message': 'Item added successfully'}), 201

@app.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    result = [{'id': item.id, 'name': item.name} for item in items]
    return jsonify(result), 200

def insert_item(name):
    with app.app_context():
        new_item = Item(name=name)
        db.session.add(new_item)
        db.session.commit()
        print(f'Item "{name}" added to the database.')

def list_items():
    with app.app_context():
        items = Item.query.all()
        for item in items:
            print(f'{item.id}: {item.name}')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == 'add' and len(sys.argv) == 3:
            item_name = sys.argv[2]
            insert_item(item_name)
        elif command == 'list':
            list_items()
        else:
            print('Usage:')
            print('  python app.py add "Item Name"')
            print('  python app.py list')
    else:
        with app.app_context():
            db.create_all()
        app.run(host='0.0.0.0', port=5000)
