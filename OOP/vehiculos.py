# Si un def está dentro de una clase se llamaMÉTODO, si está fuera se llama FUNCIÓN


class Vehiculo():
    
    # Constructor: Método donde defino las propiedades de la clase

    def __init__(self, color, marca, velocidad_maxima):
        self.color = color
        self.marca = marca
        self.velocidad_maxima = velocidad_maxima
        self.velocidad_actual = 0
        self.encendido = False

    def encender(self):
        self.encendido = True
        print('Vehículo encendido. El velocimetro muestra ' + str(self.velocidad_actual) + ' km/h')
    
    def apagar(self):
        self.encendido = False  
        print('Vehículo apagado')
    
    def mostrar_velocimetro(self):
        print('La velocidad actual es de ' + str(self.velocidad_actual) + 'km/h' +  ' de ' + str(self.velocidad_maxima) + 'km/h')
    
    def acelerar(self, velocidad):
        if(self.encendido == True):
            if(self.velocidad_actual + velocidad > self.velocidad_maxima):
                self.velocidad_actual = self.velocidad_maxima
            else:
                self.velocidad_actual = self.velocidad_actual + velocidad
        else:
            print('Para acelerar hay que encender el vehículo')
        self.mostrar_velocimetro()
    
    def frenar(self, velocidad):
        if(self.velocidad_actual - velocidad < 0):
            self.velocidad_actual = 0
        else:
            self.velocidad_actual = self.velocidad_actual - velocidad
        self.mostrar_velocimetro()

class Camion(Vehiculo):
    
    def __init__(self, carga_maxima, color, marca, velocidad_maxima):
        self.carga_maxima = carga_maxima
        self.carga_actual = 0
        Vehiculo.__init__(self, color, marca, velocidad_maxima) # Heredo las propiedades de mi clase Padre
    
    def encender(self):
        self.encendido = True
        print('Camión encendido. El velocimetro muestra ' + str(self.velocidad_actual) + ' km/h')

    def apagar(self):
        self.encendido = False  
        print('Camión apagado')
    
    def mostrar_velocimetro(self):
        print('La velocidad actual es de ' + str(self.velocidad_actual) + ' de ' + str(self.velocidad_maxima) + '. Y la carga es ' + str(self.carga_actual))
    
    def cargar(self,cantidad):
        self.carga_actual = self.carga_actual + cantidad


class Automovil(Vehiculo):
    
    def __init__(self, puertas, color, marca, velocidad_maxima):
        self.puertas = puertas
        Vehiculo.__init__(self, color, marca, velocidad_maxima) # Heredo las propiedades de mi clase Padre
    
    def encender(self):
        self.encendido = True
        print('Automovil encendido. El velocimetro muestra ' + str(self.velocidad_actual) + ' km/h')

    def apagar(self):
        self.encendido = False  
        print('Automovil apagado')
    
    def abrir_puertas(self, nro_puertas):
        print('Se abren las puertas')


#Creo mi objeto mi_auto que hereda desde la clase Automovil()

mi_auto = Automovil(4, 'verde', 'Peugeot', 180)

print('Adquirí un auto ' +mi_auto.marca + ' de color ' + mi_auto.color)

mi_auto.encender()
mi_auto.acelerar(20)
mi_auto.acelerar(170)
mi_auto.frenar(5050)
mi_auto.apagar()

#Creo mi objeto mi_camion que hereda desde la clase Camion()

mi_camion = Camion(2000, 'azul', 'Scania', 120)

print('Adquirí un camión ' + mi_camion.marca + ' de color ' + mi_camion.color)

mi_camion.encender()
mi_camion.mostrar_velocimetro()
mi_camion.acelerar(50)
mi_camion.apagar()