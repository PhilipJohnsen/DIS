from app import app, conn  # Ensure conn is your psycopg2 connection

def initialize_database():
    with conn.cursor() as cur:
        # Opret tabel til kunder
        cur.execute("""
            CREATE TABLE IF NOT EXISTS customer (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL
            );
        """)

        # Opret tabel til kurve
        cur.execute("""
            CREATE TABLE IF NOT EXISTS cart (
                id SERIAL PRIMARY KEY,
                customer_id INTEGER REFERENCES customer(id)
            );
        """)

        # Opret tabel til tøjprodukter
        cur.execute("""
            CREATE TABLE IF NOT EXISTS clothing_item (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                type VARCHAR(50),
                size VARCHAR(10),
                color VARCHAR(30),
                price NUMERIC,
                image_url TEXT
            );
        """)

        # Opret tabel til varer i kurven
        cur.execute("""
            CREATE TABLE IF NOT EXISTS cart_item (
                id SERIAL PRIMARY KEY,
                cart_id INTEGER REFERENCES cart(id),
                clothing_item_id INTEGER REFERENCES clothing_item(id),
                quantity INTEGER DEFAULT 1
            );
        """)

        conn.commit()
        print("Database initialized successfully.")

if __name__ == "__main__":
    initialize_database()
