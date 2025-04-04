class Cliente:
    def __init__(self, id, nombre, contacto):
        self.id = id
        self.nombre = nombre
        self.contacto = contacto
        self.tipo = "Regular"  # Por defecto, los clientes son regulares

    def aplicar_descuento(self, monto):
        return monto  # Cliente regular no tiene descuento

    def a_diccionario(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "contacto": self.contacto,
            "tipo": self.tipo
        }

class ClienteVIP(Cliente):
    def __init__(self, id, nombre, contacto):
        super().__init__(id, nombre, contacto)
        self.tipo = "VIP"

    def aplicar_descuento(self, monto):
        return monto * 0.9  # 10% de descuento