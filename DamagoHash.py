
import base64,time

def DamagoHash(porhashear):

    paso1 = []
    aux = 3 #Valor arbitrario
    sum = 1
    for i in porhashear.encode():
        if i == len(porhashear):
            break
        if i%2 == 0:
          sum += i
        else:
          sum *= i
    #print("sum = ",sum)
    paso1 = list(str(sum))
    paso2 = []
    for i in paso1:
      a,b = bin(int(i)).split('b')
      paso2.append(b)
    paso3 = ""
    for i in paso2:
      paso3 += i
    paso4 = ""
    for i in range(0,len(paso3)-1,2):
      paso4 += str(int(paso3[i])^int(paso3[i+1]))
    paso4 = "0b"+paso4
    paso4 = int(paso4,2)
    paso4 = base64.b64encode(str(paso4).encode()).decode('ascii')
    cont = 1
    while len(paso4) < 100:
      if cont % 2 == 0:
        paso4 += paso4
      else:
        paso4 += paso4[::-1]
      cont+=1
    if len(paso4) > 100:
      return DamagoHash(paso4)
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
    except ValueError:
        print("ERROR... No se pueden ingresar letras")
        return opcion()
    except:
        print("ERROR... Respete las normas")
        return opcion()

MainMenu()
while(True):
  opc =  opcion()
  if opc == 5:
    break
  if opc == 1:
    porhashear = input("Ingrese un string a hashear: ")
    print(DamagoHash(porhashear))
  if opc == 2:
    #Opcion 2, un archivo completo
    print("")
    print("NOTA: El archivo debe estar localizado en el mismo lugar del script.")
    Archivo = input("Nombre del archivo con extensión: ")
    #Timer
    timer = time.time()
    #Implementación de Buffer de tamaño 1024 bytes
    buffer=1024
    Filehash = ""
    with open(Archivo,'rb') as archivo:
        while archivo.read(buffer):
            bleidos = str(base64.b64encode(archivo.read(buffer)))
            Filehash += bleidos
            Filehash = DamagoHash(Filehash)
    print(Filehash)
    print(time.time() - timer)

  #print(DamagoHash("corneta"))
  #print(DamagoHash("cornetb"))