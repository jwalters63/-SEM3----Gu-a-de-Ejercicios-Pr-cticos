# funciones/ordenamiento.py
from modelos.producto import Producto

def bubble_sort_productos(lista, clave, ascendente=True):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            a = getattr(lista[j], clave)
            b = getattr(lista[j + 1], clave)
            if (ascendente and a > b) or (not ascendente and a < b):
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def ordenar_inventario(ventas):
    if not ventas:
        print("No hay productos en el inventario para ordenar.")
        input("Presione Enter para continuar...")
        return

    print("\n--- Ordenamiento del Inventario ---")
    print("1. Ordenar por nombre del producto")
    print("2. Ordenar por ID del producto")
    print("3. Ordenar por precio del producto")
    print("4. Ordenar por cantidad en inventario")
    opcion = input("Seleccione una opción: ").strip()

    claves = {
        "1": "nombre",
        "2": "codigo",
        "3": "precio",
        "4": "cantidad"
    }

    clave = claves.get(opcion)
    if not clave:
        print("Opción inválida.")
        input("Presione Enter para continuar...")
        return

    print("\n¿Desea ordenar de forma ascendente o descendente?")
    print("1. Ascendente")
    print("2. Descendente")
    orden = input("Seleccione una opción: ").strip()
    ascendente = True if orden == "1" else False

    ordenada = bubble_sort_productos(ventas.copy(), clave, ascendente)
    print("\nInventario ordenado:")
    for p in ordenada:
        print(p.a_diccionario())

    input("\nPresione Enter para continuar...")