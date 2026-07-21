"""[def sumar(n1, n2):
    resultado = n1 + n2
    print(resultado)


sumar(1,2)

def sumarFstring(n1,n2):
    resultado = n1 + n2
    print(f"numero puesto 1: {n1}")
    print(f"numero puesto 2: {n2}")

    print(resultado)

sumarFstring(2,3)


nombre = input('ingresa nombre: ')
edad = int(input('ingresa edad: '))


def siesadmin():
    if (nombre == 'angel'):
        print(f'bienvenido {nombre}')
    else:
        print(f'no eres admin, eres {nombre}')

def siesmayor():
    if(edad >= 18):
        print('eres mayor')
    else:
        print(f'eres menor, tienes {edad} caon')

siesadmin()
siesmayor()
]
"""

# listas

frutas = ["apple", "manzana", "bamama", "uvas", "arandano", "manzana", "apple"]

# print(frutas[0]) # ? primer elemento
# print(frutas[-1]) # ? el -1 hace referencia al ultimo elemento
# print(frutas[0:4]) # ? slice es decir recore desde el emento 0 hasta el 4, el 4 no se muestra es donde para, se muestra 1 antes


# #? metodos de litas
# frutas.append('xd')
# print(frutas)

# #? copia los elemento de una lista y se puede encasillar en una nueva con ese copy
# frutas2 = frutas.copy()
# frutas2.append('pepino')
# print(frutas2)

# ? metodo extend, deja extender o instanciar una lista o tupla a otra xd, aadir esos valores de la lista
# print(frutas.count('apple'))

# frutas2=["apel","carajo", "mexico"]

# frutas.extend(frutas2)
# print(frutas)

# ? busca el index del elemento dado, este aso arandano, esta en la pisicion 4 de la lista
# print(frutas.index('arandano'))

# ? agrega el elemento dado al indice o posicion proprocionada, en este caso antes arandano era 4, paso a ser 5, y lol 4 xd
# frutas.insert(4, 'lol')
# print(frutas)

# ? popea el indice dado, en este cao 4 es arandanos xd pobre arandano ;,v
# frutas.pop(4)

# print(frutas)
# frutas.remove('uvas')
# if(frutas == ValueError):
#     print(f'elemento no encoontrado')
# else:
#     print(frutas)


# #! Tuplas
# #? listas que no se pueden mutar una vz dado su valor

# coordenadas = (12.3, 109.3)
# coordenadas2 = (15.4, 102.3)


# #? metodo add sirve para añadir o concatenaar tuplas
# #? se tiene que contanear solo tupla con tupla
# coordenadas.__add__(coordenadas2)
# print(coordenadas.__add__(coordenadas2))


#! Diccionarios
# ? equivalente a clases o objetos en pytho
producto = {"producto": "compu", "precio": 1500, "cantidad": 5}

# ? asi se crean como si hubiera mas de 2
productos = [
    {"producto": "compu2", "precio": 12500, "cantidad": 5},
    {"producto": "celular gei", "precio": 2500, "cantidad": 10},
    {"producto": "macbuk", "precio": 25000, "cantidad": 2},
]

# #? se puede imprimir un solo diccionario
# #? para imprimir en una lista con varios diccionarios se tiene que poner el ikndice del diccionario y despues el nombre de la caracteristica
# print(producto["precio"])
# print(productos[0]["precio"])

# #? el del sirve para eliminar algo de el diccionario, si se desea uno especifico
# del producto["cantidad"]
# print(producto)

# ? aqui puede eliminar o algo de un dado indice de producto, o eliminar todo ese indice xd
# del productos[2]
# print(productos)

productos = [
    {"nombre": "laptop", "precio": 15000, "categoria": "tech"},
    {"nombre": "silla", "precio": 800, "categoria": "muebles"},
    {"nombre": "mouse", "precio": 300, "categoria": "tech"},
    {"nombre": "mesa", "precio": 1200, "categoria": "muebles"},
]

# mayor = 0
# nombre_mayor = ""

# for pr in productos:
#     if pr["precio"] > mayor:
#         mayor = pr["precio"]
#         nombre_mayor = pr["nombre"]


# print(nombre_mayor)

# suma_produtos = 0

# for pr in productos:
#     suma_produtos = suma_produtos + pr["precio"]

# print(suma_produtos)

# produtosTech = []


# for pr in productos:
#     if pr["categoria"] == "tech":
#         print(pr["nombre"])
#         produtosTech.append(pr["nombre"])
        

# print(produtosTech)

#! Sets

#* cosa a destacar, los sets si hay elementos duplicados no losm toma enc uenta, ejemplo si hay 2 rojos, solo pone 1 rojo por los 2
#? si asi se crea uno xd 
colores = {"rojo", "azul", "verde"}

# setVacio = set()

# # #? con los sets si se usa remove y no existe ese elemento, sale un error de tipo key xd
# # colores.remove("cian")

# #? para quitar un elemento pero tomar si es que no existe y no truene se usa discard
# colores.discard("cian")

# if "rojo" in colores:
#     print("sista")

# print(len(colores))

#? convertir lista a sets
#? en este caso solo saldra del 1,2,3,4,5 sin duplicados

# numeros = [1,1,2,2,2,3,4,5,5]
# numerosSet = set(numeros)
# print(numerosSet)

# a = {1,2,5}
# b = {5,6}

# #? con los sets se pueden hacer iggualaciones logicas como com probabilidad y estadistica con union, interseccion, entre otros.
# print(a | b)

# #? si no hay interseccion devuelve 'set()'
# print(a & b)

# #? diferencia, depende del orden, no es lo mismo a - b pq esto es la diferencia de lo que esta en b que no esta en a, y b - a es la diferencia de los que 
# #? esta en b pero no en a, dan 2 coas diferentes
# print(b - a)

# #! ejercicio por hacer
# #? El ejercicio 4 (el último del día 2) era: crea un set con las categorías únicas que hay en productos.

productos = [
    {"nombre": "laptop", "precio": 15000, "categoria": "tech"},
    {"nombre": "silla", "precio": 800, "categoria": "muebles"},
    {"nombre": "mouse", "precio": 300, "categoria": "tech"},
    {"nombre": "mesa", "precio": 1200, "categoria": "muebles"},
]


categoriasSet = set()
for pr in productos:
    categoriasSet.add(pr["categoria"])

print(categoriasSet)
    