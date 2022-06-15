import base64,time,os
#Función de hash principal
def DamagoHash(porhashear):
    paso1 = []
    sum = 1
    #Convertir caracteres a decimal
    for i in porhashear.encode():
        #Si se llega al final de lo que se hashea, finalizar for
        if i == len(porhashear):
            break
        #Si el decimal es par, sumar
        if i%2 == 0:
          sum += i
        #Cualquier otro caso, multiplicar
        else:
          sum *= i
    #Convertir la suma a una lista de un string. (Se obtiene caracter por caracter)
    paso1 = list(str(sum))
    paso2 = []
    #Convertir a binario y eliminar 0b inicial, luego guardar en paso2
    for i in paso1:
      a,b = bin(int(i)).split('b')
      paso2.append(b)
    paso3 = ""
    #Pasar los binarios de paso2 a un string paso3
    for i in paso2:
      paso3 += i
    paso4 = ""
    #Realizar un XOR en bloques de a 2 (caracter 0 con caracter 1, caracter 2 con caracter 3, etc.)
    #Agregar resultado de XOR a paso4
    for i in range(0,len(paso3)-1,2):
      paso4 += str(int(paso3[i])^int(paso3[i+1]))
    #Agregar el 0b eliminado anteriormente para tener una cadena de bytes
    paso4 = "0b"+paso4
    #Intentar convertir a int los bytes
    try:
      paso4 = int(paso4,2)
    except:
      paso4 = paso4
    #Convertir lo anterior a base64
    paso4 = base64.b64encode(str(paso4).encode()).decode('ascii')
    cont = 1
    #Si es más corto que 100 caracteres
    #Alterna entre repetir el hash derecho y luego al revés
    while len(paso4) < 100:
      if cont % 2 == 0:
        paso4 += paso4
      else:
        paso4 += paso4[::-1]
      cont+=1
    #Si es mayor a 100, volver a Hashear
    #Recursividad
    if len(paso4) > 100:
      return DamagoHash(paso4)
    #Retornar los 100 caracteres del hash creado
    return paso4[:100]
  
def MainMenu():
    div = "-"
    lat = "|"
    opcion1 = "1.- String ingresado por teclado"
    opcion2 = "2.- Archivo completo"
    opcion3 = "3.- Archivo por linea"
    opcion4 = "4.- Entropia de un string"
    opcion5 = "5.- Salir"
    print(" "+div*38+" ")
    print(lat + " "*12 + "Menú Principal" + " "*12 + lat)
    print(" "+div*38+" ")
    print(lat+opcion1+" "*6+lat)
    print(lat+opcion2+" "*18+lat)
    print(lat+opcion3+" "*17+lat)
    print(lat+opcion4+" "*13+lat)
    print(lat+opcion5+" "*29+lat)
def opcion():
    try:
        print(" "+"-"*38+" ")
        opc = int(input("Digite Opción-------->   "))
        if opc >= 1 and opc <= 5:
            return opc
        else:
            print("OPCIÓN NO VALIDA")
            return opcion()
    #Evitar ingreso de caracteres
    except ValueError:
        print("ERROR... No se pueden ingresar letras")
        return opcion()
    #Evitar CTRL+C
    except:
        print("ERROR... Respete las normas")
        return opcion()

MainMenu()
while(True):
  opc =  opcion()
  if opc == 5:
    break
  if opc == 1:
    #Opción 1, un string ingresado por teclado
    porhashear = input("Ingrese un string a hashear: ")
    print(DamagoHash(porhashear))
  if opc == 2:
    #Opción 2, un archivo completo
    print("")
    print("NOTA: El archivo debe estar localizado en el mismo lugar del script.")
    Archivo = input("Nombre del archivo con extensión: ")
    print(" "+"-"*38+" ")

    #Implementación de Buffer de tamaño 1024 bytes
    #Este será equivalente a 1024 siempre cuando el archivo sea de un tamaño mayor
    #Si es menor, el buffer será equivalente a la mitad del tamaño del archivo
    size = os.stat(Archivo).st_size
    if  size < 1024:
      #Dividir tamaño del archivo en la mitad, y en caso de ser decimal
      #Redondear hacia arriba
      buffer = int(size/2) + (size % 2 > 0)
    else:
      buffer=1024
    #Timer
    timer = time.time()
    Filehash = ""
    #Leer archivo con buffer
    with open(Archivo,'rb') as archivo:
      while archivo.read(buffer):
          bleidos = str(base64.b64encode(archivo.read(buffer)))
          Filehash += bleidos
          Filehash = DamagoHash(Filehash)
    print(Filehash)
    #Imprimir tiempo de ejecución
    print("Execution time: " , time.time() - timer , " s")
  if opc == 3:
      #Opción 3, archivo línea a línea
      print("")
      print("NOTA: El archivo debe estar localizado en el mismo lugar del script.")
      Archivo = input("Nombre del archivo con extensión: ")
      print(" "+"-"*38+" ")
      contalinea = 1
      with open(Archivo) as arc:
        for line in arc:
          print(DamagoHash(line))
          contalinea+=1
      print("Lineas hasheadas: ", contalinea)