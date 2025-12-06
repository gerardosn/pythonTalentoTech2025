#!/usr/bin/env python3

"""Menú CLI - Productos Básicos Gestión

Este script muestra un menú interactivo con opciones stub para gestionar productos.
La opción 5 cierra la aplicación.
"""

import sqlite3
import os
DB_PATH = 'productos.db'

def agregar_producto():
    """Agrega un nuevo producto a la base de datos."""
    print("\n[Agregar producto]")
    nombre = input("Ingrese el nombre del producto: ").strip()
    # Verifica que el nombre no esté vacío antes de continuar.
    while not nombre:
        print("El nombre del producto no puede estar vacío.")
        nombre = input("Ingrese el nombre del producto: ").strip()
    categoria = input("Ingrese la categoría del producto: ").strip()
    while not categoria:
        print("La categoría del producto no puede estar vacía.")
        categoria = input("Ingrese la categoría del producto: ").strip()
    precio = None
    while precio is None:
        precio_str = input("Ingrese el precio del producto (número entero): ").strip()
        if not precio_str:
            print("El precio del producto no puede estar vacío.")
            continue
        if not precio_str.isdigit():
            print("Entrada inválida. Ingrese un número entero para el precio.")
            continue
        precio = int(precio_str)
    # Se utiliza un context manager (with statement) para manejar la conexión a la base de datos.
    # Según la documentación oficial de Python, el context manager garantiza que la conexión se cierre automáticamente al salir del bloque:
    # https://docs.python.org/3/library/sqlite3.html#using-the-connection-as-a-context-manager
    # Por eso no es necesario llamar explícitamente a conn.close().
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO productos (nombre, categoria, precio) VALUES (?, ?, ?)", (nombre, categoria, precio))
        conn.commit()
    print(f"Producto '{nombre}' agregado exitosamente.\n")


def mostrar_productos():
    """Muestra todos los productos en la base de datos."""
    print("\n[Mostrar productos]")
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("SELECT nombre, categoria, precio FROM productos")
        productos_db = cur.fetchall()
    if not productos_db:
        print("No hay productos para mostrar.")
        return
    for i, producto in enumerate(productos_db):
        print(f"{i}. Nombre: {producto[0]}, Categoría: {producto[1]}, Precio: {producto[2]}")
    print("\n")


def buscar_producto():
    """Busca y muestra la información de un producto por su nombre en la base de datos."""
    print("\n[Buscar producto]")
    nombre_buscar = input("Ingrese el nombre del producto a buscar: ").strip()
    while not nombre_buscar:
        print("El nombre del producto no puede estar vacío.")
        nombre_buscar = input("Ingrese el nombre del producto a buscar: ").strip()
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("SELECT nombre, categoria, precio FROM productos WHERE LOWER(nombre) = LOWER(?)", (nombre_buscar,))
        producto = cur.fetchone()
    if producto:
        print(f"\nProducto encontrado: ")
        print(f"  Nombre: {producto[0]}")
        print(f"  Categoría: {producto[1]}")
        print(f"  Precio: {producto[2]}")
    else:
        print(f"El producto '{nombre_buscar}' no se encontró.\n")


def eliminar_producto():
    """Elimina un producto de la base de datos por su posición (índice mostrado)."""
    print("\n[Eliminar producto]")
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("SELECT id, nombre, categoria, precio FROM productos")
        productos_db = cur.fetchall()
    if not productos_db:
        print("No hay productos para eliminar.\n")
        return
    for i, producto in enumerate(productos_db):
        print(f"{i}. Nombre: {producto[1]}, Categoría: {producto[2]}, Precio: {producto[3]}")
    posicion_eliminar = None
    while posicion_eliminar is None:
        posicion_str = input("Ingrese la posición del producto a eliminar: ").strip()
        if not posicion_str:
            print("La posición no puede estar vacía.")
            continue
        if not posicion_str.isdigit():
            print("Entrada inválida. Ingrese un número entero para la posición.")
            continue
        posicion = int(posicion_str)
        if 0 <= posicion < len(productos_db):
            posicion_eliminar = posicion
        else:
            print("Posición no encontrada. Por favor ingrese un índice válido.\n")
    producto_a_eliminar = productos_db[posicion_eliminar]
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM productos WHERE id = ?", (producto_a_eliminar[0],))
        conn.commit()
    print(f"Producto '{producto_a_eliminar[1]}' eliminado exitosamente.\n")


def main():
    # Verifica si el archivo de la base de datos existe antes de mostrar el menú.
    # Utiliza os.path.exists(path) según la documentación oficial de Python:
    # https://docs.python.org/3/library/os.path.html#os.path.exists
    # Si la base de datos no existe, informa al usuario y termina la ejecución.
    if not os.path.exists(DB_PATH):
        print("No existe la bd. ejecute iniciobd.py")
        return
    while True:
        print("""
*************************************
***Productos Basicos Gestion***
************************************
Ingrese la opcion numero que desea:
1. Agregar producto 
2. Mostrar productos 
3. Buscar producto 
4. Eliminar producto 
5. Salir
""")

        opcion = input("Opción: ").strip()

        if not opcion.isdigit():
            print("Entrada inválida. Ingrese el número de la opción (1-5).\n")
            continue

        opcion = int(opcion)

        if opcion == 1:
            agregar_producto()
        elif opcion == 2:
            mostrar_productos()
        elif opcion == 3:
            buscar_producto()
        elif opcion == 4:
            eliminar_producto()
        elif opcion == 5:
            print("Saliendo... ¡Hasta luego!")
            break
        else:
            print("Opción fuera de rango. Por favor ingrese un número entre 1 y 5.\n")

        # Pausa corta para que el usuario vea el resultado antes de mostrar el menú otra vez
        input("Presione Enter para continuar...")


if __name__ == "__main__":
    main()

