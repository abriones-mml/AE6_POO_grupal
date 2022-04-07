from sucursal_class import Sucursal


class Vendedor:
    
    def __init__(self, run, nombre, apellido, seccion, comision=0, empleado_de_mes=0, ventas = 0): 
        self.run = run
        self.nombre = nombre
        self.apellido = apellido
        self.seccion= seccion
        self.__comision=comision
        self.empleado_del_mes=empleado_de_mes
        self.ventas = ventas

    def setComision(self,venta):
        self.__comision+=venta*0.05/100
        print(f"Comision por la compra realizada de {venta*0.5/100}")
        print(f"Usted lleva acumulado {self.__comision}.")
        return self.__comision

    def add_ventas(self):
        self.ventas += 1

    def vender(self, prod, cli, unidades, despacho):   
        
        valor_con_iva = unidades*int(prod.valor_neto*1.19)  #   valor a pagar x el cliente
        comision = int(unidades*prod.valor_neto*0.5/100)  #comisión que se lleva el vendedor
        
        if despacho:
            envio = 5000
        else:
            envio = 0
        
        a_cobrar = valor_con_iva + envio
        
        if prod.stock - unidades >= 0 and cli._Cliente__saldo >= a_cobrar:      # Compra autorizada
            
            print(f"Compra Autorizada\n\nUsted venderá {unidades} unidad(es) de {prod.stock} del producto {prod.nombre}")
            prod.stock -= unidades
            print(f"El nuevo stock de {prod.nombre} es de {prod.stock} unidad(es).")
            print(f"\nEl cliente {cli.nombre} {cli.apellido} debe cancelar un total de ${a_cobrar}")         
            print(f"\nUsted recibirá una comision de ${comision} por esta compra.")
            self.__comision += comision
            self.add_ventas()
            print(f"Usted lleva acumulado ${self.__comision} en {self.ventas} venta(s).")
            
            if despacho:
                cli._Cliente__saldo -= valor_con_iva + 5000 #se hace el descuento del saldo incluyendo despacho
            else:
                cli._Cliente__saldo -= valor_con_iva
            emitir_orden = 1
        
        else:
            if cli._Cliente__saldo < a_cobrar:
                print("Saldo insuficiente del cliente.")
            if prod.stock - unidades <= 0:
                print("Stock del producto insuficiente.")
            if prod.stock == 0:
                print("Stock del producto agotado.")
            print("Compra Rechazada.")
            emitir_orden = 0
        
        return emitir_orden
        
    def __str__(self):
        return "{:<15}{:15}{:15}{:11}{:8}{:10}".format(self.run, self.nombre.capitalize(), self.apellido.capitalize(), self.seccion.capitalize(), self.ventas, self.__comision)