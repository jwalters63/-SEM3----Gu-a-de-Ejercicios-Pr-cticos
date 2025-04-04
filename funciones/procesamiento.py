# funciones/procesamiento.py

import os
from modelos.producto import Producto
from functools import reduce

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def procesar_ventas(ventas):
    while True:
        limpiar_consola()
        print("\n--- Submenú de Ventas ---")
        print("1. Añadir producto")
        print("2. Filtrar productos por precio unitario")
        print("3. Ver inventario de productos")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("0. Volver al menú principal")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            codigo = input("Código del producto: ").strip()
            nombre = input("Nombre del producto: ").strip()
            try:
                precio = float(input("Precio del producto: "))
                cantidad = int(input("Cantidad disponible en inventario: "))
            except ValueError:
                print("⚠️ Entrada inválida. Intente de nuevo.")
                input("Presione Enter para continuar...")
                continue
            ventas.append(Producto(codigo, nombre, precio, cantidad))
            print("Producto añadido correctamente.")
            input("Presione Enter para continuar...")

        elif opcion == "2":
            if not ventas:
                print("No hay productos para filtrar.")
                input("Presione Enter para continuar...")
                continue

            print("\nFiltrar por precio unitario:")
            print("1. MAYOR que...")
            print("2. IGUAL a...")
            print("3. MENOR que...")
            tipo = input("Seleccione una opción: ").strip()
            try:
                valor = float(input("Ingrese el valor a comparar: "))
            except ValueError:
                print("⚠️ Entrada inválida.")
                input("Presione Enter para continuar...")
                continue

            if tipo == "1":
                filtradas = list(filter(lambda p: p.precio > valor, ventas))
            elif tipo == "2":
                filtradas = list(filter(lambda p: p.precio == valor, ventas))
            elif tipo == "3":
                filtradas = list(filter(lambda p: p.precio < valor, ventas))
            else:
                print("Opción inválida.")
                input("Presione Enter para continuar...")
                continue

            print("\nProductos filtrados:")
            for p in filtradas:
                print(p.a_diccionario())
            input("\nPresione Enter para continuar...")

        elif opcion == "3":
            if not ventas:
                print("No hay productos en el inventario.")
                input("Presione Enter para continuar...")
                continue

            print("\nInventario actual:")
            inventario_dict = list(map(lambda p: {
                "codigo": p.codigo,
                "nombre": p.nombre,
                "precio": p.precio,
                "cantidad": p.cantidad,
                "total": p.precio * p.cantidad
            }, ventas))

            for item in inventario_dict:
                print(item)

            total_valor = reduce(lambda acc, item: acc + item["total"], inventario_dict, 0)
            promedio_precio = reduce(lambda acc, item: acc + item["precio"], inventario_dict, 0) / len(inventario_dict)

            print(f"\nValor total del inventario: ${total_valor:.2f}")
            print(f"Precio promedio de los productos: ${promedio_precio:.2f}")
            input("\nPresione Enter para continuar...")

        elif opcion == "4":
            codigo = input("Ingrese el código del producto a actualizar: ").strip()
            producto = next((p for p in ventas if p.codigo == codigo), None)
            if producto:
                print("\nProducto encontrado:")
                print(producto.a_diccionario())
                nombre = input("Nuevo nombre (dejar vacío para no cambiar): ").strip()
                precio = input("Nuevo precio (dejar vacío para no cambiar): ").strip()
                cantidad = input("Nueva cantidad (dejar vacío para no cambiar): ").strip()

                if nombre:
                    producto.nombre = nombre
                if precio:
                    try:
                        producto.precio = float(precio)
                    except ValueError:
                        print("Precio inválido. No se modificó.")
                if cantidad:
                    try:
                        producto.cantidad = int(cantidad)
                    except ValueError:
                        print("Cantidad inválida. No se modificó.")
                print("Producto actualizado correctamente.")
            else:
                print("Producto no encontrado.")
            input("Presione Enter para continuar...")

        elif opcion == "5":
            codigo = input("Ingrese el código del producto a eliminar: ").strip()
            producto = next((p for p in ventas if p.codigo == codigo), None)
            if producto:
                ventas.remove(producto)
                print("Producto eliminado correctamente.")
            else:
                print("Producto no encontrado.")
            input("Presione Enter para continuar...")

        elif opcion == "0":
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
            input("Presione Enter para continuar...")