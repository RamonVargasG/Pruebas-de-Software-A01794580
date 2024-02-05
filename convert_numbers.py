"""
Programa para convertir números de un archivo a sus representaciones binaria y hexadecimal.
Los resultados se imprimen en pantalla y se guardan en un archivo llamado ConvertionResults.txt.
Maneja los datos inválidos de manera adecuada y registra el tiempo total de ejecución.
"""

import sys
import time

def convertir_a_binario(numero):
    """Convierte un número a su representación binaria sin usar la función bin()."""
    binario = ''
    while numero > 0:
        binario = str(numero % 2) + binario
        numero = numero // 2
    return binario or '0'

def convertir_a_hexadecimal(numero):
    """Convierte un número a su representación hexadecimal sin usar la función hex()."""
    caracteres_hex = '0123456789ABCDEF'
    hexadecimal = ''
    while numero > 0:
        hexadecimal = caracteres_hex[numero % 16] + hexadecimal
        numero = numero // 16
    return hexadecimal or '0'

def procesar_archivo(ruta_archivo):
    """Procesa cada línea del archivo, convierte los números y maneja datos inválidos."""
    resultados = []
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            try:
                numero = int(linea.strip())
                binario = convertir_a_binario(numero)
                hexadecimal = convertir_a_hexadecimal(numero)
                resultados.append(f"{numero}: binario = {binario}, hexadecimal = {hexadecimal}")
            except ValueError:
                print(f"Dato inválido '{linea.strip()}': no es un número entero.")
    return resultados

def escribir_resultados(resultados, tiempo_ejecucion):
    """Escribe los resultados en la consola y en un archivo."""
    with open("ConvertionResults.txt", 'w', encoding='utf-8') as archivo:
        for resultado in resultados:
            print(resultado)
            archivo.write(resultado + "\n")
        resumen = f"Tiempo de ejecución: {tiempo_ejecucion} segundos"
        print(resumen)
        archivo.write(resumen)

if __name__ == "__main__":
    inicio_tiempo = time.time()

    if len(sys.argv) != 2:
        print("Uso: python convert_numbers.py fileWithData.txt")
        sys.exit(1)

    ruta_archivo_entrada = sys.argv[1]
    resultados_proceso = procesar_archivo(ruta_archivo_entrada)
    tiempo_transcurrido = time.time() - inicio_tiempo
    escribir_resultados(resultados_proceso, tiempo_transcurrido)
