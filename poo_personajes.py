class Personaje:
    #Atributos de la clase
    # nombre = "Default"
    # fuerza = 0
    # inteligencia = 0
    # defensa = 0
    # vida = 0
    # pass
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__defensa = defensa
        self.__vida = vida
        pass


    def imprimir_atributos(self):
        print(self.__nombre)
        print("-Fuerza:", self.__fuerza)
        print("-Inteligencia:", self.__inteligencia)
        print("-Defensa:", self.__defensa)
        print("-Vida:", self.__vida)


    def subir_nivel(self, inteligencia, fuerza, defensa):
        self.__fuerza = self.__fuerza + fuerza
        self.__inteligencia = self.__inteligencia + inteligencia
        self.__defensa = self.__defensa + defensa
    #Variable del constructor vacío

    def esta_vivo(self):
        return self.__vida > 0

    def morir(self):
        self.__vida = 0
        print(self.__nombre, "Ha muerto")

    def dañar(self, enemigo):
        return self.__fuerza - enemigo.__defensa

    def atacar(self,enemigo):
        daño = self.dañar(enemigo)
        if daño > 0:
            enemigo.__vida = enemigo.__vida - daño
            if enemigo.__vida > 0:
                print(self.__nombre, "ha realizado",daño,"de daño a",enemigo.__nombre)
                print("vida de",enemigo.__nombre,enemigo.__vida)
            else:
                enemigo.morir()
        else:
            print(self.__nombre, "no logro hacerle daño a",enemigo.__nombre)
            print("vida de",enemigo.__nombre,enemigo.__vida)
    def getVida(self):
        return self.__vida
    def setVida(self, vida):
        if vida <= 0:
            self.morir()
        else:
            self.__vida = vida
        




miPersonaje = Personaje("EstebanDido",45,50, 1, 100)
miEnemigo = Personaje("Angel",100,100,70,100)
miPersonaje.vida = 0
print(miPersonaje.getVida())
miPersonaje.imprimir_atributos()
miPersonaje.setVida(1000)
# miPersonaje.atacar(miEnemigo)
# miEnemigo.atacar(miPersonaje)
# miEnemigo.atacar(miPersonaje)
miPersonaje.imprimir_atributos()
miPersonaje.setVida(-1000)
# subir_nivel(miPersonaje,10,10,10)
# imprimir_atributos(miPersonaje)
# print(esta_vivo(miPersonaje))
# morir(miPersonaje)
# print(esta_vivo(miPersonaje))

#Modificar valores de los atributos

#Esto es muy similar a como funciona en Roblox (Lua)
# miPersonaje.__nombre = "EstebanDido"
# miPersonaje.__fuerza = 300
# miPersonaje.__inteligencia = -2
# miPersonaje.__defensa = 30
# miPersonaje.__vida = 2

# print("El nombre de mi personaje es ", miPersonaje.__nombre)
# print("La fuerza de mi personaje es ", miPersonaje.__fuerza)
# print("La inteligencia de mi personaje es ", miPersonaje.__inteligencia)
# print("La defensa de mi personaje es ", miPersonaje.__defensa)
# print("La vida de mi personaje es ", miPersonaje.__vida)