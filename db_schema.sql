CREATE TABLE IF NOT EXISTS carts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user INTEGER NOT NULL,
    creation_time_millis datetime NOT NULL,
    status VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS cart_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cart_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    UNIQUE(cart_id, product_id)
);

CREATE TABLE IF NOT EXISTS users (
    login VARCHAR(50) PRIMARY KEY NOT NULL,
    password VARCHAR(50) NOT NULL,
    name VARCHAR(50) NOT NULL,
    is_admin BOOLEAN NOT NULL,
    UNIQUE(login)
);
REPLACE INTO users(login, password, name, is_admin) VALUES ('admin', 'admin', 'Administrador', 1);
REPLACE INTO users(login, password, name, is_admin) VALUES ('cliente', 'cliente', 'Cliente 1', 0);

CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) NOT NULL,
    available_qty INTEGER NOT NULL,
    UNIQUE(name)
);

CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) NOT NULL,
    img VARCHAR(50) NOT NULL,
    price DECIMAL NOT NULL,
    UNIQUE(name)
);

CREATE TABLE IF NOT EXISTS product_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    qty INTEGER NOT NULL,
    item_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    FOREIGN KEY(product_id) REFERENCES product(id_serie),
    FOREIGN KEY(item_id) REFERENCES item(id_serie),
    UNIQUE(product_id, item_id)
);

REPLACE INTO items(name, available_qty) values
db.session.add(Item(name='Tomate', available_qty=50))
db.session.add(Item(name='Alface', available_qty=30))
db.session.add(Item(name='Cebola', available_qty=5))
db.session.add(Item(name='Alho', available_qty=5))
db.session.add(Item(name='Carne', available_qty=15))
db.session.add(Item(name='Frango', available_qty=15))
db.session.add(Item(name='Batata', available_qty=20))
db.session.add(Item(name='Coca-Cola', available_qty=10))
db.session.add(Item(name='Heineken', available_qty=10))
db.session.add(Item(name='Guaraná', available_qty=15))

REPLACE INTO products(name, img, price) values
('Hamburguer', '', 30.5),
('Porção de Batata', '', 15),
('Guaraná', '', 7),
('Heineken', '', 7),
('Coca-Cola', '', 5);
