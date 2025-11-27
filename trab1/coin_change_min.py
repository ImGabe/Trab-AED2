import time
from functools import lru_cache


def todas_combinacoes_minimas(moedas, valor):
    @lru_cache(maxsize=None)  # cache vazio inicialmente
    def dp(restante):
        if restante == 0:
            return 0, [[]]  # 0 moedas, 1 combinação vazia(caso base)
        if restante < 0:
            return float("inf"), []

        melhor_qtd = float("inf")
        todas_comb = []

        for m in moedas:
            qtd_sub, comb_sub = dp(restante - m)
            if qtd_sub + 1 < melhor_qtd:
                # Encontrou uma nova quantidade mínima
                melhor_qtd = qtd_sub + 1
                todas_comb = [c + [m] for c in comb_sub]
            elif qtd_sub + 1 == melhor_qtd:
                # Encontrou outra combinação com mesma quantidade mínima
                todas_comb.extend([c + [m] for c in comb_sub])

        return melhor_qtd, todas_comb  # salva combinação

    return dp(valor)


# Entrada:
moedas = [1, 3, 4]
valor = 6

inicio = time.time()
qtd_min, combinacoes = todas_combinacoes_minimas(moedas, valor)
fim = time.time()

if qtd_min != float("inf"):
    print(f"Valor mínimo de moedas: {qtd_min}")
    print("Combinações mínimas:")
    for c in combinacoes:
        print(c)
else:
    print("Não é possível formar o valor alvo com essas moedas.")

print(f"Tempo de execução: {fim - inicio:.6f} segundos")
