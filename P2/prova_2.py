'''Foi realizada uma pesquisa sobre algumas características físicas de ALGUNS habitantes de uma região, NÃO FOI INFORMADA A QUANTIDADE TOTAL, então use como critério de parada, idade igual a zero para encerrar a repetição. Preste atenção nesse detalhe, pois somente poderá usar a função append, quando for digitado uma idade válida.
Foram coletados os seguintes dados de cada habitante: idade, sexo (M/F), cor dos olhos (A - azuis ou C - castanhos). Escolha se quer armazenar uma letra ou a palavra, para cor dos olhos.
Em Python crie um programa que leia esses dados, armazenando-os em vetores, uma para idade, outro para sexo (apenas uma letra) e outro para cor dos olhos.
Calcule e apresente:
Média de idades das pessoas com olhos castanhos;

Quantidade de pessoas que foram entrevistadas

Quantidade de pessoas do sexo feminino com idade entre 18 e 35 anos(inclusive) e que tenham olhos azuis.

Observação: pode usar o operador in e a função len() apenas. Outras funções prontas da linguagem Python, não serão aceitas.'''

vetor_idade = []
vetor_sexo = []
vetor_olhos = []

while True:
    idade = int(input('Digite sua idade: '))

    if idade == 0:
        break

    sexo = input('Digite o sexo [M/F]: ').upper().strip()[0]
    olhos = input('Digite a cor dos olhos [A/C]: ').upper().strip()[0]

    vetor_idade.append(idade)
    vetor_sexo.append(sexo)
    vetor_olhos.append(olhos)

total_idade_castanho = 0
idade_castanho = 0
mulheres_criterio = 0

for i in range (len(vetor_idade)):
    if vetor_olhos[i] == 'C':
        idade_castanho += vetor_idade[i]
        total_idade_castanho += 1

    if vetor_sexo[i] == 'F' and 18 <= vetor_idade[i] <=35 and vetor_olhos[i] == 'A':
        mulheres_criterio += 1 

print('Média de idade de pessoas com olhos castanhos:', idade_castanho / total_idade_castanho)
print('Quantidade de pessoas entrevistadas:', len(vetor_idade))
print('Quantidade de mulheres entre 18 a 35 anos com olhos azuis:', mulheres_criterio)
