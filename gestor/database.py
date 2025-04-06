class cliente:
    def __init__ (self, dni, nombre, apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f"({self.dni}, {self.nombre}, {self.apellido})"
    
class clientes:
    lista_clientes = []
    def buscar(dni):
        for cliente in clientes.lista_clientes:
            if cliente.dni == dni:
                return cliente
    
    def crear (dni, nombre, apellido):
        cliente = cliente(dni,nombre,apellido)
        clientes.lista.append(cliente)
        return cliente
    
    def modificar(dni, nombre, apellido):
        for i, cliente in enumerate (clientes.lista_clientes):
            if cliente.dni == dni:
                clientes.lista_clientes[i].nombre = nombre
                clientes.lista_clientes[i].apellido = apellido
                return clientes.lista_clientes[i]
            
    def borrar(dni):
        for i, cliente in enumerate (clientes.lista_clientes):
            if cliente.dni == dni:
                cliente = clientes.lista_clientes.pop (i)
                return cliente

