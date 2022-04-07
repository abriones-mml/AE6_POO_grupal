class OrdendeCompra():
    
    def __init__(self, id_ordencompra, producto, despacho):
        self.id_ordencompra = id_ordencompra
        self.producto = producto
        self.despacho = despacho
        
    def mostrar_orden(self, producto, cliente, vendedor, unidades):
        
        if self.despacho:
            envio = 5000
        else:
            envio = 0
            
        total = int(1.19*(unidades*producto.valor_neto)) + envio
        print(f"Orden de compra Nº: {self.id_ordencompra}\n")
        print(f"Cliente: {cliente.nombre} {cliente.apellido}\n")
        print(f"Vendedor: {vendedor.nombre} {vendedor.apellido} \n")
        print("Detalles de Compra:\n")
        print("{:17}{:25}{:10}{:22}{:10}".format("Código Producto", "Detalle", "Unidades", "Precio Unitario", "Total"))
        print("="*80)
        print("{:<17}{:28}{:<11}{:<13}{:10}".format(producto.sku, producto.nombre, unidades, producto.valor_neto, unidades*producto.valor_neto))
        print("_"*80)
        print("{:>69}{:10}".format("Subtotal:", unidades*producto.valor_neto))
        print("{:>69}{:10}".format("IVA:", int(0.19*(unidades*producto.valor_neto))))
        print("{:>69}{:10}".format("Despacho:", envio))
        print("{:>80}".format("_"*21))
        print("{:>69}{:10}".format("TOTAL:", total))