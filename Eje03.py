class operacionInvalida(Exception):
    pass
def Operaciones(operation):
    partes=operation.split()
    num1, operador, num2 = partes
    try:
        Num1 = float(num1)
        Num2 = float(num2)
    except ValueError:
        print("Error: Valores no validos")
        return
    if operador == '+':
        resultado= Num1 + Num2
    elif operador == '-':
        resultado= Num1 - Num2
    elif operador == '*':
        resultado= Num1 * Num2
    elif operador == '/':
        if Num2 == 0:
            print("Error: División por cero")
            return
        resultado= Num1 / Num2
    else:
        raise operacionInvalida(f"Operación inválida: {operador}")
    print(f"Resultado: {resultado}")

Operaciones("10 / 2")