CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
);

CREATE TABLE items (
    id INTEGER PRIMARY KEY,
    title TEXT,
    description TEXT,
    run_length INTEGER,
    date TEXT,
    user_id INTEGER REFERENCES users
);

CREATE TABLE sign_ups (
    id PRIMARY KEY,
    item_id  INTEGER REFERENCES items,
    user_id INTEGER REFERENCES users,
    comment TEXT
);


CREATE TABLE images (
    id INTEGER PRIMARY KEY,
    item_id INTEGER REFERENCES items,
    image BLOB
);


CREATE TABLE classes (
    id INTEGER PRIMARY KEY,
    title TEXT,
    value TEXT
);

CREATE TABLE item_classes (
    id INTEGER PRIMARY KEY,
    item_id INTEGER REFERENCES items,
    title TEXT,
    value TEXT
);
