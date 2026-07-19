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

for pr in productos:
    for n in pr:
        mayorProducto = (f'el producto actual es: {n}')
        print(mayorProducto)
