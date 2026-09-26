import sqlite3

conn = sqlite3.connect('lost_and_found.db')
cursor = conn.cursor()

cursor.executescript("""
DROP TABLE IF EXISTS matches;
DROP TABLE IF EXISTS reports;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    student_id TEXT,
    created_at TEXT,
    notes TEXT
);

CREATE TABLE reports (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    type TEXT NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    category TEXT,
    location TEXT,
    date_time TEXT,
    image_url TEXT,
    status TEXT DEFAULT 'open',
    created_at TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE matches (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    lost_report_id INTEGER,
    found_report_id INTEGER,
    match_score REAL,
    status TEXT DEFAULT 'suggested',
    created_at TEXT,
    FOREIGN KEY (lost_report_id) REFERENCES reports(id),
    FOREIGN KEY (found_report_id) REFERENCES reports(id)
);
""")

conn.commit()
conn.close()

print("Database and tables created successfully!")