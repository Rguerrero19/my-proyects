'''Lista de clientes
Crea un script en python que te permita crear una lista de clientes
guardando informacion como nombre completo y numero de telefono '''

clientes={}
flag=True
from os import system
while flag == True:
    print('\t MENU''\n 1.Guardar cliente nuevo''\n 2.Consultar cleinte')
    opcion=input('Seelccione una opcion de menu: ')
    system('clear')
    if opcion == '1':
        name=str(input('Nombre de el cleinte: '))
        phone=int(input('Numero de telefono de el cliente: '))
        clientes [name]=phone
        print('Cliente guardado con exito')
    elif opcion == '2': 
        print('Consultar cliente')
        client=input('Nombre del cliente: ')
        if client in clientes:
            print(f'Informacion del cliente: {clientes[client]}')
        else:
            print('El cliente no se encuentra en la base de datos')
    elif opcion == '3':
        print('Gracias por su preferencia :)')
        flag = False
    else:
        print('Opcion de menu incorrecta')