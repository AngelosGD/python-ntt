# #! funciones
# #? como en javascript se le pueden dar parametros y podemos usar return o print de manera directa, cualquiera de las 2

# def saludar(nombre):
#     print(f"hola {nombre}")

# saludar("angel")

# #? se usa return para un ejemplo basico de suma
# def suma(a,b):
#     return a + b

# print(suma(2,3))

# #? en este caso se da un parametro por default pero si al llamar la funcion se reemplaza por otro, se pondra el nuevo
# #? en este caso el default era hola, pero al llamarla por 2da vez paso a ser buenas
# def saludars(nombre, saludo="hola"):
#     print(f"{saludo} {nombre}")

# saludars("angel")
# saludars("mariana", "buenas")


# #? funcion argumentos por nombre
# #? se puede llamar la funcion  con el orden de los paramtros o poniendolos directamente
# def crearproducto(nombre, precio,stock):
#     return {"nombre:": nombre, "precio: ": precio, "stock: ": stock}

# print(crearproducto(precio=100, stock=4, nombre="xd"))


# ? retornar multiples valores en vase a 1 parametro
# def stats(numeros):
#     return min(numeros), max(numeros), sum(numeros)/len(numeros)

# minimo, maximo, promedio = stats([1,2,3,4,5])

# # print(minimo)
# # print(maximo)
# # print(promedio)
# #! funciones args
# #? son funciones que reciben la cantidad que sea dada por el usuario de argumetnos, y apartir de eso se puede decidir que hacer
# #? en este ejemplo con el *

# def argumetnso(*numeros):
#     print(sum(numeros))

# argumetnso(1,2,4,5,1)

# #! funciones kwargs
# #? reciben un dict, al contrario de lo anterior que solo recibia una cosa, aqui puede recibir varios
# def kwargs(**datos):
#     print(datos)

# kwargs(nombre="angel", edad=19)
# #? en este ejemplo se manda solo el parametro datos pero al llamar la funcion se desglosa mejor con un nombre y un valor
# #?  una edad y un valor

# #! IMPORTANTE ----- Funciones lamba
# #? funciones de una sola linea, como laas arrow de js

# doble = lambda x: x * 2
# print(doble(5))

# # * se pueden utilizar para argumentar otras funciones, como ordenas un diccionario con medio de precio
# productos = [
#     {"nombre": "a", "precio": 500},
#     {"nombre": "b", "precio": 100},
#     {"nombre": "c", "precio": 2000},
#     {"nombre": "d", "precio": 50},
#     {"nombre": "e", "precio": 2},
# ]

# ordenados = sorted(productos, key=lambda p: p["precio"])
# print(ordenados)


# # ? ejercicios
# # *1. Función calcular_precio_final(precio, descuento=0) que regrese el precio con descuento aplicado (si no le pasas descuento, que sea 0)


# def calcular_precio_final(precio, descuento=0):
#     return precio - (precio * descuento)


# print(calcular_precio_final(100, 0.1))


# # * 2 función stats_productos(productos) que reciba la lista y regrese (con return múltiple) el más caro, el más barato, y el promedio de precios.
# def stats_productos(productos):
#     precios = [pr["precio"] for pr in productos]
#     return max(precios), min(precios), sum(precios) / len(productos)


# productos = [
#     {"nombre": "a", "precio": 500},
#     {"nombre": "b", "precio": 100},
#     {"nombre": "c", "precio": 2000},
#     {"nombre": "d", "precio": 50},
#     {"nombre": "e", "precio": 2},
# ]

# mayor, menor, promedio = stats_productos(productos)

# print(mayor, menor, promedio)

# #? pq no me quedo del todo claro xd
# #* 2.1 Reciba la lista de empleados
# #* Adentro, saque solo los sueldos en una lista nueva (usando list comprehension)
# #* Regrese (con return múltiple) el sueldo más alto, el más bajo, y el promedio

# empleados = [
#     {"nombre": "Juan", "sueldo": 12000},
#     {"nombre": "Maria", "sueldo": 25000},
#     {"nombre": "Pedro", "sueldo": 8000},
#     {"nombre": "Lucia", "sueldo": 18000},
# ]


# def sueldos(empleados):
#     sueldo = [su["sueldo"] for su in empleados]
#     return max(sueldo), min(sueldo), sum(sueldo)/len(sueldo)

# minimo, maximo, promedio = sueldos(empleados)

# print(minimo, maximo, promedio)

# #TODO nota aqui, en el return puse que primero retorne max(sueldo), entonces despúes puse priero minimo, max, promedio =..., entonces
# #TODO el minimo no es el que yo pienso, ya que ese minimo, maximo... retornara el maximo debido al orden del return


# #? ejercicio 3: 
# #* Haz una función total_ventas(*ventas) que reciba cualquier cantidad de montos de venta sueltos y regrese la suma total.

# def total_ventas(*ventas):
#     return sum(ventas)

# print(total_ventas(20,40,599))
# print(total_ventas(109,109,200))

# #? ejercicio 4 Último ejercicio del día 4: usa sorted() con lambda para ordenar la lista de productos de mayor a menor precio.
# productos = [
#     {"nombre": "laptop", "precio": 15000, "categoria": "tech"},
#     {"nombre": "silla", "precio": 800, "categoria": "muebles"},
#     {"nombre": "mouse", "precio": 300, "categoria": "tech"},
#     {"nombre": "mesa", "precio": 1200, "categoria": "muebles"},
# ]


# ordenados = sorted(productos, key=lambda p: p["precio"], reverse=True)
# print(ordenados)


#! Ejercicios extra para reforzaar
#? Default params haz una función calcular_propina(cuenta, porcentaje=15) que regrese cuánto se debe dejar de propina. Si no le pasas porcentaje, usa 15% por default.
def calcular_propina(cuenta, porcentaje=15):
    return (cuenta*porcentaje)/100

print(calcular_propina(500))

#? Keyword arguments haz una función crear_tarjeta(nombre, puesto, empresa) que regrese un string tipo "Angel - Developer en NTTData". 
#? Llámala mandando los argumentos en desorden, usando nombre de parámetro (empresa=..., nombre=..., puesto=...).

def crear_tarjet(nombre, puesto, empresa):
    return(f"{nombre} - {puesto} en {empresa}")


print(crear_tarjet(empresa="ntt-data", nombre="angel", puesto="trainer"))


#? Haz una función analizar_texto(texto) que reciba un string y regrese (con return múltiple): cuántos caracteres tiene, cuántas palabras tiene, y el texto en mayúsculas.
def analizar_texto(texto):
    return len(texto), len(texto.split()), texto.lower()

print(analizar_texto("HOLA MUNDO"))

#? *args Haz una función encontrar_mayor(*numeros) que reciba cualquier cantidad de números sueltos y regrese el más grande, sin usar max() — 
#?tienes que hacerlo con un loop y una variable acumuladora (como hiciste en el día 2, pero ahora dentro de una función con *args).

def encontrar_mayor(*numeros):
    mayor = numeros[0]
    for n in numeros:
        if n > mayor:
            mayor = n
    return mayor

print(encontrar_mayor(10,100,2,8))