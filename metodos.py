#!/usr/bin/python3
import clase
import os.path
import re


# creamos cada gato y se guarda en la lista
def creaGato(lista):
    nombre = validaInput("Nombre")
    peso = validaInput("Peso", 1)
    raza = validaInput("Raza")
    color = validaInput("Color")
    castrado = validaInput("Esterilizado")
    castrado = siNo(castrado)  # asignamos True/False
    gato = clase.Gato()
    gato.crear(nombre, peso, raza, color, castrado)
    lista.append(gato)
    return lista


# comprobamos si dice si o no
def siNo(eleccion):
    if re.search("si?", eleccion):
        eleccion = True
    else:
        eleccion = False
    return eleccion


# validamos cada dato del gato
def validaInput(campo, digito=0):
    dato = ""
    incorrecto = True
    while incorrecto:
        dato = input("{0}?: ".format(campo)).strip()
        if digito == 0:
            if dato.isalpha():
                incorrecto = False
            else:
                print("El valor de {0} es incorrecto".format(campo.lower()))
        else:
            if dato.isdigit():
                incorrecto = False
            else:
                print("El valor de {0} es incorrecto".format(campo.lower()))
    return dato


# modificamos el gato
def modificaGato(lista):
    ids = validaInput("Conoce el id del gato")
    ids = siNo(ids)  # asignamos True/False
    if not id:
        listarGato(lista)
    idmodificar = validaInput("Id", 1)
    try:
        gato = lista[idmodificar]
        print("Id\tNombre\tPeso\tRaza\tColor\tEsterilizado")
        imprimeGato(gato, idmodificar)
        campo = buscaCampo("modificar")
        # modificamos cada campo
        if campo == "todo":
            nombre = validaInput("Nombre")
            peso = validaInput("Peso", 1)
            raza = validaInput("Raza")
            color = validaInput("Color")
            castrado = validaInput("Esterilizado")
            castrado = siNo(castrado)  # asignamos True/False
            nombre = gato.setNombre(nombre)
            peso = gato.setPeso(peso)
            raza = gato.setRaza(raza)
            color = gato.setColor(color)
            castrado = gato.setCastrado(castrado)
        elif campo == "esterilizado":
            castrado = validaInput("Esterilizado")
            castrado = siNo(castrado)  # asignamos True/False
            castrado = gato.setCastrado(castrado)
        elif campo == "peso":
            peso = validaInput("Peso", 1)
            peso = gato.setPeso(peso)
        elif campo == "color":
            color = validaInput("Color")
            color = gato.setColor(color)
        elif campo == "raza":
            raza = validaInput("Raza")
            raza = gato.setRaza(raza)
        elif campo == "nombre":
            nombre = validaInput("Nombre")
            nombre = gato.setNombre(nombre)
        imprimeGato(gato, idmodificar)
    except:
        print("Fallo al introducir el id del gato")


# borramos al gato
def borraGato(lista):
    ids = validaInput("Conoce el id del gato")
    ids = siNo(ids)  # asignamos True/False
    if not id:
        listarGato(lista)
    idborrar = validaInput("Id", 1)
    try:
        print("Id\tNombre\tPeso\tRaza\tColor\tEsterilizado")
        print(lista[idborrar])
        seguro = validaInput("Está seguro")
        seguro = siNo(seguro)  # asignamos True/False
        if seguro:
            lista.pop(idborrar)
    except:
        print("Fallo al introducir el id del gato")


# listamos todos los gatos o por campo
def listarGato(lista):
    campo = buscaCampo("buscar por")
    # separamos en grupos
    if campo == "todo":
        print("Id\tNombre\tPeso\tRaza\tColor\tEsterilizado")
        for x in range(len(lista)):
            gato = lista[x]
            imprimeGato(gato, x)
    elif campo == "esterilizado":
        castrado = validaInput("Esterilizado")
        castrado = siNo(castrado)  # asignamos True/False
        print("Id\tNombre\tPeso\tRaza\tColor\tEsterilizado")
        for x in range(len(lista)):
            gato = lista[x]
            if gato.getCastrado() == castrado:
                imprimeGato(gato, x)
    elif campo == "peso":
        filtro = validaInput(campo, 1)
        print("Id\tNombre\tPeso\tRaza\tColor\tEsterilizado")
        for x in range(len(lista)):
            gato = lista[x]
            if gato.getPeso() == filtro:
                imprimeGato(gato, x)
    else:
        filtro = validaInput(campo)
        print("Id\tNombre\tPeso\tRaza\tColor\tEsterilizado")
        for x in range(len(lista)):
            gato = lista[x]
            if campo == "color":
                if gato.getColor() == filtro:
                    imprimeGato(gato, x)
            elif campo == "raza":
                if gato.getRaza() == filtro:
                    imprimeGato(gato, x)
            elif campo == "nombre":
                if gato.getNombre() == filtro:
                    imprimeGato(gato, x)
    print()


# imprime gato
def imprimeGato(gato, contador):
    nombre = gato.getNombre()
    peso = gato.getPeso()
    raza = gato.getRaza()
    color = gato.getColor()
    castrado = gato.getCastrado()
    if castrado:
        castrado = "Esterilizado"
    else:
        castrado = "No esterilizado"
    print("{0}\t{1}\t{2}\t{3}\t{4}\t{5}".format(
        contador, nombre, peso, raza, color, castrado))


# elegimos un campo a tratar
def buscaCampo(nombre):
    campo = ""
    incorrecto = True
    # preguntamos que quiere listar
    while incorrecto:
        campo = input(
            "Desea {0} nombre, peso, raza, color, esterilizado o todo? ".format(nombre)).strip()
        if campo.isalpha():
            opciones = ["nombre", "peso", "raza",
                        "color", "esterilizado", "todo"]
            for x in opciones:
                if re.search(x, campo):
                    campo = x
                    incorrecto = False
                    break
            if campo not in opciones:
                print("Elección erronea")
        else:
            print("Elección erronea")
    return campo


# guardamos la lista en un archivo
def guardaLista(lista):
    f = open("gatos.txt", "w")
    for gato in lista:
        nombre = gato.getNombre()
        peso = gato.getPeso()
        raza = gato.getRaza()
        color = gato.getColor()
        castrado = gato.getCastrado()
        f.write(nombre + "//" + peso + "//" + raza +
                "//" + color + "//" + str(castrado) + "\n")
    f.close()


# cargamos la lista de un archivo
def cargarLista(lista):
    if os.path.isfile("gatos.txt") == False:
        f = open("gatos.txt", "w")
        f.close()
    f = open("gatos.txt")
    linea = f.readline()
    while linea != "":
        linea = linea.split("//")
        gato = clase.Gato()
        gato.crear(linea[0], linea[1], linea[2], linea[3], linea[4])
        lista.append(gato)
        linea = f.readline()
    f.close()
    return lista


# imprimimos bonito
def recuadro(texto, decoracion1="#", decoracion2="#"):
    tamano = len(texto) + 10
    if len(decoracion1) == 2:
        tamano = int(len(texto) * 0.75)
    print(decoracion1 * tamano)
    print(decoracion2 + "    " + texto + "    " + decoracion2)
    print(decoracion1 * tamano, end="\n\n")
