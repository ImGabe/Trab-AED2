import time

def combinacoes_minimas(moedas, valor):
    dp = [(float('inf'), []) for _ in range(valor + 1)]
    dp[0] = (0, [[]])  # base: valor 0 -> 0 moedas, combinação vazia

    for v in range(1, valor + 1):
        melhor_qtd = float('inf')
        todas_comb = []
        for m in moedas:
            if v - m >= 0:
                qtd_sub, comb_sub = dp[v - m]
                if qtd_sub + 1 < melhor_qtd:
                    melhor_qtd = qtd_sub + 1
                    todas_comb = [c + [m] for c in comb_sub]
                elif qtd_sub + 1 == melhor_qtd:
                    todas_comb.extend([c + [m] for c in comb_sub])
        dp[v] = (melhor_qtd, todas_comb) #Salva as combinações

    return dp[valor]


moedas = list(map(int, input("Digite as moedas separadas por espaço: ").split()))
valor = int(input("Digite o valor alvo: "))

inicio = time.time()
qtd_min, combinacoes = combinacoes_minimas(moedas, valor)
fim = time.time()

if qtd_min != float('inf'):
    print(f"\nValor mínimo de moedas: {qtd_min}")
    print("Todas as combinações mínimas:")
    for c in combinacoes:
        print(c)
else:
    print("Não é possível formar o valor alvo com essas moedas.")

print(f"\nTempo de execução: {fim - inicio:.6f} segundos")







