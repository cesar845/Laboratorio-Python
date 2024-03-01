cantidad = int(input('Cantidad de numero que va a digitar -> '))
contador = 0
while (contador < cantidad):
    numero = int(input('Digite un numero -> '))
    if (numero >=10 and numero <=20):
        print('Esta dentro del rango')
    else:
        print('Esta fuera del rango')
    contador = contador + 1