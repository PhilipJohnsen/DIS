from app import conn


# CLOTHING


class ClothingItem:
    def __init__(self, id, name, type_, size, color, price, image_url):
        self.id = id
        self.name = name
        self.type = type_
        self.size = size
        self.color = color
        self.price = price
        self.image_url = image_url

    def __repr__(self):
        return f"<ClothingItem {self.name} ({self.size}, {self.color}) - ${self.price}>"

def get_all_clothing_items():
    with conn.cursor() as cur:
        cur.execute("""
            SELECT id, name, type, size, color, price, image_url
            FROM clothing_item
        """)
        return cur.fetchall()


def clear_cart(customer_id):
    with conn.cursor() as cur:
        cur.execute("""
            DELETE FROM cart_item
            WHERE cart_id = (
                SELECT id FROM cart WHERE customer_id = %s
            )
        """, (customer_id,))
        conn.commit()

def get_filtered_clothing_items(size=None, color=None, type=None, sort_by=None, sort_direction="asc"):
    with conn.cursor() as cur:
        query = "SELECT id, name, type, size, color, price, image_url FROM clothing_item WHERE 1=1"
        params = []

        if size:
            query += " AND size ILIKE %s"
            params.append(size)
        if color:
            query += " AND color ILIKE %s"
            params.append(color)
        if type:
            query += " AND type ILIKE %s"
            params.append(type)

        valid_sort_fields=["name", "price"]
        if sort_by in valid_sort_fields:
            sort_direction = sort_direction.lower()
            if sort_direction not in ["asc", "desc"]:
                sort_direction = "asc"
            query += f" ORDER BY {sort_by} {sort_direction}"

        cur.execute(query, params)
        rows = cur.fetchall()

    # Wrap tuples into ClothingItem objects
    items = [ClothingItem(*row) for row in rows]
    return items



def insert_clothing_item(name, type_, size, color, price, image_url):
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO clothing_item (name, type, size, color, price, image_url)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (name, type_, size, color, price, image_url))
        conn.commit()



# CUSTOMER and the CART


def create_customer(name):
    with conn.cursor() as cur:
        cur.execute("INSERT INTO customer (name) VALUES (%s) RETURNING id", (name,))
        customer_id = cur.fetchone()[0]
        cur.execute("INSERT INTO cart (customer_id) VALUES (%s)", (customer_id,))
        conn.commit()
        return customer_id

def get_cart_items(customer_id):
    with conn.cursor() as cur:
        cur.execute("""
            SELECT cti.id, ci.name, ci.price, ci.image_url, cti.quantity
            FROM cart_item cti
            JOIN clothing_item ci ON ci.id = cti.clothing_item_id
            JOIN cart c ON c.id = cti.cart_id
            WHERE c.customer_id = %s
        """, (customer_id,))
        return cur.fetchall()




def add_to_cart(customer_id, item_id):
    with conn.cursor() as cur:
        cur.execute("SELECT id FROM customer WHERE id = %s", (customer_id,))
        if cur.fetchone() is None:
            cur.execute("INSERT INTO customer (id, name) VALUES (%s, %s)", (customer_id, 'Test User'))

        cur.execute("SELECT id FROM cart WHERE customer_id = %s", (customer_id,))
        result = cur.fetchone()
        if result:
            cart_id = result[0]
        else:
            cur.execute("INSERT INTO cart (customer_id) VALUES (%s) RETURNING id", (customer_id,))
            cart_id = cur.fetchone()[0]

        cur.execute("SELECT id FROM cart_item WHERE cart_id = %s AND clothing_item_id = %s", (cart_id, item_id))
        existing = cur.fetchone()
        if existing:
            cur.execute("UPDATE cart_item SET quantity = quantity + 1 WHERE id = %s", (existing[0],))
        else:
            cur.execute("INSERT INTO cart_item (cart_id, clothing_item_id, quantity) VALUES (%s, %s, 1)", (cart_id, item_id))

        conn.commit()



def get_cart_total_price(customer_id):
    with conn.cursor() as cur:
        cur.execute("""
            SELECT SUM(ci.price * cti.quantity)
            FROM cart_item cti
            JOIN clothing_item ci ON ci.id = cti.clothing_item_id
            JOIN cart c ON c.id = cti.cart_id
            WHERE c.customer_id = %s
        """, (customer_id,))
        result = cur.fetchone()[0]
        return result or 0.0
    
def remove_from_cart(cart_item_id):
    with conn.cursor() as cur:
        cur.execute("DELETE FROM cart_item WHERE id = %s", (cart_item_id,))
        conn.commit()
