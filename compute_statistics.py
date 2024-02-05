"""
Programa que proporciona funcionalidad para calcular estadísticas descriptivas   
(media, mediana, moda, desviación estándar y varianza) para una lista de números proporcionada,
calcula estadísticas y registra el tiempo de ejecución.
"""

import sys
import time

def read_data(input_file_path):
    """
    Lee datos numéricos de un archivo, ignorando entradas inválidas.

    Parámetros:
    - input_file_path: Ruta al archivo que contiene datos numéricos.

    Devuelve:
    Una lista de números extraídos del archivo.
    """
    data = []
    with open(input_file_path, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                num = float(line.strip())
                data.append(num)
            except ValueError as e:
                print(f"Dato inválido '{line.strip()}': {e}")
    return data

def calculate_mean(data):
    """
    Calcula la media de una lista de números.

    Parámetros:
    - data: Lista de números.

    Devuelve:
    La media de los números.
    """
    return sum(data) / len(data) if data else 0

def calculate_median(data):
    """
    Calcula la mediana de una lista de números.

    Parámetros:
    - data: Lista de números.

    Devuelve:
    La mediana de los números.
    """
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        return sorted_data[mid]

def calculate_mode(data):
    """
    Calcula la moda(s) de una lista de números.

    Parámetros:
    - data: Lista de números.

    Devuelve:
    Una lista que contiene la(s) moda(s) de los números.
    """
    frequency = {}
    for number in data:
        frequency[number] = frequency.get(number, 0) + 1
    max_frequency = max(frequency.values(), default=0)
    mode = [key for key, val in frequency.items() if val == max_frequency]
    return mode[0] if len(mode) == 1 else mode

def calculate_variance(data, mean):
    """
    Calcula la varianza de una lista de números.

    Parámetros:
    - data: Lista de números.
    - mean: La media de los números.

    Devuelve:
    La varianza de los números.
    """
    return sum((x - mean) ** 2 for x in data) / (len(data) - 1) if len(data) > 1 else 0

def calculate_std_dev(variance):
    """
    Calcula la desviación estándar a partir de la varianza.

    Parámetros:
    - variance: La varianza de una lista de números.

    Devuelve:
    La desviación estándar de los números.
    """
    return variance ** 0.5

def write_results(result_file, results):
    """
    Escribe las estadísticas calculadas tanto en la consola como en un archivo.

    Parámetros:
    - result_file: El nombre del archivo en el que se escribirán los resultados.
    - results: Diccionario que contiene los resultados del cálculo estadístico.
    """
    with open(result_file, 'w', encoding='utf-8') as file:
        for key, value in results.items():
            line = f"{key}: {value}\n"
            file.write(line)
            print(line.strip())

if __name__ == "__main__":
    start_time = time.time()

    if len(sys.argv) != 2:
        print("Uso: python computeStatistics.py fileWithData.txt")
        sys.exit(1)

    FILE_PATH = sys.argv[1]
    DATA = read_data(FILE_PATH)

    if not DATA:
        print("No hay datos válidos para calcular estadísticas.")
        sys.exit(1)

    MEAN = calculate_mean(DATA)
    MEDIAN = calculate_median(DATA)
    MODE = calculate_mode(DATA)
    VARIANCE = calculate_variance(DATA, MEAN)
    STD_DEV = calculate_std_dev(VARIANCE)

    elapsed_time = time.time() - start_time
    RESULTS = {
        "Media": MEAN,
        "Mediana": MEDIAN,
        "Moda": MODE,
        "Desviación Estándar": STD_DEV,
        "Varianza": VARIANCE,
        "Tiempo Transcurrido (segundos)": elapsed_time
    }

    write_results("StatisticsResults.txt", RESULTS)
