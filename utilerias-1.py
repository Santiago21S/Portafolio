class Utilerias:
    def error(self, msg):
        print(msg)
        input("Oprima [ENTER] para continuar")

    def pide_entero(self, msg, LI, LS):
        while True:
            v = input(msg)
            if not v.isnumeric():
                self.error("Error, valor fuera de rango")
            else:
                v = int(v)
                if v < LI or v > LS:
                    self.error("Error, valor fuera de rango")
                else:
                    return v

    def pide_cadena(self, msg, LI, LS):
        while True:
            cad = input(msg)
            if len(cad) < LI or len(cad) > LS:
                let = f"Error, la cadena debe de tener entre {LI} y {LS} caracteres"
                self.error(let)
            else:
                return cad
            
    def pide_opcion(self, msg, opciones):
        while True:
            op = input(msg).strip().lower()
            if op in opciones:
                return op
            else:
                self.error("Opción no válida. Intenta de nuevo.")
