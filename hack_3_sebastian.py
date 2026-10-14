class CajaFuerte:
    def __init__(self, password):
        self.password = password
        self.open = False
        self.fails = 0
        self.bloqued = False
    def bloquear(self):
        self.open = False
    def desbloquear(self, clave):
        if self.bloqued == True:
            return ("Bloqueo de seguridad activado.")
        if self.password == clave:
            self.open = True
            self.fails = 0
            return ("Acceso concedido")
        else: 
            self.fails = self.fails + 1
        if self.fails >= 3:
            self.bloqued = True
            self.open = False
            return("Acceso denegado, bloqueo de seguridad activado.")
        return ("Clave incorrecta")


