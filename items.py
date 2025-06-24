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
    sql = """INSERT INTO items (title, description, run_length, user_id, date) VALUES (?, ?, ?, ?, ?)"""
    db.execute(sql, [title, description, run_length, user_id, date])


    item_id = db.last_insert_id()

    sql = "INSERT INTO item_classes (item_id, title, value) VALUES (?, ?, ?)"
    for title, value in classes:
        db.execute(sql, [item_id, title, value])


def add_sign_up(item_id, user_id, comment):
    sql = """INSERT INTO sign_ups (item_id, user_id, comment) VALUES (?, ?, ?)"""
    db.execute(sql, [item_id, user_id, comment])

def get_sign_ups(item_id):
    sql = """SELECT sign_ups.comment, users.username, users.id user_id
            FROM sign_ups, users
            WHERE sign_ups.item_id = ? AND sign_ups.user_id = users.id
            ORDER BY sign_ups.id DESC"""
    return db.query(sql, [item_id])



def get_classes(item_id):
    sql = "SELECT title, value FROM item_classes WHERE item_id = ?"
    return db.query(sql, [item_id])

def get_items():
    sql = "SELECT id, title, date FROM items ORDER BY id DESC"
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
    for title, value in classes:
        db.execute(sql, [item_id, title, value])



def remove_item(item_id):
    sql = "DELETE FROM item_classes WHERE item_id = ?"
    db.execute(sql, [item_id])
    sql = "DELETE FROM items WHERE id = ?"
    db.execute(sql, [item_id])

def find_items(query):
    sql = """SELECT id, title, date
            FROM items
            WHERE title LIKE ? OR description LIKE ?
            ORDER BY id DESC"""
    like = "%" + query + "%"
    return db.query(sql, [like, like])
