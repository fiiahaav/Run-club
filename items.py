import db

def get_all_classes():
    sql = "SELECT title, value FROM classes ORDER BY id"
    result = db.query(sql)

    classes = {}
    for title, value in result:
        if title not in classes:
            classes[title] = []
    for title, value in result:
        classes[title].append(value)

    return classes

def add_item(title, description, run_length, user_id, date, classes):
    all_classes = get_all_classes()
    sql = """INSERT INTO items (title, description, run_length, user_id, date)
                                VALUES (?, ?, ?, ?, ?)"""
    db.execute(sql, [title, description, run_length, user_id, date])

    item_id = db.last_insert_id()

    link_sql = "INSERT INTO item_classes (item_id, title, value) VALUES (?, ?, ?)"
    for class_title, class_value in classes:
        db.execute(link_sql, [item_id, class_title, class_value])
    return item_id


def add_sign_up(item_id, user_id, comment):
    sql = """INSERT INTO sign_ups (item_id, user_id, comment) VALUES (?, ?, ?)"""
    db.execute(sql, [item_id, user_id, comment])

def get_sign_ups(item_id):
    sql = """SELECT sign_ups.comment, users.username, users.id user_id
            FROM sign_ups, users
            WHERE sign_ups.item_id = ? AND sign_ups.user_id = users.id
            ORDER BY sign_ups.id DESC"""
    return db.query(sql, [item_id])

def get_images(item_id):
    sql = "SELECT id, item_id, image FROM images WHERE item_id = ?"
    return db.query(sql, [item_id])

def add_image(item_id, image):
    sql = "INSERT INTO images (item_id, image) VALUES (?, ?)"
    db.execute(sql, [item_id, image])

def get_image(image_id):
    sql = "SELECT image FROM images WHERE id = ?"
    result = db.query(sql, [image_id])
    return result[0][0] if result else None

def remove_image(item_id, image_id):
    sql = "DELETE FROM images WHERE id = ? AND item_id = ?"
    db.execute(sql, [image_id, item_id])


def get_classes(item_id):
    sql = "SELECT title, value FROM item_classes WHERE item_id = ?"
    return db.query(sql, [item_id])

def get_items():
    sql = """SELECT items.id,
                    items.title,
                    strftime('%d.%m.%Y', items.date) AS formatted_date,
                    users.id AS user_id,
                    users.username,
                    COUNT(sign_ups.comment) AS sign_up_count
             FROM items
             JOIN users ON items.user_id = users.id
             LEFT JOIN sign_ups ON items.id = sign_ups.item_id
             GROUP BY items.id
             ORDER BY items.date ASC"""
    return db.query(sql)

def get_item(item_id):
    sql = """SELECT items.id, items.title,
                         items.description,
                         items.run_length,
                         items.date,
                         users.id AS user_id,
                         users.username
                    FROM items, users
                    WHERE items.user_id = users.id AND items.id = ?"""
    result=db.query(sql, [item_id])
    return result[0] if result else None


def update_item(item_id, title, description, run_length, date, classes):
    sql = """UPDATE items SET title = ?,
                              description = ?,
                              run_length = ?,
                              date = ?
                              WHERE id = ? """
    db.execute(sql, [title, description, run_length, date, item_id])

    sql = "DELETE FROM item_classes WHERE item_id = ?"
    db.execute(sql, [item_id])

    sql = "INSERT INTO item_classes (item_id, title, value) VALUES (?, ?, ?)"
    for class_title, class_value in classes:
        db.execute(sql, [item_id, class_title, class_value])

def remove_item(item_id):
    db.execute("DELETE FROM sign_ups WHERE item_id = ?", [item_id])
    db.execute("DELETE FROM item_classes WHERE item_id=?", [item_id])
    db.execute("DELETE FROM images WHERE item_id = ?", [item_id])
    db.execute("DELETE FROM items WHERE id = ?", [item_id])

def find_items(query):
    sql = """SELECT id, title, date
             FROM items
             WHERE title LIKE ?
                OR description LIKE ?
                OR date LIKE ?
             ORDER BY date DESC"""

    like = "%" + query + "%"
    return db.query(sql, [like, like, query])
