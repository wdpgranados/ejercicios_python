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
        
    