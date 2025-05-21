# funciones para que nos sirve 
#def saludar():
 #   x = 5
  #  y = 10
   # print("Hola, bienvenido ", x + 10)

#saludar()
#saludar()
#saludar()
#saludar()

def saludar(name, lastname="anonimo"):
    print("TU NOMBRE ES ", name)
    print("TU APELLIDO ES ", lastname)
    print(f"HOLA {name} {lastname}")


def saludarSinParametros():
    print("Hola")   


#saludar( "stefany", "perez")
#saludar( "anne", "garcia")
#saludar("camila")
#saludar("STEFANY", "D´ ARC")
#saludar(lastname="lopez", name= "ketty")
#saludar(name="bedt")
#saludarSinParametros()

#numeros = (1, 2, 3, 4, 5, 8)
#numeros = 1
#numeros = (1, 2, 3)
#numeros = (1, "b",2, 3,"a")
#numeros = (1, 2, 3) + (4, 5, 8)
#numeros = (1, 2, 3) 
#letras = ("a", "b", "c")
#lisNumeros =[1, 2, 3]
#lisNumeros [0]= 10

#caracteres = list("nicole")

#alfanumerica = numeros + letras

#mascotas = ["lucas", "totoro", "milo"]   mascotas
#print(mascotas)
#mascotas.append("gato")
#mascotas[2] = "perro"

#mascotas = ["1", "2", "3"]        #numeros
#print(mascotas)
#mascotas.append("4")
#mascotas[2] = "4"

#xya = list(range(10))

#xya = list(range(0,10, 2))
#xya = list(range(10, 25, 2)) #para ejecutar 10 veces una funcion
#xya = list(range(10))

#matriz =[[1, 2,] , [ 5, 6]]
#matriz =[(1, 2,) , [ 5, 6]] # tupla y lista


#print(xya[::-1])
#print(xya)


#print(mascotas[0:2])  #salto de linea
#print(mascotas[0:2:1])  #salto de linea
#print(mascotas[0:2:2])  #salto de linea
#print(mascotas[::1])  #salto todo
#print(mascotas[::-1])  #salto lo imbierte
#+print(mascotas[2:3:1])  #incio-termino -salto

#print(caracteres)
# 1d23a

#def suma(*numeros):
#def suma(numeros):
    #result = 0
    #for number in numeros:
        #print(type(number))
        #if isinstance(number, int):
        #if type(number) is int:
       #  result += number
        #result = result + number
       
    #print(result)
    #return result

#suma(numeros)       

#suma(1, 2, 3, 4)
#suma(1)
#suma(numeros)       
#suma(1, 2, 3)
#x = suma(1, 2, 3, "a")
#print(numeros)
#suma(numeros)
#print(alfanumerica)
#print(numeros)
#print(lisNumeros)

#los diccionarios que funcionan con la estructura de un valor

#punto = {"x": 10,"y": 20,}
#print(punto["x"])

#punto = {"name": 10,"id": 20,}  # lo podemo utilizar para cuando utilizamos un apy

#print(punto["id"])

puntoCartesiano = {"x": 10,"y": 20,"z": 4}  # 

#puntoCartesiano["z"] = 3
#print (puntoCartesiano)
#print (puntoCartesiano.get("x")) #exsite el valor 
#print (puntoCartesiano.get("w")) #no existe el valor
#print (puntoCartesiano.get("w", "no existe")) #no existe el valor  (0 , "no existe")

#for valor in puntoCartesiano.items():  # por separados "valor" o "llave"
   # print(valor)
    
for valor , llave in puntoCartesiano.items():  # unidos "valor , llave"
   #  TODO: poner logica 
    print(valor, llave)
   
productos = [
    {"id": 1, "nombre": "camisa", "precio": 100, "cantidad": 10},
    {"id": 2, "nombre": "pantalon", "precio": 200, "cantidad": 20},
    
   ]
     
