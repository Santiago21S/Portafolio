import djitellopy
from djitellopy import Tello

class Tello_espanol(Tello):
    def conectar(self):
        self.connect()
    
    def despegar(self):
        self.takeoff()

    def mover(self, dire, dist):
        if dire == "arriba":
            self.move_up(dist)   
        elif dire == "abajo":    
            self.move_down(dist)   
        elif dire == "adelante":
            self.move_forward(dist)   
        elif dire == "atras":
            self.move_back(dist)   
        elif dire == "izquierda":
            self.move_left(dist)   
        elif dire == "derecha":
            self.move_right(dist)
        else:
            print("DIRECCION NO VALIDA. INTENTA DE NUEVO")

    def rotar_a_favor(self, angulo):
        self.rotate_clockwise(angulo)

    def rotar_en_contra(self, angulo):
        self.rotate_counter_clockwise(angulo)
    
    def aterrizar(self):
        self.land()

    def ver_bateria(self):
        print(f"Batería: {self.get_battery()}%")
    
    def desconectar(self):
        self.end()
