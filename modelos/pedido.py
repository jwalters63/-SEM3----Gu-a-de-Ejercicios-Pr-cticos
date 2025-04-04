# modelos/pedido.py

from modelos.cliente import Cliente
from modelos.producto import Producto

class Pedido:
    def __init__(self, cliente, productos):
        self.cliente = cliente  # instancia de Cliente o ClienteVIP
        self.productos = productos  # lista de instancias de Producto
        self.total = self.calcular_total()

    def calcular_total(self):
        subtotal = sum(p.precio * p.cantidad for p in self.productos)
        if hasattr(self.cliente, 'tipo') and self.cliente.tipo == "VIP":
            return self.cliente.aplicar_descuento(subtotal)
        return subtotal

    def mostrar_resumen(self):
        print(f"Cliente: {self.cliente.nombre} ({self.cliente.tipo})")
        print("Productos comprados:")
        for p in self.productos:
            print(f"- {p.nombre}: {p.cantidad} x ${p.precio:.2f}")
        print(f"Total con descuento aplicado: ${self.total:.2f}")