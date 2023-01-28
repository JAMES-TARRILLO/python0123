class Autoparte:
    def __init__(self,tipo,subtipo,marca,serie):
        self.tipo=tipo
        self.subtipo=subtipo
        self.marca=marca
        self.serie=serie
    def __str__(self) -> str:
        return f"La autoparte contiene los siguientes atributos: {self.tipo} , {self.subtipo} , {self.marca} ,{self.serie}"

class Catalogo:
    listAutopartes=[]
    def __init__(self,listaAutopartes:list=[]):
        self.listAutopartes=listaAutopartes
    
    def agregar(self,y):
        self.listAutopartes.append(y)
    def verCatalogo(self):
        for x,y in enumerate(self.listAutopartes):
            x+=1
            print(x,y)
try:
    y1=Autoparte('Neumatico','DeInvierno','Michelin','165/70-R14-81T')
    y2=Autoparte('Freno','Disco','BMW','82B0010')
    y3=Autoparte('Filtro','DeAceite','Renault','OC467')

    catalogo=Catalogo()
    catalogo.agregar(y1)
    catalogo.agregar(y2)
    catalogo.agregar(y3)
    catalogo.verCatalogo()


except Exception as b:
    print("Error al crear los productos de las autopartes")
    print(b)