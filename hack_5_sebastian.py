class correo:
    def __init__(self, destinatario, mensaje):
        self.destinatario = destinatario
        self.mensaje = mensaje
    def enviar(self):
        print("Correo para:", self.destinatario, self.mensaje)

class mensaje_sms:
    def __init__(self, destinatario, mensaje):
        self.destinatario = destinatario
        self.mensaje = mensaje
    def enviar(self):
        print("Sms para:", self.destinatario, self.mensaje)

notificacion_1 = correo("juan@example.com", "ven a recoger tu pedido a la tienda")
notificacion_2 = mensaje_sms("1234567", "Tu pedido esta listo!")

notificaciones = [notificacion_1, notificacion_2]

for notificacion in notificaciones:
    notificacion.enviar()