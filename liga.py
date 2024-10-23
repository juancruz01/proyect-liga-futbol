import random

#equipos
class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntos = 0
        self.goles_a_favor = 0
        self.goles_en_contra = 0

    #metodos para modificar
    def puntos_update(self, goles_favor , goles_contra):
        if goles_favor > goles_contra:
            self.puntos += 3
        elif goles_favor == goles_contra:
            self.puntos += 1
        self.goles_a_favor += goles_favor
        self.goles_en_contra += goles_contra


#partidos

class Partido:
    def __init__(self, equipo1, equipo2):
        self.equipo1 = equipo1
        self.equipo2 = equipo2

    def jugar(self):
        goles_equipo1 = random.randint(0,7) 
        goles_equipo2 = random.randint(0,7)
        self.equipo1.puntos_update(goles_equipo1, goles_equipo2)
        self.equipo2.puntos_update(goles_equipo2, goles_equipo1)
        print(f"{self.equipo1.nombre} {goles_equipo1} - {self.equipo2.nombre} {goles_equipo2} ")



#liga

class Liga:
    def __init__(self, equipos):
        self.equipos = equipos

    def todos_contra_todos(self):
        for i in range(len(self.equipos)):
            for j in range(i + 1, len(self.equipos)):
                partido = Partido(self.equipos[i], equipos[j]) 
                partido.jugar()
        
    def tabla_posiciones(self):
        self.equipos.sort(key=lambda x : x.puntos, reverse=True)
        print("Tabla de Posicione: ")
        for equipo in self.equipos:
            print(f"{equipo.nombre}: {equipo.puntos} puntos / GF = {equipo.goles_a_favor} GC = {equipo.goles_en_contra}")

river = Equipo("River")
manchester_city = Equipo("Manchester City")
boca = Equipo("Boca Juniors")
claypole = Equipo("Claypole")
santa_clara = Equipo("Santa Clara")


equipos = [river, manchester_city, boca, claypole, santa_clara]

liga = Liga(equipos)
liga.todos_contra_todos()
print("-----------------------------")
liga.tabla_posiciones()