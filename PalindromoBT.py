import time

def PalindromoBackingTrack(texto):
    texto = texto.lower()
    palavras = texto.split()

    resultados = []   

    def e_palindromo(s):
        return len(s) > 2 and s == s[::-1]

    def backtrack(palavra, inicio, solucao, encontrados):
        if inicio >= len(palavra):
            return

        for fim in range(inicio + 1, len(palavra) + 1):

            trecho = palavra[inicio:fim]
            solucao.append(trecho)

            if e_palindromo(trecho) and trecho not in encontrados:
                encontrados.append(trecho)

            backtrack(palavra, fim, solucao, encontrados)

            solucao.pop()

    for palavra in palavras:
        encontrados = []

        for inicio in range(len(palavra)):
            backtrack(palavra, inicio, [], encontrados)

        if encontrados:
            resultados.append({
                "palavra": palavra,
                "palindromos": sorted(encontrados, key=len)
            })

    return resultados


# -----------------------------
# Teste
# -----------------------------
texto = "ovo arara ana babab"
resultado = PalindromoBackingTrack(texto)

print("********** Palíndromos Encontrados ******************")

inicio = time.time()
for item in resultado:
    print(f"Palavra: {item['palavra']}")
    print(f"  Palíndromos encontrados: {item['palindromos']}")
fim = time.time()

print(f"Tempo de execução: {fim - inicio:.6f} segundos")




