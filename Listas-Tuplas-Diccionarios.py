#Listas (variables con x cantidad de valores asignados, se permite la re asignación de los valores y su ordenamiento)

autos = ['Ford', 'Chevrolet', 'Fiat']
print(autos)
print(autos[2])
print(autos[-1])
print(autos[0:2])
autos.append('Dodge') #Meter en última posición un valor nuevo al array
print(autos)
autos.insert(1, 'Ferrari') #Meter en una posición exacta del array un valor nuevo
print(autos)
del autos[2] #Eliminar un valor de mi array indicando su posición
print(autos)
print(len(autos))
autos[2]='Porsche' #Modificar el valor de un elemento de mi array
print(autos)

if(autos[2] == 'Porsche'):
    print('Todo bien')
else:
    print('Todo mal')

#Tuplas (variables con x cantidad de valores asignados, no se permite la re asignación de los valores y su ordenamiento)

colores = ('Amarillo', 'Azul', 'Verde')
print(colores)
print('Amarillo' in colores) #Verifica si está el valor en la Tupla

if('Amarillo' in colores):
    print('El Amarillo existe')

#Dicionarios (se asignan keys y values para dichos kyes. Se puede reasignar, agregar y elimianr keys y values)

usuario = {'id':1, 'name': 'Pedro', 'age': 37, 'casado': 'True'}
print(usuario['name'])
print(usuario['casado'])
usuario['name'] = 'Nancy Tuplá' #Modifico un value de una key específica
print(usuario)
usuario['apellido'] = 'Algo' #Agrego una key y un value a mi diccionario
print(usuario)
del(usuario['apellido']) #Elimino una Key, y consecuentemente su value, de mi diccionario
print(usuario)

print(usuario.keys()) #Me devuelve las keys de mi diccionario
print(usuario.values()) # Me devuelve los values de mi diccionario


if('id' in usuario):
    print('Tiene id')

usuario.clear() #Limpia mi diccionario
print(usuario)
del usuario #Elimina mi diccionario
print(usuario)