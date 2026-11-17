DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS menu_items;
DROP TABLE IF EXISTS users;

PRAGMA foreign_keys = ON;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    role TEXT NOT NULL DEFAULT 'customer'
);

CREATE TABLE menu_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price_cents INTEGER NOT NULL DEFAULT 0 CHECK (price_cents >= 0),
    available INTEGER NOT NULL DEFAULT 1 CHECK (available IN (0, 1))
);

CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER REFERENCES users(id) ON DELETE SET NULL,
    customer_name TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'received',
    notes TEXT NOT NULL DEFAULT '',
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE order_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL REFERENCES orders(id) ON DELETE CASCADE,
    menu_item_id INTEGER NOT NULL REFERENCES menu_items(id) ON DELETE RESTRICT,
    quantity INTEGER NOT NULL DEFAULT 1 CHECK (quantity > 0)
);

INSERT INTO menu_items (id, name, category, price_cents) VALUES
    (1, 'Cafe con Leche', 'Drinks', 350),
    (2, 'Cuban Sandwich', 'Food', 950),
    (3, 'Guava Pastelito', 'Pastries', 300),
    (4, 'Cortadito', 'Drinks', 275),
    (5, 'Media Noche', 'Food', 900),
    (6, 'Tres Leches', 'Desserts', 450);

INSERT INTO orders (id, customer_name, status, notes) VALUES
    (101, 'Maria Lopez', 'preparing', 'Extra napkins'),
    (102, 'Carlos Rivera', 'received', ''),
    (103, 'Ana Torres', 'ready', 'Pickup at the counter');

INSERT INTO order_items (order_id, menu_item_id, quantity) VALUES
    (101, 2, 1),
    (101, 1, 1),
    (102, 5, 1),
    (102, 4, 1),
    (103, 3, 2),
    (103, 6, 1);