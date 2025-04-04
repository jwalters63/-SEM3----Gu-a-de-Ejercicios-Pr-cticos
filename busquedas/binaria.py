# busquedas/binaria.py

def buscar_binaria_codigo(lista, codigo):
    lista_ordenada = sorted(lista, key=lambda p: p.codigo)
    izquierda, derecha = 0, len(lista_ordenada) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista_ordenada[medio].codigo == codigo:
            return lista_ordenada[medio]
        elif lista_ordenada[medio].codigo < codigo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return None

def buscar_binaria_nombre(lista, nombre):
    lista_ordenada = sorted(lista, key=lambda p: p.nombre.lower())
    izquierda, derecha = 0, len(lista_ordenada) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        actual = lista_ordenada[medio].nombre.lower()
        if actual == nombre.lower():
            return lista_ordenada[medio]
        elif actual < nombre.lower():
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return None