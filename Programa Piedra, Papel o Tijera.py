#Programa Piedra Papel o tijera
import random 

opciones = ["piedra","papel","tijera"]
opcionPrograma = random.choice(opciones)

eleccionusuario = input ("Juguemos piedra, papel o tijera, elije una opcion (En minusculas) ")


#Piedra opciones 
if eleccionusuario == "piedra" and opcionPrograma == "piedra":
    print("\nPiedra con Piedra, Fue un empate")

elif eleccionusuario == "papel" and opcionPrograma == "piedra ":
    print("\nPapel vs Piedra, Ganaste! Felicidades")

elif eleccionusuario == "tijera" and opcionPrograma == "piedra":
    print("\nTijera vs Piedra, Perdiste :( ")


#Opciones Papel

elif eleccionusuario == "piedra" and opcionPrograma == "papel":
    print("\nPiedra vs Papel, Perdiste :( ")

elif eleccionusuario == "papel" and opcionPrograma == "papel":
    print("\nPapel vs Papel, es un empate! ")

elif eleccionusuario == "tijera" and opcionPrograma == "papel":
    print("\nTijera vs Papel, Ganaste! Felicidades ")


# Opciones Tijera 

elif eleccionusuario == "piedra" and opcionPrograma == "tijera":
    print("\nPiedra vs Tijera, Ganaste! Felicidades")

elif eleccionusuario == "papel" and opcionPrograma == "tijera":
    print("\nPapel vs Tijera, Perdiste :( ")

elif eleccionusuario == "tijera" and opcionPrograma == "tijera":
    print("\nTijera vs Tijera, es un empate!")