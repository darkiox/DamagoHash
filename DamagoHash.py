import base64
#Función de hash principal
def DamagoHash(porhashear):
    paso1 = []
    sum = 1
    #Convertir caracteres a decimal
    for i in porhashear.encode():
        #Si el decimal es par, sumar
        if i%2 == 0:
          sum += i
        #Cualquier otro caso, multiplicar
        else:
          sum *= i
    #Convertir la suma a una lista de un string. (Se obtiene caracter por caracter)
    paso1 = list(str(sum))
    paso2 = ""
    #Convertir a binario y eliminar 0b inicial, luego guardar en paso2
    for i in paso1:
      a,b = bin(int(i)).split('b')
      paso2+=b
    paso3 = ""
    #Realizar un XOR en bloques de a 2 (caracter 0 con caracter 1, caracter 2 con caracter 3, etc.)
    #Agregar resultado de XOR a paso3
    for i in range(0,len(paso2)-1,2):
      paso3 += str(int(paso2[i])^int(paso2[i+1]))
    #Agregar el 0b eliminado anteriormente para tener una cadena de bytes
    paso3 = "0b"+paso3
    #Intentar convertir a int los bytes
    try:
      paso3 = int(paso3,2)
    except:
      paso3 = paso3
    #Convertir lo anterior a base64
    paso3 = base64.b64encode(str(paso3).encode()).decode('ascii')
    cont = 1
    #Si es más corto que 100 caracteres
    #Alterna entre repetir el hash derecho y luego al revés
    while len(paso3) < 100:
      if cont % 2 == 0:
        paso3 += paso3
      else:
        paso3 += paso3[::-1]
      cont+=1
    #Si es mayor a 100, volver a Hashear
    #Recursividad
    if len(paso3) > 100:
      return DamagoHash(paso3)
    #Retornar los 100 caracteres del hash creado
    return paso3