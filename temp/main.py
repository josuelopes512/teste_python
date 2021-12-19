import nltk
from nltk.util import pr
nltk.download('punkt')


with open('br-sem-acentos.txt', mode='r') as f:
    treinamento = f.read()
    
# print(treinamento[:500])

# print(len(treinamento))


texto_exemplo = 'Olá, tudo bem?'


palavras_separadas = nltk.tokenize.word_tokenize(texto_exemplo)
lista_tokens = nltk.tokenize.word_tokenize(treinamento)


lista_palavras = [token for token in palavras_separadas if token.isalpha()]
lista_palavras_tokens = sorted([token.lower() for token in lista_tokens if token.isalpha()])
# print(lista_palavras_tokens)

def insere_letras(fatias):
    novas_palavras = []
    letras = 'abcedfghijklmnopqrstuvwxyzáâàãéêèíîìóôòõúûùç'
    for esquerdo, direito in fatias:
        for letra in letras:
            novas_palavras.append(esquerdo + letra + direito)
    return novas_palavras

# print(insere_letras([('programa', 'ão')]))
palavra_exemplo = 'programaão'


def gerador_palavras(palavra):
    # Criando uma lista vazia para armazenar as duas fatias de cada palavra
    fatias = []
    # Iterando por cada letra de cada palavra
    for i in range(len(palavra) + 1):
        # Armazenando as duas fatias em uma tupla e essa tupla em uma lista
        print(palavra[:i], palavra[i:])
        fatias.append((palavra[:i], palavra[i:]))
    # Chamando a função insere_letras() com a lista de tuplas das fatias 
        # recém-criadas e armazenando o retorno dessa função em uma variável
    palavras_geradas = insere_letras(fatias)
    # Retornando a lista de possíveis palavras. A palavra correta estará aí no meio
    return palavras_geradas

# Chamando a função gerador_palavras() com a pallavra_exemplo como parãmetro
    # e armazenando a lista que ela retorna em uma variável
palavras_geradas = gerador_palavras(palavra_exemplo)


for palavra in palavras_geradas:
    # Selecionando a palavra correta
    if palavra == 'programação':
        # Mostrando que a palavra correta está dentro dessa lista
        print(f'A palavra correta é "{palavra}" e ela está dentro da lista palavras_geradas')


frequencia = nltk.FreqDist(lista_palavras_tokens)

# Calculando o total de palavras e armazenando esse número em uma variável
total_palavras = len(lista_palavras_tokens)

# Mostrando as 10 palavras mais comuns da nossa lista_normalizada
frequencia.most_common(10)

print(frequencia.most_common(100))