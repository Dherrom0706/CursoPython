#El doble ** funciona para elevar un numero a otro en este caso 2 a 3
exponente = 2**3
print(exponente)

#Como no hay tipos para las variables, esto muestra decimales, si queremos una division que devuelva solo el valor de la parte entera
#tendremos que usar // ---------> 9//2 esto daria 4 y no 4.5
division = 9/2
print(division)
print(type(division)) #Esto nos devuelve el tipo que es la variable en ese momento, despues sera un string
#En este ejemplo se ha cambiado el tipo de la variable simplemente cambiando lo que contiene, en este caso es una cadena y contenia un int
division = "Hola"
print(division)
print(type(division))

#El poner una variable con tres """ es para indicar que van a haber saltos de linea
mensaje = """Esto es un mensaje
con tres 
saltos de linea"""
print(mensaje)