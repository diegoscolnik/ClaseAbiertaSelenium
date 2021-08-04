#Práctica: Programa de promedios

#Ingresar el nombre y apellido de un alumno y sus notas de matemática, literatura y física.
#Se pide imprimir el nombre, el apellido y el promedio.
#Si el promedio es mayor a 6 entonces debe aparecer un cartel que diga "Aprobado". 
#Caso contrario, si tiene menos de 4 puntos imprimir "Insuficiente" y si tiene entre 4 y 5.99999 imprimir "A recuperatorio".
#En caso de tener 9 puntos o más, imprimir (aparte del aprobado) "Alumno destacado".

#Variables

nombre = 'Diego'
apellido = 'Scolnik'
nota_mat = 10
nota_lit = 10
nota_fis = 10
suma_notas = [nota_mat, nota_lit, nota_fis]

#Función Promedio de Notas

def promedio_de_notas(suma_notas):
    return(sum(suma_notas)/float(len(suma_notas)))

var_promedio = promedio_de_notas(suma_notas)
descripción_alumno = ("El alumno se llama " + nombre + " " + apellido + " y su promedio es de " + str(var_promedio))

#Print Nombre, apellido y promedio

print(descripción_alumno)

#Print resultado de promedio
#Resultados desaprobados

def resultado_alumno(var_promedio):
    if(var_promedio < 4):
        print("Alumno con promedio insuficiente")
    elif(4 <= var_promedio <= 5.99999):
        print("El alumnmo debe ir a recuperatorio")
    elif(var_promedio > 6):
        print("El alumno fue aprobado")
        if(var_promedio >= 9):
            print("Alumno destacado")

resultado_alumno(var_promedio)