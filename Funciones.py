#Para definir una funcion seria de la siguiente forma
from tkinter.messagebox import RETRY


def nombre_funcion(parametrosNecesarios):
    var1 = 2
    var2 = 3
    if var1 < var2: 
        #Para concatenar tienen que ser del mismo tipo, asi que convertimos las variables tipo int a str
        print(str(var1)+ ' menor que ' +str(var2))
    else:
        print(str(var1)+ ' mayor que ' +str(var2))
    #Se pueden devolver varios valores de esa forma como si fuese una array
    return var1,var2

print(nombre_funcion("Hola"))