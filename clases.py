"""Crear una aplicación que permita 
la compra de ticket en un estadio de futbol"""

class Cliente: 
    """Clase Cliente"""
    def __init__(self, cod, nom, ape):
        self.codigo = cod
        self.nombres = nom
        self.apellidos  = ape    

    def __str__(self):
        return f"""Codigo: {self.codigo}
Nombres: {self.nombres}
Apellidos: {self.apellidos}"""

class Cola:
    def __init__(self):
        self.elementos = []

    def agregar(self, elem):
        self.elementos.append(elem)

    def quitar(self):
        try:
           return self.elementos.pop(0)
        except Exception as ex:
           print("Cola vacía...", str(ex))

    def estaVacia(self):
        return self.elementos == []