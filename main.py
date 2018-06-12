#!/usr/bin/python3
from metodos import *
import re


recuadro("Bienvenido al gestor de gatos")
incorrecto = True
lista = []  # donde se guardaran los gatos
lista = cargarLista(lista)
while incorrecto:
    eleccion = input(
        "Elija que desea realizar:\n\t*Listar gatos\n\t*Añadir gato\n\t*Modificar gato\n\t*Borrar gato\n\t*Guardar lista\n\t*Salir\n")
    if eleccion.isalpha():
        eleccion.lower()
        if re.search("salir", eleccion):
            incorrecto = False
            recuadro("Que pase un buen dia!")
        elif re.search("listar", eleccion):
            listarGato(lista)
        elif re.search("añadir", eleccion):
            lista = creaGato(lista)
        elif re.search("modificar", eleccion):
            lista = modificaGato(lista)
        elif re.search("borrar", eleccion):
            lista = borraGato(lista)
        elif re.search("guardar", eleccion):
            guardaLista(lista)
        else:
            print("Opción incorrecta")
    else:
        print("Introduccion incorrecta")
