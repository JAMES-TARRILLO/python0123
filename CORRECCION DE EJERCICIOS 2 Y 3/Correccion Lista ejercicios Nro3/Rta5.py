def Respuesta5():
 try:
     def suma_recursiva(n:int):
         if n<1:
             return 0
         else:
             return n + suma_recursiva(n-1)
 
     m=int(input("suma_recursiva - Colocar un numero: "))
     print(suma_recursiva(m))
 
 
     def dividir(a:int,b:int):
         if b<1:
             return "No se puede dividir entre cero"
         else:
             return a//b
 
     m=int(input("Ahora Dividir \nColocar primer numero: "))
     n=int(input("Colocar segundo numero: "))
     print(dividir(m,n))
 
 except:
     print("Ha ocurrido un error, coloca bien el número")
 
 else:
     import os
     CWD=os.getcwd()
     print(f"Current working directory {CWD}")
 
 finally:
     print("Proceso terminado") 
 
 
 