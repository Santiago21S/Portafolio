import os
import utilerias as ut

class JuegoBN:
    def __init__(self):
        self.util = ut.Utilerias()
        self.file = ""
        self.aciertos = 0
        self.fallos = 0

        print("===========================================================")
        print("BIENVENIDO A BATALLA NAVAL!! Indica el nombre del archivo que deseas cargar :)")
        print("Si quieres iniciar un juego nuevo, por favor presiona [ENTER]")
        print("Recuerda escribir el nombre del archivo sin extensión.")
        print("===========================================================")
        self.file = self.util.pide_cadena("Indica el nombre del archivo: ", 0, 10)
        if len(self.file) == 0:
            self.file = "inicial.csv"
        else:
            self.file += ".csv"

        self.carga_matriz()

    def carga_matriz(self):
        self.matriz = [["V" for _ in range(8)] for _ in range(8)]
        if os.path.exists(self.file):
            with open(self.file, "r") as arch:
                self.matriz = [line.strip().split(",") for line in arch]
            print(f"Juego cargado desde {self.file}")
        else:
            barcos = [(1, 2), (1, 3), (3, 6), (4, 6), (5, 6), (6, 0), (6, 1), (6, 2), (6, 3)]
            for (ren, col) in barcos:
                self.matriz[ren][col] = "B"
            print("Archivo no encontrado. Se ha creado un juego nuevo.")

    def muestra_tablero(self):
        print("   0 1 2 3 4 5 6 7")
        print("  " + ("-" * 17))
        for ren in range(8):
            print(str(ren) + " |", end="")
            for col in range(8):
                if self.matriz[ren][col] == "V" or self.matriz[ren][col] == "B":
                    print(" ", end="|")
                else:
                    print(self.matriz[ren][col], end="|")
            print(" ")
        print("  " + ("-" * 17))
        print("ACIERTOS =", self.aciertos, "FALLOS =", self.fallos)

    def descarga_matriz(self, nuevo_archivo=False):
        if nuevo_archivo:
            nombre_file = self.util.pide_cadena("Indica el nombre del nuevo archivo: ", 1, 10) + ".csv"
        else:
            nombre_file = self.file
        with open(nombre_file, "w") as arch:
            for ren in self.matriz:
                arch.write(",".join(ren) + "\n")
        print(f"Juego guardado en {nombre_file}")

    def tiro(self, ren, col):
        if ren >= 8 or col >= 8:
            texto_panico = """
            PPPPPPP    AAAA   NNN   NNN   IIIII   CCCCCC   OOOOO
            PP   PP  AA   AA  NNNN  NNN    II    CC    CC OO   OO
            PPPPPPP  AAAAAAA  NN NN NNN    II    CC       OO   OO
            PP       AA   AA  NN  NNNNN    II    CC    CC OO   OO
            PP       AA   AA  NN   NNNN   IIIII   CCCCCC   OOOOO
            """
            print(texto_panico)
            opcion = self.util.pide_opcion("¿Deseas guardar la partida en otro archivo? (s/n): ", ["s", "n"])
            if opcion == "s":
                self.descarga_matriz(nuevo_archivo=True)
            else:
                self.descarga_matriz(nuevo_archivo=False)
            return False 
        else:
            if self.matriz[ren][col] == "A" or self.matriz[ren][col] == "X":
                self.util.error("Error, ya existe el tiro previo en esa celda")
            else:
                if self.matriz[ren][col] == "V":
                    self.util.error("Celda vacía, se incrementan los errores")
                    self.fallos += 1
                    self.matriz[ren][col] = "X"
                else:
                    self.util.error("Celda con barco, se incrementan los aciertos")
                    self.aciertos += 1
                    self.matriz[ren][col] = "A"
