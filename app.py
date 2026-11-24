import math
import os
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    abort,
    flash
)
import db

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev")

app.config["DATABASE"] = os.path.join(
    app.instance_path,
    "cafe.sqlite"
)

os.makedirs(app.instance_path, exist_ok=True)

db.init_app(app)

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
    database = db.get_db()
    items = database.execute(
        """
        SELECT id, name, category, price_cents
        FROM menu_items
        WHERE available = 1
        ORDER BY name
        """
    ).fetchall()
    return render_template(
        "menu.html",
        items=items
    )


# Individual menu item page
@app.route("/menu/<int:item_id>")
def item_detail(item_id):
    database = db.get_db()
    item = database.execute(
        "SELECT * FROM menu_items WHERE id = ?",
        (item_id,)
    ).fetchone()

    if item is None:
        abort(404)

    return render_template(
        "item.html",
        item=item
    )


# Add a menu item
@app.route("/admin/menu/new", methods=["GET", "POST"])
def new_menu_item():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        category = request.form.get("category", "").strip()
        price = request.form.get("price", "").strip()
        form_data = {
            "name": name,
            "category": category,
            "price": price,
        }

        if not name:
            return render_template(
                "new_menu_item.html",
                error="Menu item name is required.",
                form_data=form_data
            )

        if not category:
            return render_template(
                "new_menu_item.html",
                error="Menu item category is required.",
                form_data=form_data
            )

        try:
            price_value = float(price)
            if not math.isfinite(price_value) or price_value < 0:
                raise ValueError
            price_cents = round(price_value * 100)
            if price_cents > 9223372036854775807:
                raise ValueError
        except (OverflowError, ValueError):
            return render_template(
                "new_menu_item.html",
                error="Enter a valid non-negative price.",
                form_data=form_data
            )

        database = db.get_db()
        database.execute(
            """
            INSERT INTO menu_items
            (name, category, price_cents, available)
            VALUES (?, ?, ?, ?)
            """,
            (name, category, price_cents, 1)
        )
        database.commit()
        return redirect(url_for("menu"))

    return render_template("new_menu_item.html", form_data={})


# Edit a menu item
@app.route("/items/<int:item_id>/edit", methods=["GET", "POST"])
def edit_menu_item(item_id):
    database = db.get_db()
    item = database.execute(
        "SELECT id, name, category, price_cents FROM menu_items WHERE id = ?",
        (item_id,)
    ).fetchone()

    if item is None:
        abort(404)

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        category = request.form.get("category", "").strip()
        price = request.form.get("price", "").strip()
        form_data = {
            "name": name,
            "category": category,
            "price": price,
        }
        errors = []

        if not name:
            errors.append("Menu item name is required.")

        if not category:
            errors.append("Menu item category is required.")

        try:
            price_value = float(price)
            if not math.isfinite(price_value) or price_value < 0:
                raise ValueError
            price_cents = round(price_value * 100)
            if price_cents > 9223372036854775807:
                raise ValueError
        except (OverflowError, ValueError):
            errors.append("Enter a valid non-negative price.")
            price_cents = None

        if errors:
            return render_template(
                "edit_menu_item.html",
                item=item,
                form_data=form_data,
                errors=errors
            )

        database.execute(
            """
            UPDATE menu_items
            SET name = ?, category = ?, price_cents = ?
            WHERE id = ?
            """,
            (name, category, price_cents, item_id)
        )
        database.commit()
        flash("Menu item updated successfully.")
        return redirect(url_for("menu"))

    form_data = {
        "name": item["name"],
        "category": item["category"],
        "price": "{:.2f}".format(item["price_cents"] / 100),
    }
    return render_template(
        "edit_menu_item.html",
        item=item,
        form_data=form_data,
        errors=[]
    )


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
