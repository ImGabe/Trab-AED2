import random
import time


def split(matrix):
    n = len(matrix)
    mid = n // 2

    top = matrix[:mid]

    top_left = [row[:mid] for row in top]
    top_right = [row[mid:] for row in top]

    bottom = matrix[mid:]

    bottom_left = [row[:mid] for row in bottom]
    bottom_right = [row[mid:] for row in bottom]

    return top_left, top_right, bottom_left, bottom_right


def add_matrix(A, B):
    return [[a + b for a, b in zip(row_a, row_b)] for row_a, row_b in zip(A, B)]


def subtract_matrix(A, B):
    return [[a - b for a, b in zip(row_a, row_b)] for row_a, row_b in zip(A, B)]


def join_matrices(C11, C12, C21, C22):
    top = [a + b for (a, b) in zip(C11, C12)]
    bottom = [a + b for (a, b) in zip(C21, C22)]

    return top + bottom


def strassens(A, B):
    n = len(A)

    if n == 1:
        return [[A[0][0] * B[0][0]]]
    else:
        A11, A12, A21, A22 = split(A)
        B11, B12, B21, B22 = split(B)

        M1 = strassens(add_matrix(A11, A22), add_matrix(B11, B22))
        M2 = strassens(add_matrix(A21, A22), B11)
        M3 = strassens(A11, subtract_matrix(B12, B22))
        M4 = strassens(A22, subtract_matrix(B21, B11))
        M5 = strassens(add_matrix(A11, A12), B22)
        M6 = strassens(subtract_matrix(A21, A11), add_matrix(B11, B12))
        M7 = strassens(subtract_matrix(A12, A22), add_matrix(B21, B22))

        T1 = add_matrix(M1, M4)
        T2 = subtract_matrix(T1, M5)
        C11 = add_matrix(T2, M7)

        C12 = add_matrix(M3, M5)

        C21 = add_matrix(M2, M4)

        T3 = add_matrix(M1, M3)
        T4 = subtract_matrix(T3, M2)
        C22 = add_matrix(T4, M6)

        C = join_matrices(C11, C12, C21, C22)

        return C


def generate_matrix(n):
    return [[random.randint(1, 9) for _ in range(n)] for _ in range(n)]


def naive_multiply(A, B):
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C


def main():
    test_sizes = [64, 128, 256, 512, 1024]

    for n in test_sizes:
        print(f"\n--- INICIANDO TESTE PARA MATRIZ DE TAMANHO {n}x{n} ---")

        print(f"[{time.strftime('%H:%M:%S')}] Gerando matrizes...")
        A = generate_matrix(n)
        B = generate_matrix(n)

        print(f"[{time.strftime('%H:%M:%S')}] Executando Strassen...")
        start_strassens = time.perf_counter()
        strassens_result = strassens(A, B)
        end_strassens = time.perf_counter()
        total_strassens_time = end_strassens - start_strassens
        print(f"- Tempo de execução (Strassen): {total_strassens_time:.6f} segundos")

        print(f"[{time.strftime('%H:%M:%S')}] Executando Força Bruta...")
        start_naive = time.perf_counter()
        naive_result = naive_multiply(A, B)
        end_naive = time.perf_counter()
        total_naive_time = end_naive - start_naive
        print(f"- Tempo de execução (Força Bruta): {total_naive_time:.6f} segundos")

        print()

        if total_strassens_time < total_naive_time:
            speedup = total_naive_time / total_strassens_time
            print(f"Strassen foi mais rápido por um fator de {speedup:.2f}x")
        else:
            slowdown = total_strassens_time / total_naive_time
            print(f"Força Bruta foi mais rápido por um fator de {slowdown:.2f}x")

        assert strassens_result == naive_result, (
            f"ERRO: Os resultados não são iguais para {n}x{n}!"
        )


if __name__ == "__main__":
    main()
