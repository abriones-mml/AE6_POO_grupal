class Proveedor:
    
    def __init__(self, rut, nombre, razon, pais, juridica):
        self.rut=rut
        self.nombre_legal=nombre
        self.razon_social=razon
        self.pais=pais
        self.juridica=juridica
    
    # Método para obtener en pantalla un string con los datos del proveedor   
    def __str__(self):
        return "{:15}{:25}{:25}{:15}{:15}".format(self.rut, self.nombre_legal.title(), self.razon_social, self.pais, self.juridica)
        
