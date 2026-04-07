import sqlite3

# 🔹 connect to DB
def connect_db():
    conn = sqlite3.connect("stock.db")
    return conn


# 🔹 create table
def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS stock (
        item TEXT PRIMARY KEY,
        quantity INTEGER,
        unit TEXT
    )
    """)

    conn.commit()
    conn.close()


# 🔹 add or update stock
def update_stock(item, quantity, unit, action):
    conn = connect_db()
    cursor = conn.cursor()

    # check if item exists
    cursor.execute("SELECT quantity FROM stock WHERE item=?", (item,))
    result = cursor.fetchone()

    if result:
        current_qty = result[0]

        if action == "add":
            new_qty = current_qty + quantity
        else:
            new_qty = current_qty - quantity

        cursor.execute(
            "UPDATE stock SET quantity=? WHERE item=?",
            (new_qty, item)
        )

    else:
        new_qty = quantity
        cursor.execute(
            "INSERT INTO stock (item, quantity, unit) VALUES (?, ?, ?)",
            (item, new_qty, unit)
        )

    conn.commit()
    conn.close()

    return new_qty

# 🔹 get stock
def get_stock(item):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT quantity, unit FROM stock WHERE item=?", (item,))
    result = cursor.fetchone()

    conn.close()

    if result:
        return result[0], result[1]
    else:
        return None, None