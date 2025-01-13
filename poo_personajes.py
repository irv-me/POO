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




miPersonaje = Personaje("EstebanDido",45,50, 1, 100)
miEnemigo = Personaje("Angel",100,100,70,100)

miPersonaje.atacar(miEnemigo)
miEnemigo.atacar(miPersonaje)
# imprimir_atributos(miPersonaje)
# subir_nivel(miPersonaje,10,10,10)
# imprimir_atributos(miPersonaje)
# print(esta_vivo(miPersonaje))
# morir(miPersonaje)
# print(esta_vivo(miPersonaje))

#Modificar valores de los atributos

#Esto es muy similar a como funciona en Roblox (Lua)
# miPersonaje.nombre = "EstebanDido"
# miPersonaje.fuerza = 300
# miPersonaje.inteligencia = -2
# miPersonaje.defensa = 30
# miPersonaje.vida = 2

# print("El nombre de mi personaje es ", miPersonaje.nombre)
# print("La fuerza de mi personaje es ", miPersonaje.fuerza)
# print("La inteligencia de mi personaje es ", miPersonaje.inteligencia)
# print("La defensa de mi personaje es ", miPersonaje.defensa)
# print("La vida de mi personaje es ", miPersonaje.vida)