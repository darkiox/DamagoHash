
# DamagoHash

Un algoritmo de hash con efecto avalancha para verificación de integridad. Diseñado para su uso en hash de contraseñas.

Para utilizar debes clonar el repositorio y ejecutar DamagoHashMenu.py. En caso de querer importar en tu proyecto, solo debes importar la funcion DamagoHash de DamagoHash.py


## Cómo funciona

Al ingresar datos a la función, esta primeramente convierte los caracteres a decimales, luego si el decimal es par, se suma a una variable "sum", y si es inpar, se multiplica a dicha variable.
Luego la suma se transforma a una lista de un string y se convierte a binario. Posterior a eso se realiza un XOR de dos en dos, es decir, los dos primeros caracteres entregan un resultado que se agrega a un string, los siguientes dos caracteres entregan otro resultado que se agrega al mismo string, hasta completar. En caso de que el largo del binario en el cual se están realizando las operaciones sea impar, se ignora el último caracter.
Luego del XOR se transforma el resultado en una cadena de bytes y se intenta transformar a un entero, el cual luego se codifica en base64 y se decodifica en ASCII.
En caso de que dicha decodificación en ASCII sea menor que 100, se repite sobre si mismo alternando el orden. (holaalohholaaloh...) Si es mayor a 100, se vuelve a reingresar a la función DamagoHash hasta que el largo sea efectivamente 100.
## Comparaciones
Tabla de comparaciones de Base y Entropía para el hash "ColoColoTieneLaLibertadores", comparado con implementaciones de MD5, SHA1, SHA256 en el sistema operativo Linux.
|          | **DamagoHash** | **MD5** | **SHA1** | **SHA256** |
|--------------|----------------|---------|----------|------------|
| **Base**     | 25             | 15      | 15       | 15         |
| **Entropía** | 465            | 126     | 157      | 251        |
| **ExecTime** | 0.001s         | 0.004s  | 0.01s    | 0.01s      |

----

Tabla de comparaciones de tiempo de ejecución con ingreso de múltiples líneas. Comparaciones realizadas con las implementaciones de MD5, SHA1 y SHA256 de la librería "hashlib" de Python.
|       | **DamagoHash** | **MD5**  | **SHA1** | **SHA256** |
|-----------|----------------|----------|----------|------------|
| **1 línea**   | 0.004s         | 0.0s     | 0.0005s  | 0.00049s   |
| **10 líneas** | 0.0449s        | 0.00049s | 0.0005   | 0.0005s    |
| **20 líneas** | 0.08s          | 0.0s     | 0.0s     | 0.0005s    |
| **50 líneas** | 0.157s         | 0.0005s  | 0.00049s | 0.0s       |

---
Tabla de comparaciones de tiempo de ejecución con ingreso de archivos visibles en el repositorio. Comparaciones realizadas con las implementaciones de MD5, SHA1 y SHA256 de la librería "hashlib" de Python.
|              | **DamagoHash** | **MD5** | **SHA1** | **SHA256** |
|------------------|----------------|---------|----------|------------|
| **informe1.pdf** | 0.713s         | 0.001s  | 0.0005s  | 0.0004s    |
| **informe2.pdf** | 1.8485s        | 0.0244s | 0.001s   | 0.00099s   |
| **informe3.pdf** | 1.4399s        | 0.0255s | 0.0009s  | 0.002s     |
| **informe4.pdf** | 0.405s         | 0.009s  | 0.0005s  | 0.0004s    |
| **thevenin.pdf** | 30.52s         | 0.0279s | 0.0130s  | 0.0210s    |
