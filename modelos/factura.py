# modelos/factura.py

from modelos.cliente import Cliente
from modelos.producto import Producto

class Factura:
    def __init__(self, cliente, productos):
        self.cliente = cliente
        self.productos = productos
        self.total = self.calcular_total()

    def calcular_total(self):
        subtotal = sum(p.precio * p.cantidad for p in self.productos)
        if hasattr(self.cliente, 'tipo') and self.cliente.tipo == "VIP":
            return self.cliente.aplicar_descuento(subtotal)
        return subtotal

    def generar_reporte(self):
        print("\n=== FACTURA ===")
        print(f"Cliente: {self.cliente.nombre} ({self.cliente.tipo})")
        print(f"Contacto: {self.cliente.contacto}")
        print("\nDetalle de productos:")
        for p in self.productos:
            print(f"- {p.nombre} | Cantidad: {p.cantidad} | Precio: ${p.precio:.2f} | Subtotal: ${p.precio * p.cantidad:.2f}")
        print("Los clientes VIP tienen un 10% de descuento.")
        print(f"\nTotal a pagar: ${self.total:.2f}")

    def a_diccionario(self):
        return {
            "cliente": self.cliente.a_diccionario(),
            "productos": [p.a_diccionario() for p in self.productos],
            "total": self.total
        }


class HistorialFacturas:
    def __init__(self):
        self.facturas = []

    def agregar_factura(self, factura):
        self.facturas.append(factura)

    def listar_facturas(self):
        if not self.facturas:
            print("No hay facturas registradas.")
            return

        print("\n=== HISTORIAL DE FACTURAS ===")
        for i, factura in enumerate(self.facturas, start=1):
            print(f"\nFactura #{i}:")
            factura.generar_reporte()