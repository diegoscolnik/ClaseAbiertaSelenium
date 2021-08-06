#Sacar promedio
def promedio(mate, literatura, fisica):
    return(mate+literatura+fisica/3)

#Imprimir datos
def datos_del_alumno(nombre, apellido, promedio):
    print("El alumno "+nombre+" "+apellido+" tiene como promedio: "+str(prom))

#Ver aprobación de alumno
def estado_aprobacion(prom):
    if(prom > 6):
        print("El alumno aprobó")
        if(prom >= 9):
            print("Alumno destacado")
    elif(prom >= 4):
        print("A recuperatorio")
    else:
        print("Insuficiente")

#Ingreso de datos

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
mate = int(input("Ingrese su nota de matemáticas: "))
literatura = int(input("Ingrese su nota de literatura: "))
fisica = int(input("Ingrese su nota de física: "))

prom = promedio(mate, literatura, fisica)
datos_del_alumno(nombre, apellido, promedio)
estado_aprobacion(prom)





