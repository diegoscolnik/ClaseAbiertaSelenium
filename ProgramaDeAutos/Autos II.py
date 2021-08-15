# Práctica III - Autos II

def calcular_precio(marca, puerta, color):
    marcas = {'FORD':100000, 'CHEVROLET':120000, 'FIAT':80000}
    colores = {'BLANCO':10000, 'AZUL':20000, 'NEGRO':30000}
    puertas = {2:50000, 4:65000, 5:78000}
    precio = marcas[marca] + colores[color] + puertas[puerta]
    #if(ventas > 5 and ventas < 11):
    #    precio = precio * 0.9
    #elif(ventas > 10 and ventas < 51):
    #    precio = precio * 0.85
    #elif(ventas > 50):
    #    precio = precio * 0.82
    return precio

print('*********PROGRAMA DE AUTOS*********')
print('Somos vendedores de Ford, Chevrolet y Fiat')
print('Somos lideres del mercadod esde 1940')

mas_clientes = 'si'

ventas = []

marcas = ['FORD', 'CHEVROLET', 'FIAT']
puertas = [2, 4, 5]
colores = ['BLANCO', 'AZUL', 'NEGRO']

while mas_clientes == 'si':
    nombre = input('Ingrese nombre: ')
    apellido = input('Ingrese apellido: ')
    marca = ''
    puerta = 0
    color = ''
    while marca not in marcas:
        marca = input('Ingrese marca de auto: ')
        marca = marca.upper()
    while puerta not in puertas:
        puerta = int(input('Ingrese cantidad de puertas: '))
    while color not in colores:
        color = input('Ingrese color del auto: ')
        color = color.upper()
    #precio = calcular_precio(marca, puerta, color)
    ventas.append({'nombre':nombre, 'apellido':apellido, 'marca':marca, 'puertas':puerta, 'color':color})
    mas_clientes = input('Hay más clientes?: ')

largo = len(ventas)

for i in ventas:
    precio = calcular_precio(marca, puertas, color)
    print('La persona: ' + i['nombre'] + ' ' + i['apellido'] + 
          ' compró un auto marca ' + i['marca'] + ' de ' + str(i['puertas']) + ' puertas y de color ' + i['color'] + ' con un precio de $' + str('precio')) 