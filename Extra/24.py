"""Um vetor é palíndromo se ele não se alterar quando o mesmo for invertido. Escreva um programa que verifique se um vetor é palíndromo, fazendo comparação de índice/posição por índice/posição do vetor original (vo) com o vetor invertido (vi). Não use nenhuma função pronta da linguagem Python. A tamanho do vetor pode ser da sua escolha.
Exemplo: vetor original vo = {1, 3, 5, 2, 2, 5, 3, 1}
vetor invertido é vi = {1, 3, 5, 2, 2, 5, 3, 1} O vetor invertido é palíndromo, pois ele invertido é igual ao original

vetor original vo = {9, 7, 5, 2, 4, 5, 3, 6}
vetor invertido é vi = {6, 3, 5, 4, 2, 5, 7, 9} O vetor invertido não é palíndromo, pois ele invertido é igual ao original"""

vo = []
vi = []

for i in range(5):
    vo.append(int(input('Insira um número inteiro: ')))

for i in range(len(vo)-1, -1, -1):
    vi.append(vo[i])

print("\n", vo)

print("\n", vi)

if vo == vi:
    print("\nEsse vetor é um palíndromo")
else:
    print("\nEsse vetor não é um palíndromo")
