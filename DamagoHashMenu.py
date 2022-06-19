import base64,time,os,math
from DamagoHash import DamagoHash

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

def inputNumero(out):
    try:
        num = int(input(out))
        if isinstance(num, int):
            return num
        else:
            print("Debe ingresar un número.")
            return inputNumero(out)
    except ValueError:
        print("ERROR... No se pueden ingresar letras")
        return inputNumero(out)
    except:
        print("ERROR... Respete las normas")
        return inputNumero(out)

MainMenu()
while(True):
  opc =  opcion()
  if opc == 5:
    break
  if opc == 1:
    #Opción 1, un string ingresado por teclado
    porhashear = input("Ingrese un string a hashear: ")
    print(" "+"-"*38+" ")
    timer = time.time()
    print(DamagoHash(porhashear))
    print("Execution time: ", time.time()-timer, " s")
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
      lineas = inputNumero("Cantidad de lineas a hashear (-1 para todo el archivo): ")
      print(" "+"-"*38+" ")
      contalinea = 0
      with open(Archivo) as arc:
        for line in arc:
          line = line[:-1] #Quitar salto de linea
          print(" "+"-"*38+" ")
          print("Linea = '" , line, "'")
          print("Hash = '", DamagoHash(line),"'")
          print(" "+"-"*38+" ")
          contalinea+=1
          if(contalinea == lineas):
            break
      print("Lineas hasheadas: ", contalinea+1)
  if opc == 4:
      #Opción 4, entropía de un string
      print("")
      Stringbase = input("Ingrese un string para calcular su entropía: ")
      print(" "+"-"*38+" ")
      #Se toma como base cada caracter diferente ingresado
      Basestring = list(dict.fromkeys(Stringbase))
      #Se calcula la entropía y se redondea hacia arriba
      Entropia = math.ceil(len(Stringbase)*math.log2(len(Basestring)))
      print("Entropía de '" +Stringbase+"'")
      print("Entropía =" ,Entropia)
      print("Base = " + str(len(Basestring)))
