import sqlite3
from pathlib import Path

DB_PATH = "Christmas_Decorations.sqlite"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE Christmas_Decorations(
	id INTEGER PRIMARY KEY,
	name TEXT NOT NULL,
	category TEXT ,
	theme TEXT,
	discription TEXT,
	color TEXT,
	room TEXT,
	quantity INTEGER,
	storage_bin TEXT,
	image_path TEXT,
	notes TEXT)
                """)
    
    conn.commit()
    conn.close()
    print("Christmas Decorations")

if __name__=="__main__":
    Path('images').mkdir(exist_ok=True)
    init_db()