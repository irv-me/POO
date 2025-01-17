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
        pass


    def imprimir_atributos(self):
        print(self.nombre)
        print("-Fuerza:", self.fuerza)
        print("-Inteligencia:", self.inteligencia)
        print("-Defensa:", self.defensa)
        print("-Vida:", self.vida)


    def subir_nivel(self, inteligencia, fuerza, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa
    #Variable del constructor vacío

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(self.nombre, "Ha muerto")

    def dañar(self, enemigo):
        return self.fuerza - enemigo.defensa

    def atacar(self,enemigo):
        daño = self.dañar(enemigo)
        if daño > 0:
            enemigo.vida = enemigo.vida - daño
            if enemigo.vida > 0:
                print(self.nombre, "ha realizado",daño,"de daño a",enemigo.nombre)
                print("vida de",enemigo.nombre,enemigo.vida)
            else:
                enemigo.morir()
        else:
            print(self.nombre, "no logro hacerle daño a",enemigo.nombre)
            print("vida de",enemigo.nombre,enemigo.vida)

class Guerrero(Personaje):
    #SObrescribir el constructor
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada
    #sobrescribir impresion de atributos

    def imprimir_atributos(self):
         super().imprimir_atributos()
         print("-Espada:", self.espada)

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



#GAME CREAR
# arturoSuarez = Guerrero("Arturo Suárez",12,3000,2,100,0.5)
# arturoSuarez.escoger_navaja()
# gandalf = Mago("Gandalf",12,3000,2,100,0.5)
# gandalf.escoger_navaja()
# miPersonaje = Personaje("EstebanDido",45,50, 1, 100)
# miEnemigo = Personaje("Angel",100,100,70,100)



arturoSuarez = Guerrero("Arturo Suárez",20,15,10,100,5)
gandalf = Mago("Gandalf",20,15,10,100,5)
miPersonaje = Personaje("EstebanDido",20,15,10,100)
miEnemigo = Personaje("Angel",100,100,70,100)

miPersonaje.atacar(arturoSuarez)
arturoSuarez.atacar(gandalf)
gandalf.atacar(miPersonaje)


