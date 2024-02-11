"""
Este módulo calcula el total de ventas a partir de un catálogo de productos
y un registro de ventas.
"""

import json
import sys
import time


def load_json_file(file_path):
    """
    Carga y devuelve los datos JSON del archivo especificado.

    Parámetros:
    - file_path: La ruta al archivo JSON a cargar.

    Devuelve:
    Un objeto Python cargado del archivo JSON.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error al cargar archivo {file_path}: {e}")
        sys.exit(1)


def compute_total_sales(product_catalog, sales_record):
    """
    Calcula el costo total de todas las ventas
    basado en el catálogo de productos y el registro de ventas.

    Parámetros:
    - product_catalog: Lista de productos.
    - sales_record: Lista de ventas.

    Devuelve el costo total y el número de errores encontrados.
    """
    product_price_map = {
        product["title"]: product["price"]
        for product in product_catalog}
    total_cost = 0
    errors = 0

    for sale in sales_record:
        try:
            product_price = product_price_map[sale["Product"]]
            total_cost += product_price * sale["Quantity"]
        except KeyError:
            print(f"Error: Producto '{sale['Product']}' no encontrado "
                  f"en el catálogo.")
            errors += 1

    return total_cost, errors


def write_results_to_file(total_cost, errors, elapsed_time):
    """
    Escribe los resultados del cálculo en un archivo llamado SalesResults.txt.

    Parámetros:
    - total_cost: El costo total de todas las ventas.
    - errors: El número de errores encontrados durante el cálculo.
    - elapsed_time: El tiempo tomado para realizar el cálculo.
    """
    with open("SalesResults.txt", 'w', encoding='utf-8') as file:
        file.write(f"Costo Total de Ventas: ${total_cost:.2f}\n")
        file.write(f"Errores: {errors}\n")
        file.write(f"Tiempo Transcurrido: {elapsed_time:.2f} segundos\n")


def main():
    """
    Función principal para cargar archivos, calcular ventas
    y escribir resultados.
    """
    if len(sys.argv) != 3:
        print("Uso: computeSales catalogoDePrecios registroDeVentas")
        sys.exit(1)

    start_time = time.time()
    product_catalog = load_json_file(sys.argv[1])
    sales_record = load_json_file(sys.argv[2])

    total_cost, errors = compute_total_sales(product_catalog, sales_record)
    elapsed_time = time.time() - start_time

    print(f"Costo Total de Ventas: ${total_cost:.2f}")
    print(f"Errores: {errors}")
    print(f"Tiempo Transcurrido: {elapsed_time:.2f} segundos")

    write_results_to_file(total_cost, errors, elapsed_time)


if __name__ == "__main__":
    main()
