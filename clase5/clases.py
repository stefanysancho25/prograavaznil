mensaje = "Hola Mundo"

print(type(mensaje))

class gato:
    patas = 4

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
       

    def habla(self):
        #print("miau")
        print(f"mi nombre es {self.nombre} y tengo {self.edad} años")


mi_gato = gato("Mimi", 2)
mi_gato2 = gato("yuyu", 3) 
mi_gato2.habla()
mi_gato.habla()
mi_gato2.patas = 3
print(mi_gato.patas)
