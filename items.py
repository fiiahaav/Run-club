import db

def add_item(title, description, run_length, user_id):
    sql = """INSERT INTO items (title,      description, run_length, user_id) VALUES (?, ?, ?, ?)"""
    db.execute(sql, [title, description, run_length, user_id])
