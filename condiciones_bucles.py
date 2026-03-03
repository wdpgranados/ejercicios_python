
# las condiciones sirven para tomar decisiones en en código
edad = 18
if edad >=18:
    print("ya eres mayor de edad")
else:
    print("aun eres menor de edad")
    
# validación en un proceso de pago
saldo_cuenta = 1500
precio_producto = 600
stock_disponible = 5

if stock_disponible > 0:
    if saldo_cuenta >=precio_producto:
        print("compra realizada con éxito")
        saldo_cuenta -= precio_producto
        stock_disponible -= 1
    else:
        print("saldo insuficiente para realizar la compra")
else:
    print("producto agotado")
                
usuario_autenticado = True
rol_usuario = "admin" # puede ser "admin", "editor" o "lector"
cuenta_activa = True

if usuario_autenticado and cuenta_activa:
    if rol_usuario == "admin":
        print("bienvenido admin, tienes acceso completo al sistema")
    elif rol_usuario == "editor":
        print("bienvenido editor, tienes acceso para editar contenido")
    else:
        print("acceso limitado solo acceso de lectura  ")
else:
    print("acceso denegado: usuario no autenticado o cuenta inactiva") 
    
temperatura_actual = 28
temperatura_optima = 22

if temperatura_actual > temperatura_optima + 2 :
    print("hace demasiado calor, enciende el aire acondicionado")
elif temperatura_actual < temperatura_optima - 2:
    print("hace demasiado frío, enciende la calefacción")
else:
    print("la temperatura es agradable, no es necesario ajustar el termostato")
        
import math
numero = int(input("ingrese un numero positivo:"))
while numero < 0:
    print("no puedes ingresar numeros negativos")
    numero = int(input("ingrese un numero positivo:"))
print(f"la raiz cuadrada del {numero} es {math.sqrt(numero):.2f}")


# el bucle while se ejecuta mientras la condición sea verdadera y se detiene cuando la condición se vuelve falsa
i = -1
while i >= -10:
    print(i)
    i -= 1
    
i = 1
while i <= 10:
    if i == 9:
        break # romple el bucle cuando i es igual a 9
    print(i)
    i +=1

numero = 1
while numero <= 10:
    if numero  % 3 == 0:
        numero +=1
        continue # salta el resto del código en la iteración actual y pasa a la siguiente iteración
    print(numero)
    numero +=1   # incrementa el numero en cada iteración para evitar un bucle infinito
        
            
    
    
# bugle for se utiliza para iterar sobre una secuencia de elementos, como listas, tuplas o rangos de números
lista = ["manzana", "banana", "naranja","pera"]

for fruta in lista:
    print(fruta)    

for i in range(1,6):
    print(i)
        