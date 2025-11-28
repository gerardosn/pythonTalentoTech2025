#!/usr/bin/env python3
"""Inicializa la base de datos SQLite con valores iniciales.

Ejecútese una sola vez:
    python3 iniciobd.py
"""

import os
import sqlite3

DB_PATH = "productos.db"
INICIALES = (
    ("Camisa", "Ropa", 25),
    ("Zapatos", "Calzado", 50),
    ("Gorra", "Accesorios", 15),
)

def main():
    if os.path.exists(DB_PATH):
        print(f"La base de datos '{DB_PATH}' ya existe. No se realizaron cambios.")
        return
    conn = None
    try:
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                categoria TEXT NOT NULL,
                precio INTEGER NOT NULL
            )
        """)
        cur.executemany(
            "INSERT INTO productos (nombre, categoria, precio) VALUES (?, ?, ?)",
            INICIALES,
        )
        conn.commit()
    except Exception as e:
        print(f"Error al crear la base de datos: {e}")
        raise
    finally:
        if conn:
            conn.close()

    print(f"Base de datos '{DB_PATH}' creada e inicializada con {len(INICIALES)} registros.")


if __name__ == "__main__":
    main()
