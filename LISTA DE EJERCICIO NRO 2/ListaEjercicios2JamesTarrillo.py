print(1)

print("Menú interactivo")
while True:
    print("""Escribe una opción:
    1) Dibujar un cuadrado con *
    2) lista de numeros multipos de 2
    3) lista de alumnos mayores de edad
    4) Salir""")
    
    opcion = input(": ")
    if opcion == '1':
        f=int(input("Coloca un valor menor a 11 para el tamaño: "))
        c=f*3
        if f<11:
            for i in range(1,f+1):
                for l in range(1,c+1):
                    print("*",end="")
                print(" ")
        else:
            print("tamaño incorrecto")
    elif opcion == '2':
        Numeros=int(input("ingresar hasta que numero Iterar: "))
        ListaNumeros=list()
        for i in range(1,Numeros+1):
            if i%2==0:
                ListaNumeros.append(i)
        print("Los siguientes numeros son multiplos de 2:")
        print(ListaNumeros)
    elif opcion == '3':
        BaseAlumnos={"juan":17,"pedro":18,"mateo":25,"jorge":15}
        for i,l in BaseAlumnos.items():
            if l>=18:
                print(i,l)
    elif opcion =='4':
        print("¡Interaccion finalizada!")
        break
    else:
        print("opcion incorrecta, vuelva a intentarlo")


print("""
2""")

Biblioteca={"categorias":{
            "AutoBiografico":{"titulo":"Yo Confieso",
                              "autor":"Mikel Lejarza",
                              "estado":"disponible"},
            "Cientifico":    {"titulo":"Sapiens",
                              "autor":"Yuval Noah",
                              "estado":"disponible"},
            "AutoAyuda":     {"titulo":"La Isla",
                              "autor":"Aldous Huxley",
                              "estado":"disponible"},
            "Usuarios":     ["B001","B002","B003"]
}                    
}

#Lista de Categorias
categorias=list(Biblioteca["categorias"].keys())
print("Consulta de categorias:")
for i in categorias:
    print(i)

# Nombre libros y autores
categoria=input("Ingrese categoria: ")
for a,b in Biblioteca["categorias"][categoria].items():
    print(a,":", b)

#Cambiar de estado
Respuesta=["si"]
Prestado=input("Se prestara el libro? (si/no): ")
if Prestado in Respuesta:
    UsuarioPrestado=input("ingrese el usuario: ")
    Biblioteca["categorias"][categoria]["estado"]="prestado"+"-"+UsuarioPrestado
    print("Se actualizo estado del libro")
    for k,v in Biblioteca["categorias"][categoria].items():
        print(k,":", v)
else:
    print("fin de la consulta")

#Cambiar de estado
print("Lista de Usuarios actuales:")
print(Biblioteca["categorias"]["Usuarios"])


print("""
3""")

def mayorvalor(a,b):
    if a>b:
        print(a)
    else:
        print(b)
        
valor1=int(input("ingrese primer valor: "))
valor2=int(input("ingrese segundo valor: "))
print("El mayor valor es: ")
mayorvalor(valor1,valor2)


print("""
4""")

import sys
a=sys.argv

def Argumentos(*args):
    for arg in args:
        print(arg)

Argumentos("hola soy","James y tengo",[4,"hermanas y",1,"hermano"],{'Estudios':["universitario","maestria"]})