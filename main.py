# main.py

from funciones.procesamiento import procesar_ventas
from funciones.ordenamiento import ordenar_inventario
from funciones.clientes import gestionar_clientes
from busquedas.lineal import buscar_por_codigo, buscar_por_nombre
from busquedas.binaria import buscar_binaria_codigo, buscar_binaria_nombre
from modelos.cliente import Cliente, ClienteVIP
from modelos.factura import Factura, HistorialFacturas
from modelos.producto import Producto

inventario = []
historial = HistorialFacturas()
clientes = []

def menu_principal():
    while True:
        print("\n=== Menú Principal ===")
        print("1. Gestión de productos y ventas")
        print("2. Ordenar inventario")
        print("3. Buscar producto")
        print("4. Gestión de clientes")
        print("5. Generar factura")
        print("6. Ver historial de facturas")
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

        elif opcion == "4":
            gestionar_clientes(clientes)

        elif opcion == "5":
            print("\n--- Generar factura ---")
            id_cliente = input("ID del cliente: ")
            cliente = next((c for c in clientes if c.id == id_cliente), None)

            if not cliente:
                print("Cliente no encontrado. Debe registrarlo primero desde la gestión de clientes.")
                input("Presione Enter para continuar...")
                continue

            productos_factura = []

            while True:
                codigo = input("Código del producto a agregar (Enter para terminar): ").strip()
                if not codigo:
                    break
                producto = buscar_por_codigo(inventario, codigo)
                if not producto:
                    print("Producto no encontrado.")
                    continue
                try:
                    cantidad = int(input(f"Cantidad para '{producto.nombre}': "))
                except ValueError:
                    print("Cantidad inválida.")
                    continue
                productos_factura.append(Producto(producto.codigo, producto.nombre, producto.precio, cantidad))

            if productos_factura:
                factura = Factura(cliente, productos_factura)
                historial.agregar_factura(factura)
                factura.generar_reporte()
            else:
                print("No se agregaron productos a la factura.")

            input("Presione Enter para continuar...")

        elif opcion == "6":
            historial.listar_facturas()
            input("Presione Enter para continuar...")

        elif opcion == "0":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu_principal()
