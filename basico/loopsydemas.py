# #! for
# #? se puede poner solo hasta donde llega, 2 parametros (inicio y fin)
# #? y el 3ro de cuanto va incrementando el ciclo

# suma = 0
# for i in range(1, 100, 10):
#     suma += i
#     print(suma)

# # #! enumerates caon

# frutas = [
#     {"nombre": "manzana", "categoria": "roja"},
#     {"nombre": "fresa", "categoria": "roja"},
#     {"nombre": "pepino", "categoria": "verde"},
#     {"nombre": "perejil", "categoria": "verde"},
#     {"nombre": "manzana verde", "categoria": "verde"},
#     {"nombre": "carayo", "categoria": "sepa"},
#     {"nombre": "siuuu", "categoria": "sepa"},
    
    
# ]


# roja = set()
# verde = set()

# for n,fruta in  enumerate(frutas):
    
#     print(f'fruta {n}, categria {fruta["categoria"]}\n')
#     if fruta["categoria"] == "roja":
#         roja.add(fruta["nombre"])
#         print(f'se añadio la fruta: {fruta["nombre"]}')
#     if fruta["categoria"] == 'verde':
#         verde.add(fruta["nombre"])
#         print(f'se añadio la fruta: {fruta["nombre"]}')
        
#     else:
#         print(f"esta fruta no tiene categoria detectada: {fruta["nombre"]} su categoria es {fruta['categoria']}")
        
# print(roja)
# print(verde)


#! WHILE como en javascript caon
# numeros = {1,2,3,4,5,6,7,7,7,8}
# # print(numeros.__len__())

# contador = 0
# while contador < numeros.__len__():
#     contador +=1
#     print(contador)



# #! LIST COMPRESIONS
# #? sentencias que normalmente llevan varias lineas, resumida a una linea de trancazo caon

# #* forma normal para numeros elevados al cuadrado

# cuadrados = []
# for n in range(5):
#     cuadrados.append(n ** 2)
# print(cuadrados)

# #* en una sola linea
# cuadrados = [i ** 2 for i in range(5)]
# print(cuadrados)

# #* practica:


# # dobles = []
# # for n in numeros:
# #     dobles.append(n * 2)

# # print(dobles)

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# dobles = [i * 2 for i in numeros]
# print(dobles)
# #* ejercicio correcto :D, en este caso tenia que iterar con la lista de numeros pq en el primero de 
# #* muestra no habia para iterar y se debia dar un rango xd



#? ejercicio 2:
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# pares = []
# for n in numeros:
#     if n % 2 == 0:
#         pares.append(n)

# print(pares)


# pares = [n for n in numeros if n%2==0]
# print(pares)

#* listo 
#TODO nota: siempre iniciar con expresion, en este caso n for, no solo el for

# #? ejercicio 3:
# productos = [
#     {"nombre": "laptop", "precio": 15000, "categoria": "tech"},
#     {"nombre": "silla", "precio": 800, "categoria": "muebles"},
#     {"nombre": "mouse", "precio": 300, "categoria": "tech"},
#     {"nombre": "mesa", "precio": 1200, "categoria": "muebles"},
# ]

# caros = []
# for pr in productos:
#     if pr["precio"] > 1000:
#         caros.append(pr["nombre"])

# print(caros)

# caros = [pr["nombre"] for pr in productos if pr["precio"] > 1000]
# print(caros)


# #* LISTO ;D
# #todo en este caso entendi que el primer elemento es lo que se toma del for o del parametor que se evalua/itera xd
# #todo por ejemplo buscabamos filtrar el nombre del producto entonces pr["nombre"] ya despues la condicion
#todo con pr["precio"] > 1000

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# resultado = []
# for n in numeros:
#     if n % 2 == 0:
#         resultado.append(n ** 2)
#     else:
#         resultado.append(n)

# print(resultado)

# resultado = [n**2 if n%2 == 0 else n for n in numeros]
# print(resultado)

#! Dict comprehesions
#? lo mismo que lo anterior pero con diccionatrios


#* manera tradicional
# productos = [
#     {"nombre": "laptop", "precio": 15000, "categoria": "tech"},
#     {"nombre": "silla", "precio": 800, "categoria": "muebles"},
# ]

# # forma tradicional
# precios = {}
# for pr in productos:
#     precios[pr["nombre"]] = pr["precio"]


# precios ={pr["nombre"]: pr["precio"] for pr in productos}
# print(precios)

#todo misma estructura, la condicion o lo que se evalua, y for pr in productos
productos = [
    {"nombre": "laptop", "precio": 15000, "categoria": "tech"},
    {"nombre": "silla", "precio": 800, "categoria": "muebles"},
    {"nombre": "mouse", "precio": 300, "categoria": "tech"},
    {"nombre": "mesa", "precio": 1200, "categoria": "muebles"},
]

#? 1: Crea un dict {nombre: categoria} de todos los productos.
categoria= {pr["nombre"]: pr["categoria"] for pr in productos}
print(categoria)


#? 2-Crea un dict {nombre: precio} pero solo de los productos de categoría "tech"

precios={ pr["nombre"]: pr["precio"]  for pr in productos if pr["categoria"]=="tech"}
print(precios)

#? 3 Crea un dict {nombre: precio} pero con el precio ya con 10% de descuento aplicado (precio * 0.9).

descuento = { pr["nombre"]: pr["precio"] * 0.9 for pr in productos }
print(descuento)

#? 4 Crea un dict donde el precio sea la key y el nombre el value: {precio: nombre}.

invertido = {pr["precio"]: pr["nombre"] for pr in productos}
print(invertido)