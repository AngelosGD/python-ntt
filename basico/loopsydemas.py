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
cuadrados = [i ** 2 for i in range(5)]
print(cuadrados)

#* practica:

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# dobles = []
# for n in numeros:
#     dobles.append(n * 2)

# print(dobles)



