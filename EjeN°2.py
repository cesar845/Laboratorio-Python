import os
os.system("cls")

var_totalFlt = 0
var_tabletasInt = 1200000
var_televisoresInt = 1900000
var_videobeamInt = 800000
var_computadoresInt = 2600000

var_nombreStr = input('Nombre del comprador -> ')
var_contactoStr = input('Contacto del comprador -> ')
var_direccionStr = input('Direccion del comprador -> ')
var_presupuestoFlt = float(input('Presupuesto -> '))
var_controlBln = True
while var_controlBln == True:
    import os
    os.system("cls")
    var_opcionStr = int(input('<<< MENU DE OPCIONES >>>\n\n1. Tabletas\n2. Televisores\n3. Videoeam\n4. Computadores\n5. Facturar\n-> '))
    if var_opcionStr >= 1 and var_opcionStr <= 4:
        var_cantidadInt = int(input('Cantidad -> '))
    if var_opcionStr == 1:
        var_totalFlt += (var_cantidadInt * var_tabletasInt)
    if var_opcionStr == 2:
        var_totalFlt += (var_cantidadInt * var_televisoresInt)
    if var_opcionStr == 3:
        var_totalFlt += (var_cantidadInt * var_videobeamInt)
    if var_opcionStr == 4:
        var_totalFlt += (var_cantidadInt * var_computadoresInt)

    if var_opcionStr == 5:
        print('El total a pagar es $', var_totalFlt)
        if var_presupuestoFlt >= var_totalFlt:
            print('Gracias por su compra')
        else:
            print('No tiene suficiente saldo')
        var_controlBln = False