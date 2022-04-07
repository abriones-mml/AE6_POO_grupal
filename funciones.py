import platform
import os

def limpiar():
    sistema = platform.system()
    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")
        
def escoger_opcion_menu(primera, ultima):
    while True:
        try:
            opcion = int(input("\nSeleccione opción: "))
            if opcion in range(primera, ultima+1):
                break
            else:
                print(f"Ingrese un número entero en el rango {primera}-{ultima}")
        except ValueError:
            print("Ingrese un número!")
    return opcion