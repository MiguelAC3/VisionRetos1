import csv
import math
import random
import time

ROWS = 1000
COLS = 1000
MIN_VALUE = 0
MAX_VALUE = 255


def generate_random_matrix(rows: int = ROWS, cols: int = COLS):
    """Genera una matriz 1000x1000 de enteros aleatorios entre 0 y 255."""
    matrix = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            row.append(random.randint(MIN_VALUE, MAX_VALUE))
        matrix.append(row)
    return matrix


def matrix_statistics(matrix):
    """Calcula mínimo, máximo, media y desviación estándar usando fórmulas matemáticas."""
    flat = []
    total = 0
    minimum = 255
    maximum = 0

    for row in matrix:
        for value in row:
            flat.append(value)
            total += value
            if value < minimum:
                minimum = value
            if value > maximum:
                maximum = value

    count = len(flat)
    if count == 0:
        return {
            "min": 0,
            "max": 0,
            "mean": 0,
            "std": 0,
            "count": 0,
        }

    mean = total / count
    variance = 0.0
    for value in flat:
        diff = value - mean
        variance += diff * diff
    variance /= count
    std_dev = math.sqrt(variance)

    return {
        "min": minimum,
        "max": maximum,
        "mean": mean,
        "std": std_dev,
        "count": count,
    }


def flatten_matrix(matrix):
    """Aplana la matriz a un vector de 1 dimensión."""
    flat = []
    for row in matrix:
        flat.extend(row)
    return flat


def save_matrix_csv(matrix, file_path):
    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(matrix)


def save_flat_vector_txt(vector, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        for value in vector:
            file.write(f"{value}\n")


def save_statistics_txt(stats, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(f"minimo: {stats['min']}\n")
        file.write(f"maximo: {stats['max']}\n")
        file.write(f"media: {stats['mean']}\n")
        file.write(f"desviacion_estandar: {stats['std']}\n")
        file.write(f"num_valores: {stats['count']}\n")


def main():
    start_total = time.perf_counter()

    start_create = time.perf_counter()
    matrix = generate_random_matrix(ROWS, COLS)
    create_time = time.perf_counter() - start_create

    start_stats = time.perf_counter()
    stats = matrix_statistics(matrix)
    stats_time = time.perf_counter() - start_stats

    flat_vector = flatten_matrix(matrix)
    total_time = time.perf_counter() - start_total

    csv_path = "matriz_1000x1000.csv"
    txt_vector_path = "vector_aplanado_1000x1000.txt"
    txt_stats_path = "estadisticas_1000x1000.txt"

    save_matrix_csv(matrix, csv_path)
    save_flat_vector_txt(flat_vector, txt_vector_path)
    save_statistics_txt(stats, txt_stats_path)

    print("Matriz generada:", ROWS, "x", COLS)
    print(f"Tiempo de creación: {create_time:.6f} segundos")
    print(f"Tiempo de cálculo estadístico: {stats_time:.6f} segundos")
    print(f"Tiempo total: {total_time:.6f} segundos")
    print(f"Mínimo: {stats['min']}")
    print(f"Máximo: {stats['max']}")
    print(f"Media: {stats['mean']}")
    print(f"Desviación estándar: {stats['std']}")
    print(f"Archivo CSV guardado en: {csv_path}")
    print(f"Vector aplanado guardado en: {txt_vector_path}")
    print(f"Estadísticas guardadas en: {txt_stats_path}")


if __name__ == "__main__":
    main()
