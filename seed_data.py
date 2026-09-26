import sqlite3

conn = sqlite3.connect('lost_and_found.db')
cursor = conn.cursor()

# Add sample users
cursor.execute("""
INSERT INTO users (name, email, student_id, created_at, notes)
VALUES ('Alex', 'alex@mail.com', 'S12345', '2026-09-26', 'test user')
""")
alex_id = cursor.lastrowid

cursor.execute("""
INSERT INTO users (name, email, student_id, created_at, notes)
VALUES ('Sam', 'sam@mail.com', 'S67890', '2026-09-26', 'test user')
""")
sam_id = cursor.lastrowid

# Add a lost report (by Alex)
cursor.execute("""
INSERT INTO reports (user_id, type, title, description, category, location, date_time, image_url, status, created_at)
VALUES (?, 'lost', 'Lost Wallet', 'Black leather wallet with student ID inside', 'wallet', 'Library 2nd Floor', '2026-09-25 14:30', NULL, 'open', '2026-09-25')
""", (alex_id,))

# Add a found report (by Sam)
cursor.execute("""
INSERT INTO reports (user_id, type, title, description, category, location, date_time, image_url, status, created_at)
VALUES (?, 'found', 'Found Wallet', 'Black wallet found near library entrance', 'wallet', 'Library Entrance', '2026-09-25 15:00', NULL, 'open', '2026-09-25')
""", (sam_id,))

conn.commit()
conn.close()

print("Sample data added successfully!")