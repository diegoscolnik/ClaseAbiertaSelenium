#Práctica II - Autos

for i in range(5):

    #Variable precio acumulativa

    precio = 0
    
    #Datos Cliente
    nombre = input('Indique su nombre: ')
    apellido = input('Indique su apellido: ')

    #Defino precio por marca
    marca = input('Indique marca de auto entre Ford, Chevrolet o Fiat: ')

    if(marca == 'Ford'):
        precio = precio + 100000
    elif(marca == 'Chevrolet'):
        precio = precio + 120000
    elif(marca == 'Fiat'):
        precio = precio + 80000
    
    #Defino rpecio por agregado de puertas

    puertas = input('Indique cantidad de puertas entre 0, 2, 4 o 5: ')

    if(puertas == '2'):
        precio = precio + 50000
    elif(puertas == '4'):
        precio = precio + 65000
    elif(puertas == '5'):
        precio = precio + 78000

    #Defino precio por color

    color = input('Indique color del auto entre Blanco, Azul o Negro: ')

    if(color == 'Blanco'):
        precio = precio + 10000
    elif(color == 'Azul'):
        precio = precio + 20000
    elif(color == 'Negro'):
        precio = precio + 30000
    
    print('La persona: ' + nombre + ' ' + apellido + ' compró un auto marca ' + marca + ' de ' + puertas + ' puertas y de color ' + color + ' con un precio de $' + str(precio)) 