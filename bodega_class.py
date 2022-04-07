class BodegaPrincipal:
    
    def __init__(self, direccion, mt2, stock):
        self.direccion= direccion
        self.mt2=mt2
        self.stock=stock

    def despachar_producto(self, producto_elegido, cantidad, sucursal):
        
        if self.stock[producto_elegido] >= cantidad:
            print("Producto despachado a sucursal")
            self.stock[producto_elegido] = self.stock[producto_elegido]-cantidad
            sucursal.stock[producto_elegido] = sucursal.stock[producto_elegido]+cantidad
            print(f"El nuevo stock del producto en Bodega Principal es de {self.stock[producto_elegido]} unidad(es).")
            print(f"El nuevo stock del producto en Sucursal es de {sucursal.stock[producto_elegido]} unidad(es).")
            
            if sucursal.stock[producto_elegido] > 500:
                print("Alerta!! El stock de unidades del producto es mayor que 500.")
                dif = sucursal.stock[producto_elegido] - 500
                print(f"Se devolverán {dif} unidades desde Sucursal.")
                sucursal.stock[producto_elegido] = 500
                self.stock[producto_elegido] += dif
        
        else: 
            print("Despacho rechazado, no hay suficiente stock en Bodega Principal")

    def recepcionar_producto(self, producto_elegido, cantidad):
            self.stock[producto_elegido]=self.stock[producto_elegido]+cantidad
            print("Producto recepcionado")

    def __str__(self):
        return f"Datos Bodega principal:\n"'Dirección: {:<15} \nmts^2: {:<15}'.format(self.direccion, self.mt2)

    # lo modifique
    def mostrar_stock(self, nombres_productos):
        for i in range(len(self.stock)):
            print("{:<5}{:25}{:6}".format( i+1, nombres_productos[i], self.stock[str(i+1)]))