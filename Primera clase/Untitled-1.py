#¿Qué es una estructura de datos?

#Organizar los datos en forma que permitan un manejo eficiente desde un conjunto de numeros en un arreglo hasta
#sistematizadas complejos como bases de datos, todas las aplicaciones dependen de estructuras de datos diseñados.

#el tipo común y fundamental es el arreglo... este se usa para manejar colecciones de elementos.

#Definicion: 
#un arreglo es una estructura que, dependiendo del lenguaje, almacena elementos del mismo tipo, los organiza en posiciones
#de memoria que son contiguas, permite acceder a los items por medio de un indice.

#En python, ademas de conocerse como arreglos, se pueden conocer como listas.

#¿Porqué usar arreglos?.

#Los arreglos tienen un uso muy extendido debido a la simplicidad y eficiencia a la hora de manejar datos relacionados
#entres si ofrecen acceso inmediato a cualquier elemento dado su indice, son esenciales para algoritmos fundamentales,
#como metodos de busqueda y metodos de orden.

#Casos de uso mas omunes:
#almacenar listadoshistoricos de temperatura diaria en una ciudad, almacenar nombres de un grupo de estudiantes, gestionar 
#un inventario.

#Características principales.
#1 acceso rapido de informaci+on por medio de un inidice.
#Cualquier elemento puede ser accedido con el indice lo que toma un timepo de magnitud constante.

# arreglo = [10, 20, 30, 40, 50]
# print ("El elemento en el indice 2 es: ", arreglo [-2])


#Homogeneidad:
#En lenguaje como c, todos los elementos deben ser del mismo tipo...
#pero, python permite mezclar tipos, pero si hay un proposito estricto, es mejor usar elementos homogeneos.

#Tamaño dinamico:
#A diferencia de otros lenguajes las listas en python pueden crecer o reducirse de tamaño en cualquier momento.
# array = [1, 2, 3]
# print(array)
# array.append (4)
# print (array)
# array.pop ()
# print (array)
# print (len(array))

##Operaciones fundamentales de los arreglos.

#1 crear y llenar arreglos.


# arr = []

#Llenar con 5 valores un arreglo, estos valores los debe ingresar el usuario.

# for i in range (5):
#     valor = int(input(f"Ingrese un número sobre la posición {i}: "))
#     arr.append(valor)
# print (f"El arreglofinalmente queda: {arr}")

#Recorrer el arreglo.
#Los arreglos se recorren o iteran con los ciclos for o while. Lo mas común es hacerlo en ciclo for.

# print ("Elementos de arreglo: ")
# for i in range (len)(arr):
#     print (f"Indice {i},: {arr[i]}")

#Modificar elementos internos del arreglos.
    
# layout = [1, 2, 3, 4, 5]
# print ("Elementos del arreglo antes de la modificación: ", layout)
# layout [2] = 3.1416
# print ("Elementos del arreglo antes de la modificación: ", layout)

#Eliminación.
#Se puede hacer de dos maneras dependiendo del parametro que quiera utilizar:
#Podemos eliminar por elemento
#Eliminar por indice (pop) elimina el ultimo elemento o eliman el elemento en la posición indicada.

# layout.pop (1)
# print ("Elementos del arreglo despues de eliminar por indice: ")

#Eliminar por elemento (remove) elimina el primer elemento que encuentre que coincida con el valorque se le indique.
# layout.remove (4)
# print ("Elementos del arreglo depsues de eliminar por elemento: ", layout)


#Aritmetica con arreglos:

# pepito = [5, 10, 15, 20, 25]

# suma = sum (pepito)
# promedio = suma / len(pepito) 
# maximo = max (pepito)
# minimo = min (pepito)

# print (f"Suma: {suma}, el promedio: {promedio}, Maximo: {maximo}, Minimo: {minimo}")

#Ventajas y desventajas de utilizarlo.
#Ventajas:
#Eficiencia en el acceso a elemetos por indice.
#Estructura es simple para almacena datos relacionados.
#Base para muchas otras estructuras como pilas, colas, matrices etc...

#Desventajas:
#Tamaño fijo (en lenguajes como C)
#No se pueden eliminar elementos en medio del arreglo (en lenguajes como C)
#inserciones y las eliminaciones suelen ser muy costosas si no se hacen en cabeza o cola.
#consumen memoria continua, lo que puede llegar a limitar su tamaño.


#Escribir un programa que:
#solicite al usuario ingresar 10 números.
#Almacene solo los números pares en un arreglo y luego muestre los números pares alamcenados en el arreglo

# numeros = []

# for i in range (100):
#     num = int(input(f"Ingrese el número {i + 1}: "))
#     if num % 2 == 0:
#         numeros.append (num)
# print ("Números pares: ", numeros)

#Crear un programa que solicite al usuario 5 numeros y los invierta.

# arreglo = []

# for i in range (5):
#     valor = input (f"Ingrese un valor para el arreglo en la posicion {i + 1}: ")
#     arreglo.append (valor)
# print (f"El arreglo original es: {arreglo}")
# print (f"Arreglo invertido quedó: {arreglo[: : - 1]}")

#Crear un programa que calcule el promedio de calificaiones de un grupo de estudiantes y
#determine cuantos aprovaros teniendo en cuenta que la calificaión miníma para aprobar es 6.

calificaciones = []

#Pedir calificaciones.

n = int(input("¿Cuantos estudiantes hay? ")) 
for i in range (n):
    nota = float (input(f"Ingrese la calificación del estudiante {i + 1} "))
    calificaciones.append(nota)

#Calculamos el promedio:
promedio = sum(calificaciones)/len(calificaciones)
aprobados = len([nota for nota in calificaciones if nota >= 6])

print (f"El promedio del grupo: {promedio: .2f}")
print (f"Estudiantes aprobados: {aprobados}")
       


