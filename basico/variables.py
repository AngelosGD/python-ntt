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
print(frutas.count('apple'))