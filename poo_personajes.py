import sys 

# COLORES
BLACK   = "\033[30m"
RED     = "\033[31m"
GREEN   = "\033[32m"
YELLOW  = "\033[33m"
BLUE    = "\033[34m"
MAGENTA = "\033[35m"
CYAN    = "\033[36m"
RESET = "\033[0m"


#CONSTRUCTOR
class Personaje:
    #Atributos de la clase
    # nombre = "Default"
    # fuerza = 0
    # inteligencia = 0
    # defensa = 0
    # vida = 0
    # pass
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
        self.inventario = {'vida': 0, 'fuerza': 0, 'inteligencia': 0}
        pass


    def imprimir_atributos(self):
        print(YELLOW + self.nombre,"atributos"+ RESET)
        print("-Fuerza:", self.fuerza)
        print("-Inteligencia:", self.inteligencia)
        print("-Defensa:", self.defensa)
        print("-Vida:", self.vida)
        print("-Pociones:",self.inventario)
        print(YELLOW+"------"+ RESET)


    def subir_nivel(self, inteligencia, fuerza, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa
    #Variable del constructor vacío

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(RED + self.nombre, "ha muerto" + RESET)

    def dañar(self, enemigo):
        return self.fuerza - enemigo.defensa

    def atacar(self,enemigo):
        daño = self.dañar(enemigo)
        if hasattr(enemigo, "escudo") and enemigo.escudo > 0:
            daño = self.fuerza # No utilizamos la funcion dañar ya que esta toma en cuenta la defensa. lo que queremos es el daño puro para el escudo.
            if daño < 0: daño = 0
            enemigo.escudo -= daño
        
            if enemigo.escudo > 0: 
                print(GREEN + " ⛨ El escudo de", enemigo.nombre, "lo protegió!, vida del escudo:", YELLOW, enemigo.escudo, RESET)
                daño = 0 
            else:
                print(GREEN + " ⛨El escudo de", enemigo.nombre, "Se ha roto!", YELLOW, "🛡/", RESET)
                daño = (-1 * enemigo.escudo) - enemigo.defensa #Lo que sobra del daño, y lo que va a la vida #Añadimos defensa ya que ahora si estamos dañando al guerrero.

          
        if daño > 0:
            enemigo.vida = enemigo.vida - daño
            if enemigo.vida > 0:
                print(RED + self.nombre, "ha realizado",daño,"de daño a",enemigo.nombre + RESET)
                print("vida de",enemigo.nombre, YELLOW, enemigo.vida,RESET,)
            else:
                enemigo.morir()
        else:
            print(RED + self.nombre, "no logro hacerle daño a",enemigo.nombre + RESET)
            print("vida de",enemigo.nombre,YELLOW, enemigo.vida,RESET)

    def agregar_pocima(self, tipo, cantidad=1):
        if tipo in self.inventario:
            self.inventario[tipo] += cantidad
            print(YELLOW + f"Se han añadido {cantidad} pócima(s) de {tipo} al inventario de {self.nombre}." + RESET)
        else:
            print(RED + f"Tipo de pócima {tipo} no válido." + RESET)

    def usar_pocima(self, tipo):
        if tipo in self.inventario and self.inventario[tipo] > 0:
            if tipo == 'vida':
                self.vida += 50  # Restaura 50 puntos de vida
                print(GREEN + f"☆ {self.nombre} ha usado una pócima de vida y ha recuperado",YELLOW+"50"+GREEN,"puntos de vida!" + RESET)
            elif tipo == 'fuerza':
                self.fuerza = int(self.fuerza * 1.5)  # Aumenta la fuerza en un 50%
                print(GREEN + f"☆ {self.nombre} ha usado una pócima de fuerza y ha aumentado su fuerza en un "+ YELLOW + "50%" + RESET)
            elif tipo == 'inteligencia':
                self.inteligencia = int(self.inteligencia * 1.5)  # Aumenta la inteligencia en un 50%
                print(GREEN + f"☆ {self.nombre} ha usado una pócima de inteligencia y ha aumentado su inteligencia en un "+ YELLOW + "50%" + RESET)
            self.inventario[tipo] -= 1
        else:
            print(f"{self.nombre} no tiene pócimas de {tipo} en su inventario.")

#FUNCIONES
def personajeMasVida(personajes):
    max_vida = max(personajes, key=lambda p: p.vida)
    print(f"El personaje con más vida es {max_vida.nombre} con {max_vida.vida} puntos de vida.")

def sumaInteligencia(personajes):
    total_inteligencia = sum(p.inteligencia for p in personajes)
    print(f"La inteligencia total de los personajes es: {total_inteligencia}")

def personajesVidaMayorA(personajes, valor_vida):
    filtrados = [p for p in personajes if p.vida > valor_vida]
    if filtrados:
        print(f"Los personajes con vida mayor a {valor_vida} son:")
        for p in filtrados:
            print(f"- {p.nombre}: {p.vida} puntos de vida")
    else:
        print(f"No hay personajes con vida mayor a {valor_vida}.")
#CLASES

class Guerrero(Personaje):
    #SObrescribir el constructor
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada,escudo):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada
        self.escudo = escudo * defensa

    #sobrescribir impresion de atributos

    def imprimir_atributos(self):
         super().imprimir_atributos()
         print("-Espada:", self.espada)
         print("-Escudo:", self.escudo)
         print(YELLOW+"------"+ RESET)


    #sobreescribir el calculo del daño
    def dañar(self, enemigo):
        return self.fuerza*self.espada - enemigo.defensa

    def escoger_navaja(self):
        opcion = int(input("Escoge la navaja:\n(1) Navaja suiza, daño 10.\n(2) Navaja pioja, daño 6.\n"))
        if(opcion == 1):
            self.espada = 10
        elif(opcion == 2):
            self.espada = 6
        else:
            print("valor invalido")
            self.escoger_navaja()

