import sqlite3

def init_db():
    conn = sqlite3.connect("ranker.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS candidates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            phone TEXT,
            skills TEXT,
            score REAL,
            resume_file TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_candidate(candidate):
    conn = sqlite3.connect("ranker.db")
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO candidates (name, email, phone, skills, score, resume_file)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        candidate.get("name"),
        candidate.get("email"),
        candidate.get("phone"),
        ", ".join(candidate.get("skills", [])),
        candidate.get("score"),
        candidate.get("file_name")
    ))
    conn.commit()
    conn.close()

def get_all_candidates():
    conn = sqlite3.connect("ranker.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM candidates")
    data = cursor.fetchall()
    conn.close()
    return data
