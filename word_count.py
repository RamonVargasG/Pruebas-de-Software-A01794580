"""
Programa que cuenta la frecuencia de cada palabra en un archivo de texto.
Imprime los resultados en la consola y los escribe en un archivo llamado WordCountResults.txt.
"""

import sys
import time

def count_words(file_path):
    """
    Cuenta la frecuencia de cada palabra distinta en el archivo especificado.

    :param file_path: Ruta al archivo de texto a analizar.
    :return: Un diccionario con las palabras como claves y sus frecuencias como valores.
    """
    word_count = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as file:  # Especificar codificación
            for line in file:
                words = line.strip().split()
                for word in words:
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1
    except FileNotFoundError:
        print(f"Error: Archivo no encontrado {file_path}")
    except IOError as e:
        print(f"Error al leer el archivo {file_path}: {e}")
    return word_count

def write_results_to_file(word_count, execution_time):
    """
    Escribe los conteos de palabras y el tiempo de ejecución en un archivo.

    :param word_count: Diccionario de conteos de palabras.
    :param execution_time: Tiempo tomado para ejecutar la operación de conteo de palabras.
    """
    with open("WordCountResults.txt", 'w', encoding='utf-8') as file:  # Especificar codificación
        for word, count in word_count.items():
            file.write(f"{word}: {count}\n")
        file.write(f"\nTiempo de ejecución: {execution_time:.4f} segundos")

def main():
    """
    Función principal para ejecutar el script. Requiere un nombre de archivo como argumento.
    """
    if len(sys.argv) != 2:
        print("Uso: python wordCount.py fileWithData.txt")
        return

    start_time = time.time()
    file_path = sys.argv[1]
    word_count = count_words(file_path)
    execution_time = time.time() - start_time

    for word, count in word_count.items():
        print(f"{word}: {count}")
    print(f"\nTiempo de ejecución: {execution_time:.4f} segundos")

    write_results_to_file(word_count, execution_time)

if __name__ == "__main__":
    main()
