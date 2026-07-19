""" [def sumar(n1, n2):
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

frutas = ["apple", "manzana","bamama","uvas", "arandano", "manzana", "apple"]

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

#? metodo extend, deja extender o instanciar una lista o tupla a otra xd, aadir esos valores de la lista
# print(frutas.count('apple'))

# frutas2=["apel","carajo", "mexico"]

# frutas.extend(frutas2)
# print(frutas)

#? busca el index del elemento dado, este aso arandano, esta en la pisicion 4 de la lista
# print(frutas.index('arandano'))

#? agrega el elemento dado al indice o posicion proprocionada, en este caso antes arandano era 4, paso a ser 5, y lol 4 xd
# frutas.insert(4, 'lol')
# print(frutas)

#? popea el indice dado, en este cao 4 es arandanos xd pobre arandano ;,v
# frutas.pop(4)

print(frutas)
frutas.remove('uvas')
if(frutas == ValueError):
    print(f'elemento no encoontrado')
else:
    print(frutas)