class Mago(Personaje):
    #SObrescribir el constructor
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro
    #sobrescribir impresion de atributos

    def imprimir_atributos(self):
         super().imprimir_atributos()
         print("-libro:", self.libro)
         print(YELLOW+"------"+ RESET)

    #sobreescribir el calculo del daño
    def dañar(self, enemigo):
        return self.inteligencia*self.libro - enemigo.defensa

    def escoger_navaja(self):
        opcion = int(input("Escoge el libro:\n(1) El principito, daño 10.\n(2) Crepusculo, daño 6.\n"))
        if(opcion == 1):
            self.libro = 10
        elif(opcion == 2):
            self.libro = 6
        else:
            print("valor invalido")
            self.escoger_navaja()



#PLANTILLA GUERRERO, Guerrero("",0,0,0,0,1,0) Espada si o si tiene que tener uno, si no el multiplicador de daño eliminara el daño por completo
#====|AMBIENTE DE JUEGO|====#
#NOMBRE,nombre, fuerza, inteligencia, defensa, vida,|| arma, escudo
Fulano = Guerrero("Fulano",16,3000,4,100,1,10)
Fulano.agregar_pocima("vida",1)
Fulano.agregar_pocima("fuerza",1)
Fulano.agregar_pocima("inteligencia",1)


Zangano = Personaje("Zangano",16,3000,5,100)


Fulano.atacar(Zangano)
for i in range(5):
    Zangano.atacar(Fulano)

Fulano.imprimir_atributos()
Fulano.usar_pocima("vida")
Fulano.usar_pocima("fuerza")
Fulano.usar_pocima("inteligencia")
Fulano.imprimir_atributos()

for i in range(5):
    Fulano.atacar(Zangano)



#========= archivo :D
# arturoSuarez = Guerrero("Arturo Suárez",12,3000,2,100,0.5)
# arturoSuarez.escoger_navaja()
# gandalf = Mago("Gandalf",12,3000,2,100,0.5)
# gandalf.escoger_navaja()
# miPersonaje = Personaje("EstebanDido",45,50, 1, 100)
# miEnemigo = Personaje("Angel",100,100,70,100)



# arturoSuarez   = Guerrero("Arturo Suárez",20,15,10,100,5)
# gandalf = Mago("Gandalf",20,15,10,100,5)
# miPersonaje = Personaje("EstebanDido",20,15,10,100)
# miEnemigo = Personaje("Angel",100,100,70,100)

# miPersonaje.atacar(arturoSuarez)
# arturoSuarez.atacar(gandalf)
# gandalf.atacar(miPersonaje)

# merlin = Personaje("Merlin",1,5, 1, 100)
# lancerot = Personaje("Lancerot",1,15, 1, 80)
# houdini = Personaje("Houdini",1,15, 1, 100)

# personajes = [merlin, lancerot, houdini]

# personajeMasVida(personajes)

# sumaInteligencia(personajes)

# personajesVidaMayorA(personajes,90)

