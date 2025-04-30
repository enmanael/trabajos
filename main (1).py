def preparar_datos(info):
    #se espera una cadena
    acumulador = ""
    for letra in info:
        acumulador += letra + "-"
    return acumulador[:-1]  
def mezcla_datos(a, b):
    # se comparan segun el orden 
    if a > b:
        return a + b
    elif a == b:
        return a * 2
    else:
        return b + a
def iniciar():
    entrada1 = input("Ingresa un valor de referencia textual: ")
    entrada2 = input("Ingresa otra unidad: ")
    x = preparar_datos(entrada1)
    y = preparar_datos(entrada2)
    #para convertir la cadena de entrada en una nueva forma
    resultado = mezcla_datos(x, y)
    print("Resultado no final:", resultado)
    # es  un problema de identacion
    if entrada1 in entrada2:
        print("Coincidencia detectada.")
iniciar()
#el codigo es un acumulador pero como no son numeros los que pide si no letras al poner las letras te muestra todas las letras que pusiste
