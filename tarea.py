#1 par o impar
def par_impar():
    num= int(input("ingresa un  numero: "))
    if  num % 2 == 0:
        print("el numero es par")
    else:
        print("el numero es impar")
#2 numero mayor entre tres numeros
def num_mayor():
    num1= int(input("escribe el primer numero: "))
    num2= int(input("escribe el segundo numero: "))
    num3= int(input("escribe el tercer numero: "))
    Max= max(num1, num2, num3)
    Men= min(num1, num2, num3)
    print(f"el numero mayor es: {Max} y el menor es: {Men}")
#3 edad valida para votar
def edad_votar():
    edad= int(input("escrbe tu edad: "))
    if edad >= 18:
        print("tienes la edad suficiente para votar")
    else:
        print("no tienes edad suficiente para votar")
#4 calificacion
def calificacion():
    nota= int(input("ingresa tu  nota: "))
    if 0 <= nota <= 29:
        print("fuiste reprobado")
    elif 30 <= nota <= 39:
        print("aprobaste")
    elif 40<= nota <= 50:
        print("aprobaste con una nota alta")
    else:
        print("nota invalida")
#5 suma de los siguientes 100 numeros 
def suma_100_num():
    n= int(input("escribe el numero que quieres sumar: "))
    suma= 0
    for i in range(n + 1, n + 101):
        suma += i 
    print(f"la suma de los siguientes 100 numeros es {suma}") 
#6 convercion euros a dolares
def conv():
    tasa_cam= 1.17
    valor= float(input("ingresa el valor en euros que quieres convertir a dolares: "))
    conv= valor * tasa_cam
    print(f"la convercion de euros a dolares es: {conv}")
#7  area de un rectangulo 
def area_rectangulo():
    altura= int(input("ingresa la altura del rectngulo: "))
    anchura= int(input("ingresa la anchura del rectangulo: "))
    area= altura * anchura
    print(f"el area del rectangulo es: {area}") 
#8 numeros pares menores
def numeros_menores():
    n= int(input("escribe un  numero: "))
    print(f"numeros impares menores que {n}")
    for i in range(1, n, 2):
        print(i, end=" ")
#9 tabla de mult
def tabla_mult():
    n= int(input("escribe el numero del que quieres la tabla: "))
    print(f"la tabla de multiplicar de {n} es: ")
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
#10 cuenta regresiva
def cuenta_regresiva():
    n = int(input("Ingrese un número: "))
    for i in range(n, 0, -1):
        print(i, end=" ")
    print()
#menu
def menu():
    #par_impar()
    #num_mayor()
    #edad_votar()
    #calificacion()
    #suma_100_num()
    #conv()
    #area_rectangulo()
    #numeros_menores()
    #tabla_mult()
    cuenta_regresiva()
menu()



