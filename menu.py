from datos import *
from funciones import *

while True:
    limpiar()
    print("<<<<<< Menú Principal >>>>>>\n")
    print("[1] Bodegas.")
    print("[2] Ventas.")
    print("[3] Clientes.")
    print("[4] Salir.")
    
    op = escoger_opcion_menu(1,4)
    
    if op == 1:
        
        while True:
            limpiar()
            print("<<<<<< Bodegas >>>>>>\n")
            print("[1] Gestión de Bodega Principal.")
            print("[2] Gestión de Sucursal.")
            print("[3] Ver Proveedores.")
            print("[4] Ver Productos.")
            print("[5] Volver al Menú Principal.")
        
            op1 = escoger_opcion_menu(1,5)
        
            # 1.1 Bodega principal
            if op1 == 1:
                limpiar()
                print("<<<<<< Bodega Principal >>>>>>\n")
                print("[1] Ver Bodega Principal.")
                print("[2] Despachar productos a Sucursal.")
                print("[3] Abastecer productos.")
                print("[4] Volver al Menú de Bodegas.")
        
                op11 = escoger_opcion_menu(1,4)
                
                # 1.1.1 Estado Bodega Principal
                if op11 == 1:
                    limpiar()
                    listprod = [0]*len(productos)
                    for i in range(len(productos)):
                        listprod[i] = productos[str(i+1)].nombre.capitalize()
                    print("       >>> Bodega Principal <<<")
                    print("{:<5}{:25}{:6}".format("ID", "Producto", "Stock"))
                    print("="*40)
                    bodega.mostrar_stock(listprod)
                    input()
                
                # 1.1.2 Despachar a sucursal
                if op11 == 2:
                    limpiar()
                    print("Productos a despachar:\n")
                    for key in productos:
                        print(f"[{key}]\t{productos[key].nombre.capitalize()}")
                    
                    p = str(escoger_opcion_menu(1,len(productos)))
                    
                    while True:
                        try:
                            n = int(input(f"\nIngrese número de unidades de {productos[p].nombre.capitalize()} (Stock: {productos[p].stock}) a despachar: "))
                            if n >0:
                                break
                            else:
                                print(f"Ingrese un número mayor a 0")
                        except ValueError:
                            print("Ingrese un número!")    
                                                            
                    bodega.despachar_producto(p, n, sucursal)
                    productos[p].stock = sucursal.stock[p]
                    input()

                # 1.1.3 Abastecer bodega
                if op11 == 3:
                    limpiar()
                    print("Productos a abastecer:\n")
                    for key in productos:
                        print(f"[{key}]\t{productos[key].nombre.capitalize()}")
                    p = str(escoger_opcion_menu(1,len(productos)))
                    
                    while True:
                        try:
                            n = int(input(f"\nIngrese número de unidades de {productos[p].nombre.capitalize()} a abastecer: "))
                            if n >0:
                                break
                            else:
                                print(f"Ingrese un número mayor a 0")
                        except ValueError:
                            print("Ingrese un número!")    
                    
                    bodega.recepcionar_producto(p, n)
                    input()
        
                if op11 == 4:
                    break
            
            # 1.2 Sucursal   
            elif op1 == 2:
                limpiar()
                print("<<<<<< Sucursal >>>>>>\n")
                print("[1] Ver Sucursal.")
                print("[2] Despachar productos a Bodega Principal.")
                print("[3] Reponer stock.")
                print("[4] Volver al Menú de Bodegas.")
            
                op12 = escoger_opcion_menu(1,4)
                
                # 1.2.1 Ver Sucursal == Ver stock productos
                if op12 == 1:
                    limpiar()
                    listprod = [0]*len(productos)
                    for i in range(len(productos)):
                        listprod[i] = productos[str(i+1)].nombre.capitalize()
                    print("       >>> Sucursal <<<")
                    print("{:<5}{:25}{:6}".format("ID", "Producto", "Stock"))
                    print("="*40)
                    sucursal.mostrar_stock(listprod)
                    input()
                
                # 1.2.2 Despachar a Bodega   
                if op12 == 2:
                    limpiar()
                    print("Productos a despachar:\n")
                    for key in productos:
                        print(f"[{key}]\t{productos[key].nombre.capitalize()}")
                    p = str(escoger_opcion_menu(1,len(productos)))
                    
                    while True:
                        try:
                            n = int(input(f"\nIngrese número de unidades de {productos[p].nombre.capitalize()} a despachar: "))
                            if n >0:
                                break
                            else:
                                print(f"Ingrese un número mayor a 0")
                        except ValueError:
                            print("Ingrese un número!")    
                    
                    sucursal.despachar_producto(p, n, bodega)
                    productos[p].stock = sucursal.stock[p]
                    input()
                
                # 1.2.3 Reponer stock
                if op12 == 3:
                    limpiar()
                    print("Productos para añadir stock de unidades:\n")
                    for key in productos:
                        print(f"[{key}]\t{productos[key].nombre.capitalize()}")
                    p = str(escoger_opcion_menu(1,len(productos)))
                    
                    while True:
                        try:
                            n = int(input(f"\nIngrese número de unidades de {productos[p].nombre.capitalize()} a abastecer: "))
                            if n >0:
                                break
                            else:
                                print(f"Ingrese un número mayor a 0")
                        except ValueError:
                            print("Ingrese un número!")    
                
                    bodega.despachar_producto(p, n, sucursal)
                    productos[p].stock = sucursal.stock[p]
                    input()
                
                if op12 == 4:
                    break

            # 1.3 Ver proveedores
            elif op1 == 3:
                limpiar()
                print("Nuestros proveedores:\n")
                print("{:15}{:25}{:25}{:15}{:15}".format("RUN", "Nombre", "Razón Social", "País", "Personalidad"))
                print("="*93)
                for key in proveedores:
                    print(proveedores[key])
                input("\n")
            
            # 1.4 Ver info de productos    
            elif op1 == 4:
                limpiar()
                print("Nuestros productos:\n")
                print('{:15}{:25}{:18}{:11}{:15}'.format("SKU", "Nombre", "Categoría", "Stock", "Valor neto (CLP)"))
                print("="*90)
                for key in productos:
                    print(productos[key])
                input("\n")
                
            elif op1 == 5:
                break
        
    # Menú Ventas    
    if op == 2:
        
        while True:
            limpiar()
            print("<<<<<< Ventas >>>>>>\n")
            print("[1] Ver Vendedores.")
            print("[2] Realizar Venta.")
            print("[3] Volver al Menú Principal.")
        
            op2 = escoger_opcion_menu(1,3)

            # 2.1 Info vendedores
            if op2 == 1:
                limpiar()
                print("Equipo de vendedores:\n")
                print("{:<15}{:15}{:15}{:15}{:8}{:15}".format("RUN", "Nombre", "Apellido", "Sección", "Ventas", "Comisión (CLP)"))
                print("="*85)
                for key in vendedores:
                    print(vendedores[key])
                input("\n")
            
            # 2.3 Vender
            elif op2 == 2:
                limpiar()
                print("Vendedores:\n")
                for key in vendedores:
                    print(f"[{key}]\t{vendedores[key].nombre} {vendedores[key].apellido}")
                while True:
                    try:
                        v = input("\nSeleccione Vendedor: ")
                        if v in vendedores:
                            break
                        else:
                            print(f"Ingrese un número en el rango 1-{len(vendedores)}")
                    except ValueError:
                        print("Ingrese un número!")    
                
                limpiar()
                print("Cliente:\n")
                for key in clientes:
                    print(f"[{key}]\t{clientes[key].nombre} {clientes[key].apellido}")
                
                while True:
                    try:
                        c = input("\nSeleccione Cliente para venta: ")
                        if c in clientes:
                            break
                        else:
                            print(f"Ingrese un número en el rango 1-{len(clientes)}")
                    except ValueError:
                        print("Ingrese un número!")    
                limpiar()
                print("Productos:\n")
                for key in productos:
                    print("{:3}{:30}{:10}".format(key, productos[key].nombre.capitalize(), productos[key].valor_neto))
                
                while True:
                    try:
                        p = input(f"\nSeleccione producto para venta (saldo del cliente {clientes[c].nombre.capitalize()} {clientes[c].apellido.capitalize()}: ${clientes[c]._Cliente__saldo}): ")
                        if p in productos:
                            break
                        else:
                            print(f"Ingrese un número en el rango 1-{len(productos)}")
                    except ValueError:
                        print("Ingrese un número!")    

                while True:
                    try:
                        u = int(input(f"¿Cuántas unidades de {productos[p].nombre} venderá? (Stock actual: {productos[p].stock} unidades): "))
                        if u >0:
                            break
                        else:
                            print(f"Ingrese un número mayor a 0")
                    except ValueError:
                        print("Ingrese un número!")    
                
                limpiar()
                
                while True:   
                    try:
                        despacho = int(input("Requiere despacho del producto? (0: No  1: Si): "))
                        if despacho == 0 or despacho == 1:
                            break
                        else:
                            print(f"Ingrese una de las dos opciones (0 ó 1).")
                    except ValueError:
                        print("Ingrese un número!")    
                limpiar()
                emitir_orden = vendedores[v].vender(productos[p], clientes[c], u, despacho)
                b[p]-=u
                input()
                
                if emitir_orden:
                    limpiar()
                    orden = OrdendeCompra(ventas, productos[p], despacho)
                    orden.mostrar_orden(productos[p], clientes[c], vendedores[v], u)
                    ventas += 1
                    input()
                
                if productos[p].stock <50:
                    limpiar()
                    print(f"Stock del producto {productos[p].nombre} es de {productos[p].stock} unidades, Solicitando reposición de stock . . .")
                    bodega.despachar_producto(p, 300, sucursal)        
                    print(f"El nuevo stock de {productos[p].nombre} es de {sucursal.stock[p]} unidad(es).")            
            
                    input()
                
            elif op2 == 3:
                break
            
    if op == 3:
        
        while True:
            limpiar()
            print("<<<<<< Clientes >>>>>>\n")
            print("[1] Ver Clientes.")
            print("[2] Volver al Menú Principal.")

            op3 = escoger_opcion_menu(1,2)

            if op3 == 1:
                limpiar()
                print("Clientes registrados:\n")
                print("{:4}{:15}{:18}{:16}{:19}{:15}".format("ID", "Nombre", "Apellido", "E-Mail", "Fecha Registro", "Saldo [CLP]"))
                print("="*90)
                for key in clientes:
                    print(clientes[key])
                input("\n")
                
            elif op3 == 2:
                break

    if op == 4:
        break
limpiar()
print("Que tenga una buena jornada!.\n")
#'''