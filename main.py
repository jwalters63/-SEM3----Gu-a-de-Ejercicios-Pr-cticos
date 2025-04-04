# main.py

from funciones.procesamiento import procesar_ventas
from funciones.ordenamiento import ordenar_inventario
from busquedas.lineal import buscar_por_codigo, buscar_por_nombre
from busquedas.binaria import buscar_binaria_codigo, buscar_binaria_nombre

inventario = []

def menu_principal():
    while True:
        print("\n=== Menú Principal ===")
        print("1. Gestión de productos y ventas")
        print("2. Ordenar inventario")
        print("3. Buscar producto")
        print("0. Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            procesar_ventas(inventario)

        elif opcion == "2":
            ordenar_inventario(inventario)

        elif opcion == "3":
            if not inventario:
                print("No hay productos en el inventario para buscar.")
                input("Presione Enter para continuar...")
                continue

            print("\n--- Búsqueda de Producto ---")
            print("1. Búsqueda lineal por código")
            print("2. Búsqueda lineal por nombre")
            print("3. Búsqueda binaria por código")
            print("4. Búsqueda binaria por nombre")
            tipo = input("Seleccione una opción: ").strip()

            if tipo == "1":
                valor = input("Ingrese el código del producto: ").strip()
                resultado = buscar_por_codigo(inventario, valor)

            elif tipo == "2":
                valor = input("Ingrese el nombre del producto: ").strip()
                resultado = buscar_por_nombre(inventario, valor)

            elif tipo == "3":
                inventario.sort(key=lambda p: p.codigo)
                valor = input("Ingrese el código del producto: ").strip()
                resultado = buscar_binaria_codigo(inventario, valor)

            elif tipo == "4":
                inventario.sort(key=lambda p: p.nombre.lower())
                valor = input("Ingrese el nombre del producto: ").strip()
                resultado = buscar_binaria_nombre(inventario, valor)

            else:
                print("Opción inválida.")
                input("Presione Enter para continuar...")
                continue

            if resultado:
                print("\nProducto encontrado:")
                print(resultado.a_diccionario())
            else:
                print("\nProducto no encontrado.")
            input("Presione Enter para continuar...")

        elif opcion == "0":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu_principal()