cantidad=[]
producto=[]
precio=[]
flag=True

while True:
  print('''
    1. Añadir productos.
    2. Buscar producto.
    3.'inventario.
    4.Vear productos.''')
  
  respuesta=int(input('Ingrese su opcion: '))

  if respuesta==1:
    nombre=str(input('Ingrece el nombre de si producto: '))
    unidades=int(input('Ingrese la cantidad del producto: '))
    costo=float(input('Precio de producto: '))

    cantidad.append(unidades)
    producto.append(nombre)
    precio.append(costo)
  
  elif respuesta == 2:
    buscar =input('producto a buscar: ')
    posicion= nombre.index(buscar)
    print(f'La nombre del producto es: {producto[posicion]}')
    print(f'Producto en stock: {cantidad[posicion]}')
    print(f'El precio del producto es: ${precio[posicion]}')   