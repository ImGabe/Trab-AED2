import time

def max_palavras_palindromicas(texto):
    n = len(texto)
    if n < 2:
        return 0

    dp = [0] * (n + 1)

    inicio = time.time()

    for i in range(1, n + 1):
        dp[i] = dp[i - 1]
        for j in range(i - 1):
            substr = texto[j:i]
            if substr == substr[::-1]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1

    fim = time.time()
    tempo = fim - inicio

    print(f"Texto: '{texto}' | Comprimento: {n}")
    print(f"Tempo de execucao: {tempo:.6f} segundos")
    print(f"Maximo de palavras palindromicas (tamanho >= 2): {dp[n]}")
    return dp[n]

if __name__ == "__main__":
    for txt in ["aa", "ab", "aaa", "aaaa", "aabbaa", "abc", "a"]:
        print("\n" + "-" * 40)
        max_palavras_palindromicas(txt)