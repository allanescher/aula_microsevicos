import sys
from . import create_app, db
from .models import Item

app = create_app()

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
            print('  python cli.py add "Item Name"')
            print('  python cli.py list')
    else:
        with app.app_context():
            db.create_all()
        print('Database initialized.')
