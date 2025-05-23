CREATE TABLE customer (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE cart (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES customer(id)
);

CREATE TABLE clothing_item (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    type VARCHAR(50),
    size VARCHAR(10),
    color VARCHAR(30),
    price NUMERIC,
    image_url TEXT
);

CREATE TABLE cart_item (
    id SERIAL PRIMARY KEY,
    cart_id INTEGER REFERENCES cart(id),
    clothing_item_id INTEGER REFERENCES clothing_item(id),
    quantity INTEGER DEFAULT 1
);
