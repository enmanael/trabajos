numero = int(input("Ingrese un número entero: "))  # Error 4: tipo de dato //falta el "int("
if numero % 2 == 0:     # Error 1: de sintaxis //faltaba un "="
 print("El número es par.") 
else: 
 print("El número es impar.") 
cantidad = int(input("¿Cuántos números pares desea ver?: ")) 
contador = 0 
i = 1 
while contador < cantidad:   # Error 2: de sintaxis (falta ':') 
 if i % 2 == 0:
  print("Par número " + str(contador + 1) +":"+str(i))  # Error 3: de tipo al concatenar //nesecita el str
 contador += 1 
 i += 1