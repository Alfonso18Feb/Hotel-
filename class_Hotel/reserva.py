from datetime import date
import Cliente
class reserva():

    '''primero construir clase'''

    def __init__(self, idreserva, fecha_inicio,fecha_fin,cliente,habitacion,estado):
        self.idreserva=idreserva
        self.fecha_inicio=fecha_inicio
        self.fecha_fin=fecha_fin
        self.cliente=cliente
        self.habitacion=habitacion
        self.estado=estado

    '''Luego ponemos los getters en todas las variables'''
    #coje el valor de la variable

    def get_idreserva(self):
        if isinstance(self.idreserva, int):
            if self.idreserva>0:
                return self.idreserva
            else: 
                raise ValueError("numeros positivos")
        else: 
            raise TypeError("El id de la reserva debe ser un numero entero")

    def get_fecha_inicio(self):
        if isinstance(self.fecha_inicio,date):#no puedes coger dias menores que el dia que estamos hoy
            if self.fecha_inicio>=date:
                return self.fecha_inicio
            else:
                raise ValueError("No puedes reservar en dias que ya han pasado")
        else:
            raise TypeError("la fecha debe ser un datetime ")
    
    def get_fecha_fin(self):
        if isinstance(self.fecha_fin,date):#poner que el fin tiene que ser un dia mas que el inicio
            return self.fecha_fin 
        else:
            raise TypeError("la fecha debe ser un datetime ")
    
    def get_cliente(self):
        if isinstance(self.cliente,Cliente.cliente):
            return self.cliente
        else:
            raise TypeError("la fecha debe ser objeto cliente del modulo cliente")

    def get_habitacion(self):
        return self.habitacion

    def get_estado(self):
        return self.estado

    '''Ahorra el setter para las variables que podemos cambia'''

    def set_fecha_inicio(self,fecha_inicio):
        self.fecha_inicio=fecha_inicio

    def set_fecha_fin(self,fecha_fin):
        self.fecha_fin=fecha_fin

    def set_estado(self,estado): #solo un cliente puede reservar la habitacion:'hacemos un eq para ver si ya hay un cliente que ya tienela habitatión'
        self.estado=estado

    '''Ahora los metodos de la clase reserva'''

    def modificar_reserva():#aqui no seria preguntar si informacion bien y cambiar por consola en el def main
        pass
    def Obtener_informacion(self):
        return "Reserva:"+ str(self.idreserva) +"Fecha inicio"+str(self.fecha_inicio) +"Fecha final"+str(self.fecha_fin) +"Cliente:"+str(self.cliente)+"Habitacion:"+str(self.habitacion)+"Estado"+ str(self.estado)

'''Aqui esta las cosas que el usuario puede modificar (prints)'''

def main():
    C1= reserva(1,date(1223,6,1),date(1324,7,1),"Santander","VIP","Ocupado")
    print(C1.Obtener_informacion)

