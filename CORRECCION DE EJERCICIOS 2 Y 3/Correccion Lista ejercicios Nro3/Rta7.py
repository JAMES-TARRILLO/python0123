def Respuesta7():
 class Producto:
     def __init__(self,nombre,codigo):
         self.nombre=nombre
         self.codigo=codigo
     def __str__(self) -> str:
         return f"El producto contiene los siguientes atributos: {self.nombre} , {self.codigo}.\nprocede de:"
     def paisOrigen(self):
         pais=self.codigo.split(sep='-')
         print(pais[0])
     def NumLote(self):
         lote=self.codigo.split(sep='-')
         print(lote[1])             

 try:
     produc1=Producto('Aceite','CHILE-0054-2023')
     
     print(produc1)
     produc1.paisOrigen()
     print("numero de lote:")
     produc1.NumLote()
      
 except Exception as b:
     print("Error al mostrar los productos")
     print(b) 
 
 
 
