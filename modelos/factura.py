# Modelo de la clase Factura
# Esta clase representa una factura en el sistema de facturación.

from modelos.cliente import Cliente
from modelos.producto import Producto

class Factura:
    def __init__(self, cliente, productos):
        self.cliente = cliente
        self.productos = productos

    def calcular_total(self):
        return sum(p.precio * p.cantidad for p in self.productos)

    def a_diccionario(self):
        return {
            "cliente": self.cliente.a_diccionario(),
            "productos": [p.a_diccionario() for p in self.productos],
            "total": self.calcular_total()
        }