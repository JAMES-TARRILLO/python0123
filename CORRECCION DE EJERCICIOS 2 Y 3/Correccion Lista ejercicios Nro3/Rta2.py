
def Respuesta2():
 texto="""
 Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto.
 Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un
 impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos
 y los mezcló de tal manera que logró hacer un libro de textos especimen.
 """
 
 print(f"""PARA EL SIGUIENTE TEXTO:
 {texto}""")
 while True:
     print("""ESCOJA UNA OPCION:
     a) Separar con comillas las palabras del texto 
     b) Concatenar una Lista que contiene las palabras del texto
     c) Cantidad de veces que se repite una palabra en el texto
     d) Ubicar una palabra en el texto
     e) Pasar a mayuscula todo el texto
     f) Pasar a minuscula todo el texto
     g) Salir""")
     
     ColocarOpcion = input("DIGITAR OPCION: ")
     opcion=ColocarOpcion.lower()
     if opcion == 'a':
         a=texto.split(sep=" ")
         print(a,"\n\nCONTINUE")
     elif opcion == 'b':
         a=texto.split(sep=" ")
         b=" ".join(a)
         print(f"""A CONTINUACION LA SIGUIENTE LISTA {a} SE ESTA CONCATENANDO:""")
         print(b,"\n\nCONTINUE")
     elif opcion == 'c':
         c=input("DIGITE LA PALABRA EXACTA: ")
         c1=texto.count(c)
         if c1>0:
             c2=texto.count(c)
             print("LAS  VECES QUE SE REPITE LA PALABRA EN EL TEXTO SON: "+ str(c2)+"\n\nCONTINUE")
         else:
             print("LA PALABRA NO SE ENCUENTRA EN EL TEXTO","\n\nCONTINUE")
     elif opcion =='d':
         d=input("DIGITE LA PALABRA: ")
         d1=texto.find(d)
         if d1>0:
             d2=texto.find(d)
             print("LA PALABRA SE ENCUENTRA EN LA UBICACION "+ str(d2)+"\n\nCONTINUE")
         else:
             print("LA PALABRA NO SE ENCUENTRA EN EL TEXTO","\n\nCONTINUE")
     elif opcion =='e':
         e=texto.upper()
         print(e,"\n\nCONTINUE")
     elif opcion =='f':
         f=texto.lower()
         print(f,"\n\nCONTINUE")
     elif opcion =='g':
         print("¡INTERACCION CULMINADA!")
         break
     else:
         print("OPCION INCORRECTA")
 