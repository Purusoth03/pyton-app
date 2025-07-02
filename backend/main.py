from fastapi import FastAPI
import os
import psycopg2
from psycopg2.extras import RealDictCursor

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db:5432/postgres")

app = FastAPI()

def get_db():
    conn = psycopg2.connect(DATABASE_URL)
    return conn

@app.get("/api/items")
def read_items():
    conn = get_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT id, name FROM items")
    items = cur.fetchall()
    cur.close()
    conn.close()
    return items
