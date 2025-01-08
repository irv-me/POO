class Personaje:
    #Atributos de la clase
    nombre = "Default"
    fuerza = 0
    inteligencia = 0
    defensa = 0
    vida = 0
    pass

#Variable del constructor vacío

miPersonaje = Personaje()

#Modificar valores de los atributos

#Esto es muy similar a como funciona en Roblox (Lua)
miPersonaje.nombre = "EstebanDido"
miPersonaje.fuerza = 300
miPersonaje.inteligencia = -2
miPersonaje.defensa = 30
miPersonaje.vida = 2

print("El nombre de mi personaje es ", miPersonaje.nombre)
print("La fuerza de mi personaje es ", miPersonaje.fuerza)
print("La inteligencia de mi personaje es ", miPersonaje.inteligencia)
print("La defensa de mi personaje es ", miPersonaje.defensa)
print("La vida de mi personaje es ", miPersonaje.vida)