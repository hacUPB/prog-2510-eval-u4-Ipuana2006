import os
import csv
import matplotlib.pyplot as plt

#FUNCIONES PARA ARCHIVOS .TXT

def contar_palabras_caracteres(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            palabras = contenido.split()#Divide el contenido del archivo en una lista de palabras, utilizando los espacios como delimitadores
            total_caracteres = len(contenido)
            sin_espacios = len(contenido.replace(" ", "").replace("\n", ""))  # Elimina todos los espacios y saltos de línea del contenido y luego obtiene el número de caracteres restantes.
            print(f"Palabras: {len(palabras)}")
            print(f"Caracteres (con espacios): {total_caracteres}")
            print(f"Caracteres (sin espacios): {sin_espacios}")
    except FileNotFoundError:
        print("Archivo no encontrado.")

def reemplazar_palabra(nombre_archivo):
    palabra_buscar = input("Palabra a buscar: ")
    palabra_reemplazo = input("Palabra de reemplazo: ")
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo: #Esta línea sirve para abrir un archivo y poder trabajar con él (leerlo o escribir en él).
            contenido = archivo.read()
        nuevo_contenido = contenido.replace(palabra_buscar, palabra_reemplazo)
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write(nuevo_contenido) #Escribe el nuevo contenido (con las palabras reemplazadas) en el archivo
        print("Reemplazo realizado exitosamente.")
    except FileNotFoundError:
        print("Archivo no encontrado.")

def histograma_vocales(nombre_archivo):
    vocales = 'aeiou'
    conteo = dict.fromkeys(vocales, 0)#Crea un diccionario donde las claves son las vocales ('a', 'e', 'i', 'o', 'u') y los valores iniciales son 0.
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo: 
            contenido = archivo.read().lower() #Lee todo el contenido del archivo y lo convierte a minúsculas
            for letra in contenido: #
                if letra in conteo: #Comprueba si el carácter es una vocal (está en el diccionario conteo).
                    conteo[letra] += 1 #Si el carácter es una vocal, incrementa su recuento en el diccionario conteo.
        plt.bar(conteo.keys(), conteo.values(), color='skyblue') #Crea un gráfico de barras
        plt.title("Histograma de vocales")
        plt.xlabel("Vocal")
        plt.ylabel("Frecuencia")
        plt.show()
    except FileNotFoundError:
        print("Archivo no encontrado.")

#FUNCIONES PARA ARCHIVOS .CSV

def mostrar_15_filas(nombre_archivo):
    try:
        with open(nombre_archivo, newline='', encoding='utf-8') as archivo:
            lector = csv.reader(archivo) #Crea un objeto lector de CSV utilizando
            for i, fila in enumerate(lector): # Recorre cada fila del archivo CSV, manteniendo un registro del número de fila
                print(fila)
                if i == 14:
                    break
    except FileNotFoundError:
        print("Archivo no encontrado.")

def calcular_estadisticas(nombre_archivo):
    columna_nombre = input("Nombre de la columna numérica a analizar: ")
    try:
        with open(nombre_archivo, newline='', encoding='utf-8') as archivo: 
            lector = csv.DictReader(archivo) #que trata la primera fila del CSV como encabezados de columna, permitiendo acceder a los valores por el nombre de la columna.
            datos = []
            for fila in lector:
                valor = fila.get(columna_nombre) # Obtiene el valor de la columna especificada por el usuario para la fila actua
                if valor:
                    try:
                        datos.append(float(valor))
                    except ValueError:
                        continue
        if datos:
            datos.sort() #Ordena la lista datos en orden ascendente
            cantidad = len(datos)
            promedio = sum(datos) / cantidad
            mediana = datos[cantidad // 2] if cantidad % 2 != 0 else (datos[cantidad // 2 - 1] + datos[cantidad // 2]) / 2 # Calcula la mediana. Si la cantidad de datos es impar, la mediana es el valor central. Si es par, es el promedio de los dos valores centrales
            print(f"Número de datos: {cantidad}")
            print(f"Promedio: {promedio}")
            print(f"Mediana: {mediana}")
            print(f"Mínimo: {min(datos)}")
            print(f"Máximo: {max(datos)}")
        else:
            print("No se encontraron datos válidos en esa columna.")
    except FileNotFoundError:
        print("Archivo no encontrado.")

def graficar_columna(nombre_archivo):
    columna_nombre = input("Nombre de la columna a graficar: ")
    try:
        with open(nombre_archivo, newline='', encoding='utf-8') as archivo:   #Abre el archivo CSV en modo lectura con la codificación UTF-8 para manejar diferentes caracteres.
            lector = csv.DictReader(archivo) #permite acceder a los datos por el nombre de la columna en lugar de por el índice.
            datos = []
            for fila in lector:
                valor = fila.get(columna_nombre) #Para cada fila, obtiene el valor de la columna especificada por el usuario 
                if valor:
                    try:
                        datos.append(float(valor))
                    except ValueError:
                        continue
        if datos:
            plt.plot(datos) #Si contiene datos, crea un gráfico de línea 
            plt.title(f"Gráfica de la columna '{columna_nombre}'")
            plt.xlabel("Índice")
            plt.ylabel("Valor")
            plt.show() #Muestra el gráfico
        else:
            print("No hay datos numéricos válidos para graficar.")
    except FileNotFoundError: #Captura la excepción, que ocurre si el archivo CSV especificado no se encuentra.
        print("Archivo no encontrado.") 

#OTRAS FUNCIONES

def listar_archivos():
    ruta = input("Ingrese la ruta (deje en blanco para ruta actual): ").strip()
    if ruta == "":
        ruta = os.getcwd() # obtiene el directorio de trabajo actual, es decir, el directorio desde donde se está ejecutando el script
    if os.path.exists(ruta): # verifica si la ruta ingresada existe. Si no existe, se imprime "Ruta no válida.".
        if os.path.isdir(ruta):  # Si la ruta existe, esta condición verifica si es un directorio.
            archivos = os.listdir(ruta) #si es un directori, devuelve una lista de los nombres de todos los archivos y directorios en la ruta especificada.
            print("\nArchivos encontrados:")
            for archivo in archivos:
                print(archivo)
        else:
            print("La ruta ingresada corresponde a un archivo, no a un directorio.")
    else:
        print("Ruta no válida.")

#MENÚS

def submenu_txt():
    nombre_archivo = input("Nombre del archivo .txt: ")
    while True:
        print("\nSubmenú .TXT")
        print("1. Contar número de palabras y caracteres")
        print("2. Reemplazar una palabra por otra")
        print("3. Histograma de ocurrencia de vocales")
        print("4. Volver al menú principal")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            contar_palabras_caracteres(nombre_archivo)
        elif opcion == "2":
            reemplazar_palabra(nombre_archivo)
        elif opcion == "3":
            histograma_vocales(nombre_archivo)
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")

def submenu_csv():
    nombre_archivo = input("Nombre del archivo .csv: ")
    while True:
        print("\nSubmenú .CSV")
        print("1. Mostrar las 15 primeras filas")
        print("2. Calcular estadísticas de una columna")
        print("3. Graficar columna numérica")
        print("4. Volver al menú principal")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            mostrar_15_filas(nombre_archivo)
        elif opcion == "2":
            calcular_estadisticas(nombre_archivo)
        elif opcion == "3":
            graficar_columna(nombre_archivo)
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")

# FUNCIÓN PRINCIPAL

def main():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Listar archivos")
        print("2. Procesar archivo .txt")
        print("3. Procesar archivo .csv")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            listar_archivos()
        elif opcion == "2":
            submenu_txt()
        elif opcion == "3":
            submenu_csv()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()

   