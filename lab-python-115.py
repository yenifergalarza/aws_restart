print("Welcome to Guess the number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")
#importa el modulo random que se usa para generar un numero aleatorio
import random
number = random.randint(1,10)
isGuessRight= False
while isGuessRight != True:
#pide un numero aleatorio
    guess = input("Guess a number between 1 and 10:")
#compara el numero generado con el sumistrado por el usuario
    if int(guess) == number:
#al ser correcto ejecuta estas lineas
        print("You guessed{}. That is correct! You win!".format(guess))
        isGuessRight = True
#al ser incorrecto ejecuta estas lineas
    else:
        print("You guessed{}. Sorry, that isn't it. Try again".format(guess))
