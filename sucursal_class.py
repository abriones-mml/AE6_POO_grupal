from bodega_class import BodegaPrincipal

class Sucursal(BodegaPrincipal):
    def __init__(self, direccion, mt2, stock):
        super().__init__(direccion, mt2, stock)
        self.alarma = False

    def __str__(self):
        return f"Datos de sucursal:\n"'Dirección: {:<15} \nmts2: {:<15}'.format(self.direccion, self.mt2)

    def check():        #FUNCION PARA CORROBORAR EL ESTADO DE LA INSTANCIA(ALARMA)
        pass

    def despachar_producto(self, producto_elegido, cantidad, bodega): #Metodo sobrecargado
        
        if self.stock[producto_elegido] >= cantidad:
            print("Producto despachado a bodega")
            self.stock[producto_elegido] = self.stock[producto_elegido]-cantidad
            bodega.stock[producto_elegido] = bodega.stock[producto_elegido]+cantidad
            print(f"El nuevo stock es de {self.stock[producto_elegido]} unidad(es).")
        
        else: 
            print("Despacho rechazado, no hay suficiente stock")

    def recepcionar_producto(self, producto_elegido, cantidad, bodega): #agregue bodega
        super().recepcionar_producto(producto_elegido, cantidad) # aumenta el stock en cantidad
        dif = self.stock[producto_elegido] - 500
        if dif > 0:
            print("ALERTA: stock del producto elegido es mayor a 500 unidades!")
            print(f"Se devolverá(n) {dif} unidad(es) a Bodega Principal.")
            self.stock[producto_elegido] = 500
            bodega.stock[producto_elegido] += cantidad - dif #agregue esta linea
        else:
            bodega.stock[producto_elegido] -= cantidad        
            
    # lo agregue
    def mostrar_stock(self, nombres_productos):
        for i in range(len(self.stock)):
            print("{:<5}{:25}{:6}".format( i+1, nombres_productos[i], self.stock[str(i+1)]))