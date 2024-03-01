import os
codigoInt = int(input('Codigo -> '))
nombreStr = input('Nombre -> ')
existenciasInt = 0
controlBln = True
while controlBln == True:
    os.system ('cls')
    print('Codigo: ', codigoInt, '\nNombre: ', nombreStr,'\nExistecias: ', existenciasInt)
    opcionStr = input('1. Compras\n2. Ventas\n3. Reportes\n-> ')
    cantidadInt = int(input('Cantidad -> '))
    if opcionStr == '1':
        existenciasInt += cantidadInt
    if opcionStr == '2':
        if existenciasInt <= cantidadInt:
            existenciasInt -= cantidadInt
        else:
            print('No hay suficientes existencias para realizar la venta.') 
    if opcionStr == '3':
        print('Cantidad actual de inventario:', existenciasInt)
    if opcionStr == '4':
        controlBln = False