# busquedas/lineal.py

def buscar_por_codigo(lista, codigo):
    for producto in lista:
        if producto.codigo == codigo:
            return producto
    return None

def buscar_por_nombre(lista, nombre):
    for producto in lista:
        if producto.nombre.lower() == nombre.lower():
            return producto
    return None