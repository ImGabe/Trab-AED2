import time


# Complexidade: O(n)
def is_palindrome(word: str) -> bool:
    return word == word[::-1]

# Complexidade: O(n^3)
def greedy_palindrome_partition(sequence: str) -> list[str]:
    if not sequence:
        return []

    n = len(sequence)
    partitions = []
    start_index = 0

    while start_index < n:
        for end_index in range(n, start_index, -1):
            substring = sequence[start_index:end_index]

            if is_palindrome(substring):
                partitions.append(substring)
                start_index = end_index
                break

    return partitions


def run_test_case(label: str, sequence: str):
    print()
    print(label)
    print(f"Entrada: '{sequence}'")

    start_time = time.perf_counter()

    result = greedy_palindrome_partition(sequence)

    end_time = time.perf_counter()

    duration_ms = (end_time - start_time) * 1000

    print(f"saida: {result}")
    print(f"número de cortes: {len(result) - 1}")
    print(f"tempo de execução: {duration_ms:.6f} ms")


def main():
    run_test_case("caso básico", "ovo-arara")
    run_test_case("pior caso (sem palíndromos)", "abcdefghijklmnopqrstuvwxyz")
    run_test_case("melhor caso (tudo palíndromo)", "ovo")


if __name__ == "__main__":
    main()