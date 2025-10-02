import time

# Gera todas as combinações possíveis de moedas com exatamente qtd moedas
def gerar_combinacoes(moedas, qtd):
    if qtd == 0:
        return [()]  # combinação vazia
    resultado = []
    for m in moedas:
        for comb in gerar_combinacoes(moedas, qtd - 1):
            resultado.append((m,) + comb)
    return resultado


def combinacoes_minimas_forca_bruta(moedas, valor):
    qtd = 1
    while True:  # aumenta o número de moedas até achar solução
        todas = []
        for comb in gerar_combinacoes(moedas, qtd):
            if sum(comb) == valor:
                todas.append(list(comb))
        if todas:  # se encontrou combinações, esse é o mínimo
            return todas
        qtd += 1


# Entrada do usuário
moedas = list(map(int, input("Digite as moedas separadas por espaço: ").split()))
valor = int(input("Digite o valor alvo: "))

inicio = time.time()
combinacoes = combinacoes_minimas_forca_bruta(moedas, valor)
fim = time.time()

print(f"\nValor mínimo de moedas: {len(combinacoes[0])}")
print("Todas as combinações mínimas:")
for c in combinacoes:
    print(c)

print(f"Tempo de execução: {fim - inicio:.6f} segundos")
