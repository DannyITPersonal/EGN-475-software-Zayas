import math
import os
import sqlite3
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

NEXT_STATUS = {
    "received": "preparing",
    "preparing": "ready",
    "ready": "picked up",
}


def validate_item(form, item_id=None):
    errors = []
    name = form.get("name", "").strip()
    category = form.get("category", "").strip()
    price = form.get("price", type=float)

    if not name:
        errors.append("Menu item name is required.")
    else:
        normalized_name = " ".join(name.split()).casefold()
        existing_items = db.get_db().execute(
            "SELECT id, name FROM menu_items"
        ).fetchall()
        if any(
            existing_item["id"] != item_id
            and " ".join(existing_item["name"].split()).casefold()
            == normalized_name
            for existing_item in existing_items
        ):
            errors.append("A menu item with this name already exists.")

    if price is None or not math.isfinite(price):
        errors.append("Enter a valid price greater than $0 and no more than $50.")
    elif price <= 0:
        errors.append("Price must be greater than $0.")
    elif price > 50:
        errors.append("Price cannot exceed $50.")

    categories = db.get_db().execute(
        "SELECT DISTINCT category FROM menu_items ORDER BY category"
    ).fetchall()
    valid_categories = [row["category"] for row in categories]
    if category not in valid_categories:
        if valid_categories:
            category_list = ", ".join(valid_categories)
            errors.append(f"Choose a category from: {category_list}.")
        else:
            errors.append("No menu item categories are currently configured.")

    return errors


# Sample menu data
SAMPLE_ITEMS = [
    {"id": 1, "name": "Cafe con Leche", "category": "Drinks", "price_cents": 350},
    {"id": 2, "name": "Cuban Sandwich", "category": "Food", "price_cents": 950},
    {"id": 3, "name": "Guava Pastelito", "category": "Pastries", "price_cents": 300},
    {"id": 4, "name": "Cortadito", "category": "Drinks", "price_cents": 275},
    {"id": 5, "name": "Media Noche", "category": "Food", "price_cents": 900},
    {"id": 6, "name": "Tres Leches", "category": "Desserts", "price_cents": 450}
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


# Menu administration page
@app.route("/admin/menu")
def admin_menu():
    database = db.get_db()
    items = database.execute(
        """
        SELECT id, name, category, price_cents, available
        FROM menu_items
        ORDER BY category, name
        """
    ).fetchall()
    return render_template(
        "menu_admin.html",
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
        name_input = request.form.get("name", "")
        category_input = request.form.get("category", "")
        name = name_input.strip()
        category = category_input.strip()
        form_data = {
            "name": name_input,
            "category": category_input,
            "price": request.form.get("price", ""),
        }
        errors = validate_item(request.form)

        if errors:
            return render_template(
                "new_menu_item.html",
                errors=errors,
                form_data=form_data
            )

        price = request.form.get("price", type=float)
        if price is None:
            return render_template(
                "new_menu_item.html",
                errors=["Enter a valid price greater than $0 and no more than $50."],
                form_data=form_data
            )
        price_cents = round(price * 100)

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
        return redirect(url_for("admin_menu"))

    return render_template("new_menu_item.html", form_data={}, errors=[])


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
        name_input = request.form.get("name", "")
        category_input = request.form.get("category", "")
        name = name_input.strip()
        category = category_input.strip()
        form_data = {
            "name": name_input,
            "category": category_input,
            "price": request.form.get("price", ""),
        }
        errors = validate_item(request.form, item_id=item_id)

        if errors:
            return render_template(
                "edit_menu_item.html",
                item=item,
                form_data=form_data,
                errors=errors
            )

        price = request.form.get("price", type=float)
        if price is None:
            return render_template(
                "edit_menu_item.html",
                item=item,
                form_data=form_data,
                errors=["Enter a valid price greater than $0 and no more than $50."]
            )
        price_cents = round(price * 100)

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
        return redirect(url_for("admin_menu"))

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


# Delete or disable a menu item
@app.route("/items/<int:item_id>/delete", methods=["POST"])
def delete_item(item_id):
    database = db.get_db()
    item = database.execute(
        "SELECT id FROM menu_items WHERE id = ?",
        (item_id,)
    ).fetchone()

    if item is None:
        abort(404)

    order_item = database.execute(
        "SELECT 1 FROM order_items WHERE menu_item_id = ? LIMIT 1",
        (item_id,)
    ).fetchone()

    if order_item is not None:
        database.execute(
            "UPDATE menu_items SET available = 0 WHERE id = ?",
            (item_id,)
        )
        message = "Menu item is in an order and was marked unavailable instead of deleted."
    else:
        try:
            database.execute(
                "DELETE FROM menu_items WHERE id = ?",
                (item_id,)
            )
        except sqlite3.IntegrityError:
            order_item = database.execute(
                "SELECT 1 FROM order_items WHERE menu_item_id = ? LIMIT 1",
                (item_id,)
            ).fetchone()
            if order_item is None:
                raise

            database.execute(
                "UPDATE menu_items SET available = 0 WHERE id = ?",
                (item_id,)
            )
            message = "Menu item is in an order and was marked unavailable instead of deleted."
        else:
            message = "Menu item deleted successfully."

    database.commit()
    flash(message)
    return redirect(url_for("admin_menu"))


# New order page
@app.route("/order/new")
def new_order():
    return render_template("order.html", items=SAMPLE_ITEMS)


# Update an order's status
@app.route("/orders/<int:order_id>/status", methods=["POST"])
def update_order_status(order_id):
    database = db.get_db()
    order = database.execute(
        "SELECT id, status FROM orders WHERE id = ?",
        (order_id,)
    ).fetchone()

    if order is None:
        abort(404)

    requested_status = request.form.get("status", "").strip()
    next_status = NEXT_STATUS.get(order["status"])
    if requested_status != next_status:
        flash("This order cannot be moved to the requested status.")
        return redirect(url_for("kitchen"))

    result = database.execute(
        """
        UPDATE orders
        SET status = ?
        WHERE id = ? AND status = ?
        """,
        (requested_status, order_id, order["status"])
    )
    if result.rowcount != 1:
        flash("The order status changed before this update. Reload the kitchen board and try again.")
        return redirect(url_for("kitchen"))

    database.commit()
    flash(f"Order status updated to {requested_status.title()}.")
    return redirect(url_for("kitchen"))


# Kitchen board
@app.route("/kitchen")
def kitchen():
    database = db.get_db()
    orders = database.execute(
        """
        SELECT orders.id,
               orders.customer_name AS customer,
               COALESCE(group_concat(menu_items.name, ', '), '') AS items,
               strftime('%H:%M', orders.created_at) AS time,
               orders.status
        FROM orders
        LEFT JOIN order_items ON order_items.order_id = orders.id
        LEFT JOIN menu_items ON menu_items.id = order_items.menu_item_id
        GROUP BY orders.id
        ORDER BY orders.created_at
        """
    ).fetchall()
    return render_template(
        "kitchen.html",
        orders=orders,
        next_status=NEXT_STATUS
    )


# Order history
@app.route("/orders")
def orders():
    return render_template("history.html", orders=SAMPLE_ORDERS)


if __name__ == "__main__":
    app.run(debug=True)
