import random


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
    for n in [1, 2, 4, 8, 16, 32, 64, 128]:
        A = generate_matrix(n)
        B = generate_matrix(n)

        strassens_result = strassens(A, B)
        naive_result = naive_multiply(A, B)

        assert strassens_result == naive_result, f"Erro na matriz de tamanho {n}x{n}!"

    print("Todos os testes passaram!")


if __name__ == "__main__":
    main()
