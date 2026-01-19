def sumar(numero_1 : int, numero_2 : int) -> int:
    assert(isinstance(numero_1, int))
    assert(isinstance(numero_2, int))
    assert(numero_1>=0 and numero_2>=0)
    resultado = numero_1 + numero_2
    return resultado

print(sumar(1,"4"))