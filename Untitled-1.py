
class Habitaciones:
    def __init__(self, Numero, Disponibilidad=True):
        self.numero = Numero
        self.disponible = Disponibilidad

    def Cambiar_Disponibilidad(self, Disponible):
        self.disponible = Disponible

class Huespedes:
    def __init__(self, Cedula, Nombre):
        self.cedula = Cedula
        self.nombre = Nombre
        self.Numero_de_habitacion = None

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Lista:
    def __init__(self, cabeza=None):
        self.primero = cabeza

    def Agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.primero
        self.primero = nuevo_nodo

    def Buscar_habitacion(self, valor):
        temporal = self.primero
        while temporal:
            if temporal.valor == valor:
                return temporal
            else:
                temporal = temporal.siguiente
        return None

class Hotel:
    def __init__(self):
        self.Habitaciones = Lista()
        self.Huespedes_Actuales = Lista(cabeza=None)

    def Registrar_Habitacion(self, Numero, Disponible=True):
        habitacion = Habitaciones(Numero, Disponible)
        self.Habitaciones.Agregar(habitacion)

    def Registrar_Huesped(self, Cedula, Nombre):
        huesped = Huespedes(Cedula, Nombre)
        self.Huespedes_Actuales.Agregar(huesped)

    def Asignar_Habitacion(self, Huesped, Numero_de_Habitacion):
        habitacion = self.Habitaciones.Buscar_habitacion(Numero_de_Habitacion)
        if habitacion:
            if habitacion.disponible:
                habitacion.disponible = False
                Huesped.Numero_de_habitacion = Numero_de_Habitacion
                return f"{Huesped.nombre} fue asignado a la habitación {Numero_de_Habitacion}"
            else:
                return f"{Numero_de_Habitacion} esta habitación ya está ocupada..."
        else:
            return "No se encontró ninguna habitación..."


hotel = Hotel()

hotel.Registrar_Habitacion("101")
hotel.Registrar_Habitacion("102")
hotel.Registrar_Habitacion("103")

huesped1 = hotel.Registrar_Huesped("1000000", "Juan")
huesped2 = hotel.Registrar_Huesped("2222222", "Maria")

resultado1 = hotel.Asignar_Habitacion(huesped1, 101)
resultado2 = hotel.Asignar_Habitacion(huesped2, 103)

print(resultado1)
print(resultado2)