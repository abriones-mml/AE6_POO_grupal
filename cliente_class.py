class Cliente:
    
    def __init__(self, id, nombre, apellido, correo, fecha, saldo, cuenta=0):   #cuenta esl el argumento opcional del abp2
        self.id_cliente = id
        self.nombre = nombre
        self.apellido = apellido
        self.correo= correo
        self.fecha_de_registro= fecha
        self.__saldo= saldo
        self.cuenta = cuenta
    
    # Metodo para acceder al saldo del cliente
    def getSaldo(self):
        return int(self.__saldo)

    # Metodo para agregar saldo al Cliente
    def setSaldo_mas(self,saldo):
        self.__saldo+=saldo
    
    # Metodo para descontar saldo al Cliente
    def setSaldo_menos(self, cuenta):
        self.__saldo-=cuenta
    
    # Metodo para mostrar saldo
    def mostrar_saldo(self):
        print("\nEl cliente :", self.nombre, self.apellido, "tiene un saldo de $", self.__saldo)
        
    def __str__(self):
        return "{:<4}{:15}{:15}{:20}{:11}{:15}".format(self.id_cliente, self.nombre, self.apellido, self.correo, self.fecha_de_registro, self.__saldo)
        
"""
#Metodo para mostrar Id de todos los clientes
    def mostrar_id():   #NOT WORK
        print("Los clientes registrados son los siguientes:\n")
        print('{:15}{:15}'.format("Id_cliente", "Nombre"))
        print("*"*30)
        for key in (clientes):
            print('{:<15}{:<15}'.format(clientes[key].id_cliente, clientes[key].nombre))
#Metodo para mostrar los saldos de todos los clientes
    def mostrar_saldos():   #NOT WORK
        print("Los clientes registrados son los siguientes:\n")
        print('{:15}{:15}{:15}{:15}'.format("Id_cliente", "Nombre", "Apellido", "Saldo"))
        print("*"*60)
        for key in clientes:
            print('{:<15}{:<15}{:<15}{:<15}'.format(clientes[key].id_cliente, clientes[key].nombre, clientes[key].apellido, clientes[key].__saldo))
"""


"""
cli1 = Cliente(1, "diego", "gonzalez", "asd@as.com", "23/23/21", "valparaiso")
clientes={"1":cli1}


cli1.setSaldo1(90000)
#print(cli1.nombre)
#cli1.getSaldo()

#Creacion de Clientes:
liliana= Clientes(1,"Liliana","Garmendia","liligc@gmail.com","10/02/2021", 20000)
clara=Clientes(2,"Clara", "Campos", "clara@gmail.com", "10/01/2019", 40000)
antonia=Clientes(3,"Antonia", "Garmendia", "anto@gmail.com", "10/01/2022", 10000)
valentina=Clientes(4,"Valentina", "Pasten", "vale@gmail.com", "20/01/2018", 50000)
constanza=Clientes(5,"Constanza", "Campos", "cony@gmail.com", "05/01/2020", 30000)
#Creación de un diccionario con los clientes
clientes={"1":liliana,"2":clara, "3":antonia, "4":valentina, "5":constanza}

"""