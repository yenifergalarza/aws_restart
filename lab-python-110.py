#creacion de variable 
myString = "This is a string."
print(myString)


# impresion type
print( type(myString))

# usando str()
print(myString + " is of the data type " + str(type(myString)))

#trabajando concatenando cadenas

firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print( thirdString)

# trabajando con cadenas de entrada

name = input( "what is your name? ")
print(name)


# como dar formato de cadenas de salidas

color = input( "what is your favorite color? ")
animal = input ("what is your favorite animal? ")

# multiples variables en cadena 
print("{}, you like a {} {}!".format(name,color,animal))