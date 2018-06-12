#!/usr/bin/python3
class Gato:
    def crear(self, nombre, peso, raza, color, castrado):
        self.nombre = nombre
        self.peso = peso
        self.raza = raza
        self.color = color
        self.castrado = castrado

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getPeso(self):
        return self.peso

    def setPeso(self, peso):
        self.peso = peso

    def getRaza(self):
        return self.raza

    def setRaza(self, raza):
        self.raza = raza

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def getCastrado(self):
        return self.castrado

    def setCastrado(self, castrado):
        self.castrado = castrado
