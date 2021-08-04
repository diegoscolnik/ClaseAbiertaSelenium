def ingresar_numero():
    numero = int(input("Ingrese número: "))
    numero = numero * 30
    return numero

def hacer_algo_con_numeros(a,b):
    return a + b

#mi_numero = ingresar_numero()
#print(mi_numero)

a = 50
b = 80
mi_variable = hacer_algo_con_numeros(a,b)
print(mi_variable)
mi_variable = hacer_algo_con_numeros(30,1000)
print(mi_variable)