class Producto:
    def __init__(self, sku, nombre, categoria, proveedores, stock, valor_neto, color="", impuesto=1.19):    #color es el argumento opcional del abp2
        self.sku = sku
        self.nombre = nombre
        self.categoria = categoria
        self.proveedores= proveedores
        self.stock= stock
        self.valor_neto= valor_neto
        self.color=color
        self.__impuesto= impuesto
#Metodo para calcular el precio final de compra
    def precio_total(self):
        return int(self.valor_neto+(self.valor_neto*1.19/100))
#Metodo para descontar al stock del producto
    def descontar_stock(self, cantidad):
        if self.stock>=cantidad:
            print(f"Compra Autorizada\nUsted venderá {cantidad} unidades de {self.stock} del producto {self.nombre}")
            self.stock=self.stock-cantidad
            print(f"El nuevo stock de {self.nombre} es de {self.stock} unidad(es).")
        else: 
            print("Compra Rechazada, no queda stock")

    def __str__(self):
        return '{:<15}{:<25}{:<15}{:7}{:>15}'.format(self.sku, self.nombre.capitalize(), self.categoria.title(), self.stock, self.valor_neto)



"""
#Creación de instancias de Productos
zapatillas= Productos(20221, "zapatillas", "calzado", proveedores["1"].razon_social, sucursal.stock["1"], 40000,"blancas")
jeans= Productos(20222, "jeans", "vestuario",proveedores["2"].razon_social , sucursal.stock["2"], 30000, "azules")
audifonos= Productos(20223, "audifonos", "electronica", proveedores["3"].razon_social,sucursal.stock["3"], 30000,"negros")
chocolates= Productos(20224, "bombones de chocolate", "alimentacion", proveedores["4"].razon_social, sucursal.stock["4"], 15000,"oscuro")
vino= Productos(20225, "botella de vino 1.5L","licores", proveedores["5"].razon_social, sucursal.stock["5"], 20000, "tinto")
#Creación de un diccionario con los productos
productos= {"1":zapatillas, "2":jeans, "3":audifonos, "4":chocolates, "5":vino}
"""