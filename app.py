from flask import Flask, render_template, abort

app = Flask(__name__)

# Sample menu data
SAMPLE_ITEMS = [
    {"id": 1, "name": "Cafe con Leche", "category": "Drinks", "price_cents": 350},
    {"id": 2, "name": "Cuban Sandwich", "category": "Food", "price_cents": 950},
    {"id": 3, "name": "Guava Pastelito", "category": "Pastries", "price_cents": 300},
    {"id": 4, "name": "Cortadito", "category": "Drinks", "price_cents": 275},
    {"id": 5, "name": "Media Noche", "category": "Food", "price_cents": 900},
    {"id": 6, "name": "Tres Leches", "category": "Desserts", "price_cents": 450}
]

# Sample kitchen orders
SAMPLE_KITCHEN = [
    {"id": 101, "customer": "Maria Lopez", "items": "Cuban Sandwich, Cafe con Leche", "time": "10:15 AM", "status": "Preparing"},
    {"id": 102, "customer": "Carlos Rivera", "items": "Media Noche, Cortadito", "time": "10:20 AM", "status": "New"},
    {"id": 103, "customer": "Ana Torres", "items": "Guava Pastelito, Cafe con Leche", "time": "10:25 AM", "status": "Ready"}
]

# Sample order history
SAMPLE_ORDERS = [
    {"id": 201, "customer": "Maria Lopez", "items": "Cuban Sandwich, Cafe con Leche", "total_cents": 1300, "status": "Completed"},
    {"id": 202, "customer": "Carlos Rivera", "items": "Media Noche, Cortadito", "total_cents": 1175, "status": "Completed"},
    {"id": 203, "customer": "Ana Torres", "items": "Guava Pastelito, Tres Leches", "total_cents": 750, "status": "Completed"}
]


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Menu page
@app.route("/menu")
def menu():
    return render_template("menu.html", items=SAMPLE_ITEMS)


# Individual menu item page
@app.route("/menu/<int:item_id>")
def item_detail(item_id):
    item = next(
        (item for item in SAMPLE_ITEMS if item["id"] == item_id),
        None
    )

    if item is None:
        abort(404)

    return render_template("item.html", item=item)


# New order page
@app.route("/order/new")
def new_order():
    return render_template("order.html", items=SAMPLE_ITEMS)


# Kitchen board
@app.route("/kitchen")
def kitchen():
    return render_template("kitchen.html", orders=SAMPLE_KITCHEN)


# Order history
@app.route("/orders")
def orders():
    return render_template("history.html", orders=SAMPLE_ORDERS)


if __name__ == "__main__":
    app.run(debug=True)
