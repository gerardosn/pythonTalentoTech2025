#!/usr/bin/env python3

"""Menú CLI - Productos Básicos Gestión

Este script muestra un menú interactivo con opciones stub para gestionar productos.
La opción 5 cierra la aplicación.
"""

# Lista temporal para almacenar productos (sublistas: [nombre, categoria, precio])
productos = [
    ["Camisa", "Ropa", 25],
    ["Zapatos", "Calzado", 50],
    ["Gorra", "Accesorios", 15],
]


def agregar_producto():
    """Agrega un nuevo producto a la lista de productos."""
    print("\n[Agregar producto]")

    nombre = input("Ingrese el nombre del producto: ").strip()
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

    productos.append([nombre, categoria, precio])
    print(f"Producto '{nombre}' agregado exitosamente.\n")


def mostrar_productos():
    """Muestra todos los productos en la lista."""
    print("\n[Mostrar productos]")

    if not productos:
        print("No hay productos para mostrar.")
        return

    for i, producto in enumerate(productos):
        print(f"{i}. Nombre: {producto[0]}, Categoría: {producto[1]}, Precio: {producto[2]}")
    print("\n")


def buscar_producto():
    """Busca y muestra la información de un producto por su nombre."""
    print("\n[Buscar producto]")

    nombre_buscar = input("Ingrese el nombre del producto a buscar: ").strip()
    while not nombre_buscar:
        print("El nombre del producto no puede estar vacío.")
        nombre_buscar = input("Ingrese el nombre del producto a buscar: ").strip()

    encontrado = False
    for producto in productos:
        if producto[0].lower() == nombre_buscar.lower():
            print(f"\nProducto encontrado: ")
            print(f"  Nombre: {producto[0]}")
            print(f"  Categoría: {producto[1]}")
            print(f"  Precio: {producto[2]}")
            encontrado = True
            break

    if not encontrado:
        print(f"El producto '{nombre_buscar}' no se encontró.\n")


def eliminar_producto():
    """Elimina un producto de la lista por su posición (índice)."""
    print("\n[Eliminar producto]")

    if not productos:
        print("No hay productos para eliminar.\n")
        return

    mostrar_productos()  # Muestra los productos con sus índices

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

        if 0 <= posicion < len(productos):
            posicion_eliminar = posicion
        else:
            print("Posición no encontrada. Por favor ingrese un índice válido.\n")

    nombre_producto_eliminado = productos[posicion_eliminar][0]
    del productos[posicion_eliminar]
    print(f"Producto '{nombre_producto_eliminado}' eliminado exitosamente.\n")


def main():
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

