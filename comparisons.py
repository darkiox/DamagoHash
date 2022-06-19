import hashlib,time,base64
from DamagoHash import DamagoHash
opc = input("1 - Lineas, 2 - Archivo ----> ")
opc = int(opc)
if(opc == 1):
    lineas = input("Ingrese numero de lineas (1, 10, 20, 50): ")
    lineas = int(lineas)
    Archivo = "rockyou.txt"
    contalinea = 0
    timer = time.time()
    with open(Archivo) as arc:
        for line in arc:
            line = line[:-1] #Quitar salto de linea
            line = line.encode()
            hashlib.md5(line).digest()
            contalinea+=1
            if(contalinea == lineas):
                break
    print("Tiempo MD5 = ", str(time.time()-timer))

    contalinea = 0
    timer = time.time()
    with open(Archivo) as arc:
        for line in arc:
            line = line[:-1] #Quitar salto de line
            line = line.encode()
            hashlib.sha1(line).hexdigest()
            contalinea+=1
            if(contalinea == lineas):
                break
    print("Tiempo SHA1 = ", str(time.time()-timer))

    contalinea = 0
    timer = time.time()
    with open(Archivo) as arc:
        for line in arc:
            line = line[:-1] #Quitar salto de linea
            line = line.encode()
            hashlib.sha256(line).hexdigest()
            contalinea+=1
            if(contalinea == lineas):
                break
    print("Tiempo SHA256 = ", str(time.time()-timer))

    contalinea = 0
    timer = time.time()
    with open(Archivo) as arc:
        for line in arc:
            line = line[:-1] #Quitar salto de linea
            DamagoHash(line)
            contalinea+=1
            if(contalinea == lineas):
                break
    print("Tiempo DamagoHash = ", str(time.time()-timer))
if(opc == 2):
    Archivo = input("Ingrese nombre archivo: ")
    BUF_SIZE = 1024
    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    sha256 = hashlib.sha256()
    timer = time.time()
    with open(Archivo, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            md5.update(data)
    print("Archivo Tiempo MD5 = ", time.time()-timer)
    timer = time.time()
    with open(Archivo, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            sha1.update(data)
    print("Archivo Tiempo SHA1 = ", time.time()-timer)
    timer = time.time()
    with open(Archivo, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            sha256.update(data)
    print("Archivo Tiempo SHA256 = ", time.time()-timer)
    timer = time.time()
    Filehash = ""
    with open(Archivo,'rb') as archivo:
        while archivo.read(BUF_SIZE):
            bleidos = str(base64.b64encode(archivo.read(BUF_SIZE)))
            Filehash += bleidos
            Filehash = DamagoHash(Filehash)
    print("Archivo Tiempo DamagoHash = ", time.time()-timer)