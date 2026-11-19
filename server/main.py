import pymysql
from fastapi import FastAPI, HTTPException

from server.db import get_connection

app = FastAPI(title="Juego de cartas API")

@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/db-check")
def db_check():
    try:
        conn = get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT 1 AS ok")
                return {"db": "ok", "result": cur.fetchone()}
        finally:
            conn.close()
    except pymysql.MySQLError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error de base de datos: {e}"
        )