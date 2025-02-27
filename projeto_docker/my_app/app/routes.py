from flask import request, jsonify
from . import create_app, db
from .models import Item

app = create_app()

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
