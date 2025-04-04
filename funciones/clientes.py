# funciones/clientes.py

from modelos.cliente import Cliente, ClienteVIP

def gestionar_clientes(clientes):
    while True:
        print("\n--- Gestión de Clientes ---")
        print("1. Añadir cliente")
        print("2. Modificar cliente")
        print("3. Eliminar cliente")
        print("4. Ver clientes")
        print("0. Volver al menú principal")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            id_cliente = input("ID del cliente: ")
            nombre = input("Nombre: ")
            contacto = input("Contacto: ")
            tipo = input("Tipo de cliente (regular/vip): ").lower()

            if tipo == "vip":
                cliente = ClienteVIP(id_cliente, nombre, contacto)
            else:
                cliente = Cliente(id_cliente, nombre, contacto)

            clientes.append(cliente)
            print("Cliente añadido correctamente.")
            input("Presione Enter para continuar...")

        elif opcion == "2":
            id_cliente = input("Ingrese el ID del cliente a modificar: ")
            cliente = next((c for c in clientes if c.id == id_cliente), None)
            if cliente:
                print(f"Modificando cliente: {cliente.nombre}")
                nuevo_nombre = input("Nuevo nombre (dejar vacío para no cambiar): ")
                nuevo_contacto = input("Nuevo contacto (dejar vacío para no cambiar): ")
                nuevo_tipo = input("Nuevo tipo (regular/vip, dejar vacío para no cambiar): ").lower()

                if nuevo_nombre:
                    cliente.nombre = nuevo_nombre
                if nuevo_contacto:
                    cliente.contacto = nuevo_contacto
                if nuevo_tipo:
                    if nuevo_tipo == "vip" and not isinstance(cliente, ClienteVIP):
                        cliente = ClienteVIP(cliente.id, cliente.nombre, cliente.contacto)
                    elif nuevo_tipo == "regular" and isinstance(cliente, ClienteVIP):
                        cliente = Cliente(cliente.id, cliente.nombre, cliente.contacto)
                    clientes[clientes.index(next(c for c in clientes if c.id == id_cliente))] = cliente
                print("Cliente actualizado.")
            else:
                print("Cliente no encontrado.")
            input("Presione Enter para continuar...")

        elif opcion == "3":
            id_cliente = input("Ingrese el ID del cliente a eliminar: ")
            cliente = next((c for c in clientes if c.id == id_cliente), None)
            if cliente:
                clientes.remove(cliente)
                print("Cliente eliminado correctamente.")
            else:
                print("Cliente no encontrado.")
            input("Presione Enter para continuar...")

        elif opcion == "4":
            if not clientes:
                print("No hay clientes registrados.")
            else:
                print("\nLista de clientes:")
                for c in clientes:
                    print(c.a_diccionario())
            input("Presione Enter para continuar...")

        elif opcion == "0":
            break

        else:
            print("Opción inválida. Intente nuevamente.")
            input("Presione Enter para continuar...")