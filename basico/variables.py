def sumar(n1, n2):
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