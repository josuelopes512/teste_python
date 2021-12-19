# -*- coding: utf-8 -*-

with open('treinamento.txt', mode='r') as f:
    treinamento = f.read()


print(treinamento[:500])
len(treinamento)
texto_exemplo = 'Olá, tudo bem?'
tokens = texto_exemplo.split()
print(tokens)
len(tokens)


import nltk
nltk.download('punkt')

palavras_separadas = nltk.tokenize.word_tokenize(texto_exemplo)
print(palavras_separadas)
len(palavras_separadas)
'/.'.isalpha()
'à'.isalpha()

def separa_palavras(lista_tokens):
    lista_palavras = []
    for token in lista_tokens:
        if token.isalpha():
            lista_palavras.append(token)
    return lista_palavras

separa_palavras(palavras_separadas)

lista_tokens = nltk.tokenize.word_tokenize(treinamento)
lista_palavras = separa_palavras(lista_tokens)

print(f'O número total de palavras em nosso corpus é {len(lista_palavras)}')
print(lista_palavras[:5])

def normalizacao(lista_palavras):
    lista_normalizada = []
    for palavra in lista_palavras:
        lista_normalizada.append(palavra.lower())
    return lista_normalizada
lista_normalizada = normalizacao(lista_palavras)
print(lista_normalizada[:5])
set([1, 2, 3, 3, 3, 4, 5, 6, 6])
print(f'O número total de palavras que nosso corretor "sabe" de fato é {len(set(lista_normalizada))}')
palavra_exemplo = 'programaão'

(palavra_exemplo[:8], palavra_exemplo[8:])

print(f'{palavra_exemplo[:8]} + "a letra faltante (ç)" + {palavra_exemplo[8:]}'
      f'\n\nResulta na palavra \n\n\t{palavra_exemplo[:8] + "ç" + palavra_exemplo[8:]}')

def insere_letras(fatias):
    novas_palavras = []
    letras = 'abcedfghijklmnopqrstuvwxyzáâàãéêèíîìóôòõúûùç'
    for esquerdo, direito in fatias:
        for letra in letras:
            novas_palavras.append(esquerdo + letra + direito)
    return novas_palavras

insere_letras([('programa', 'ão')])[:5]

def gerador_palavras(palavra):
    fatias = []
    for i in range(len(palavra) + 1):
        fatias.append((palavra[:i], palavra[i:]))
    palavras_geradas = insere_letras(fatias)
    return palavras_geradas

palavras_geradas = gerador_palavras(palavra_exemplo)
print(palavras_geradas[:5])

for palavra in palavras_geradas:
    if palavra == 'programação':
        print(f'A palavra correta é "{palavra}" e ela está dentro da lista palavras_geradas')

print(f'Foram geradas {len(palavras_geradas)} palavras')
frequencia = nltk.FreqDist(lista_normalizada)
total_palavras = len(lista_normalizada)
frequencia.most_common(10)

def probabilidade(palavra_gerada):
    return frequencia[palavra_gerada] / total_palavras

def corretor(palavra_errada):
    palavras_geradas = gerador_palavras(palavra_errada)
    palavra_correta = max(palavras_geradas, key=probabilidade)
    return palavra_correta

palavra_exemplo = 'programaão'
corretor(palavra_exemplo)
teste = 'lgica'
print(f'Você quis dizer: {corretor(teste)}')

def cria_dados_teste(nome_arquivo):
    lista_palavras_teste = []
    f = open(nome_arquivo, 'r')
    for linha in f:
        correta, errada = linha.split()
        lista_palavras_teste.append((correta, errada))
    f.close()
    return lista_palavras_teste

lista_teste = cria_dados_teste('palavras.txt')


def avaliador(testes):
    numero_palavras = len(testes)
    acertou = 0
    for correta, errada in testes:
        palavra_corrigida = corretor(errada)
        if palavra_corrigida == correta:
            acertou += 1
    taxa_acerto = round(acertou * 100 / numero_palavras, 2)
    print(f'{taxa_acerto}% de {numero_palavras} palavras')

avaliador(lista_teste)

def deletando_caracter(fatias):
    novas_palavras = []
    for esquerdo, direito in fatias:
        novas_palavras.append(esquerdo + direito[1:])
    return novas_palavras

exemplo = [('progr', 'samação')]

deletando_caracter(exemplo)

def gerador_palavras(palavra):
    fatias = []
    for i in range(len(palavra) + 1):
        fatias.append((palavra[:i], palavra[i:]))
    palavras_geradas = insere_letras(fatias)
    palavras_geradas += deletando_caracter(fatias)
    return palavras_geradas

palavra_exemplo = 'progrsamação'

palavras_geradas = gerador_palavras(palavra_exemplo)

print(palavras_geradas[:5])
for palavra in palavras_geradas:
    if palavra == 'programação':
        print(f'A palavra correta é "{palavra}" e ela está dentro da lista palavras_geradas')

print(f'Foram geradas {len(palavras_geradas)} palavras')
avaliador(lista_teste)

def troca_caracter(fatias):
    novas_palavras = []
    letras = 'abcedfghijklmnopqrstuvwxyzáâàãéêèíîìóôòõúûùç'
    for esquerdo, direito in fatias:
        for letra in letras:
            novas_palavras.append(esquerdo + letra + direito[1:])
    return novas_palavras

troca_caracter([('prog', 'tamação')])[:5]


def gerador_palavras(palavra):
    fatias = []
    for i in range(len(palavra) + 1):
        fatias.append((palavra[:i], palavra[i:]))
    palavras_geradas = insere_letras(fatias)
    palavras_geradas += deletando_caracter(fatias)
    palavras_geradas += troca_caracter(fatias)
    return palavras_geradas

palavra_exemplo = 'progtamação'
palavras_geradas = gerador_palavras(palavra_exemplo)
print(palavras_geradas[:5])

for palavra in palavras_geradas:
    if palavra == 'programação':
        print(f'A palavra correta é "{palavra}" e ela está dentro da lista palavras_geradas')

def insere_letras(fatias):
    novas_palavras = []
    letras = 'abcedfghijklmnopqrstuvwxyzáâàãéêèíîìóôòõúûùç'
    for esquerdo, direito in fatias:
        for letra in letras:
            novas_palavras.append(esquerdo + letra + direito)
    return novas_palavras

######################## Função deletando_caracter() ##########################

def deletando_caracter(fatias):
    novas_palavras = []
    for esquerdo, direito in fatias:
        novas_palavras.append(esquerdo + direito[1:])
    return novas_palavras

######################## Função trocando_caracter() ###########################

def troca_caracter(fatias):
    novas_palavras = []
    letras = 'abcedfghijklmnopqrstuvwxyzáâàãéêèíîìóôòõúûùç'
    for esquerdo, direito in fatias:
        for letra in letras:
            novas_palavras.append(esquerdo + letra + direito[1:])
    return novas_palavras

####################### Função invertendo_caracter() ##########################

def invertendo_caracter(fatias):
    novas_palavras = []
    for esquerdo, direito in fatias:
        if len(direito) > 1:
            novas_palavras.append(esquerdo + direito[1] + direito[0] + direito[2:])
    return novas_palavras

######################### Função gerador_palavras() ###########################
def gerador_palavras(palavra):
    fatias = []
    for i in range(len(palavra) + 1):
        fatias.append((palavra[:i], palavra[i:]))
    palavras_geradas = insere_letras(fatias)
    palavras_geradas += deletando_caracter(fatias)
    palavras_geradas += troca_caracter(fatias)
    palavras_geradas += invertendo_caracter(fatias)
    return palavras_geradas


################################# AVALIANDO ###################################

palavra_exemplo = 'prorgamação'
palavras_geradas = gerador_palavras(palavra_exemplo)
print(palavras_geradas[:5])
for palavra in palavras_geradas:

    if palavra == 'programação':

        print(f'A palavra correta é "{palavra}" e ela está dentro da lista palavras_geradas')

avaliador(lista_teste)

def avaliador(testes, vocabulario):
    numero_palavras = len(testes)
    acertou = desconhecidas = 0
    for correta, errada in testes:
        palavra_corrigida = corretor(errada)
        desconhecidas += (correta not in vocabulario)
        if palavra_corrigida == correta:
            acertou += 1
    
    taxa_acerto = round(acertou * 100 / numero_palavras, 2)
    taxa_desconhecidas = round(desconhecidas * 100 / numero_palavras, 2)
    print(f'{taxa_acerto}% de {numero_palavras} das palavras conhecidas\n'
          f'e {taxa_desconhecidas}% das palavras desconhecidas')

vocabulario = set(lista_normalizada)
avaliador(lista_teste, vocabulario)
palavra_exemplo = 'prorrgramação'
corretor(palavra_exemplo)

def gerador_inception(palavras_geradas):
    novas_palavras = []
    for palavra in palavras_geradas:
        novas_palavras += gerador_palavras(palavra)
    return novas_palavras


palavras_geradas = gerador_inception(gerador_palavras(palavra_exemplo))
print(f'A quantidade de possíveis palavras geradas é {len(palavras_geradas)}')


'programação' in palavras_geradas

def corretor_super_sayajin(palavra_errada):
    palavras_geradas = gerador_palavras(palavra_errada)
    palavras_inception = gerador_inception(palavras_geradas)
    todas_palavras = set(palavras_geradas + palavras_inception)
    candidatos = [palavra_errada]
    for palavra in todas_palavras:
        if palavra in vocabulario:
            candidatos.append(palavra)
    print(f'Temos {len(candidatos)} candidatos a palavra correta.\n'
          f'São eles {candidatos}')

    palavra_correta = max(candidatos, key=probabilidade)

    return palavra_correta


antes = corretor(palavra_exemplo)

print('Antiga função corretor()\n'
      '========================\n\n'
     f'Entrada ==> {palavra_exemplo}\n'
     f'Retorno ==> {antes}')

print('Com a novoa função corretor_super_sayajin():\n')

depois = corretor_super_sayajin(palavra_exemplo)

print('\nNova função nova função corretor_super_sayajin()\n'
      '==============================================\n\n'
     f'Entrada ==> {palavra_exemplo}\n'
     f'Retorno ==> {depois}')


def corretor_super_sayajin(palavra_errada):
    palavras_geradas = gerador_palavras(palavra_errada)
    palavras_inception = gerador_inception(palavras_geradas)
    todas_palavras = set(palavras_geradas + palavras_inception)
    candidatos = [palavra_errada]
    for palavra in todas_palavras:
        if palavra in vocabulario:
            candidatos.append(palavra)
    palavra_correta = max(candidatos, key=probabilidade)
    return palavra_correta

corretor_super_sayajin(palavra_exemplo)

def avaliador(testes, vocabulario):
    numero_palavras = len(testes)
    acertou = desconhecidas = 0
    for correta, errada in testes:
        palavra_corrigida = corretor_super_sayajin(errada)
        desconhecidas += (correta not in vocabulario)
        if palavra_corrigida == correta:
            acertou += 1
    taxa_acerto = round(acertou * 100 / numero_palavras, 2)
    taxa_desconhecidas = round(desconhecidas * 100 / numero_palavras, 2)
    print(f'{taxa_acerto}% de {numero_palavras} das palavras conhecidas\n'
          f'e {taxa_desconhecidas}% das palavras desconhecidas')

vocabulario = set(lista_normalizada)

avaliador(lista_teste, vocabulario)

def avaliador(testes, vocabulario):
    numero_palavras = len(testes)
    acertou = desconhecidas = 0
    for correta, errada in testes:
        palavra_corrigida = corretor_super_sayajin(errada)
        desconhecidas += (correta not in vocabulario)
        if palavra_corrigida == correta:
            acertou += 1
        else:
            print(f"{errada} - {corretor(errada)} - {palavra_corrigida}")
    taxa_acerto = round(acertou * 100 / numero_palavras, 2)
    taxa_desconhecidas = round(desconhecidas * 100 / numero_palavras, 2)
    print(f'\n\n{taxa_acerto}% de {numero_palavras} das palavras conhecidas\n'
          f'e {taxa_desconhecidas}% das palavras desconhecidas')


vocabulario = set(lista_normalizada)


avaliador(lista_teste, vocabulario)

########################### Função insere_letras() ############################

def insere_letras(fatias):
    novas_palavras = []
    letras = 'abcedfghijklmnopqrstuvwxyzáâàãéêèíîìóôòõúûùç'
    for esquerdo, direito in fatias:
        for letra in letras:
            novas_palavras.append(esquerdo + letra + direito)
    return novas_palavras

######################## Função deletando_caracter() ##########################

def deletando_caracter(fatias):
    novas_palavras = []
    for esquerdo, direito in fatias:
        novas_palavras.append(esquerdo + direito[1:])
    return novas_palavras

######################## Função trocando_caracter() ###########################

def troca_caracter(fatias):
    novas_palavras = []
    letras = 'abcedfghijklmnopqrstuvwxyzáâàãéêèíîìóôòõúûùç'
    for esquerdo, direito in fatias:
        for letra in letras:
            novas_palavras.append(esquerdo + letra + direito[1:])
    return novas_palavras

####################### Função invertendo_caracter() ##########################

def invertendo_caracter(fatias):
    novas_palavras = []
    for esquerdo, direito in fatias:
        if len(direito) > 1:
            novas_palavras.append(esquerdo + direito[1] + direito[0] + direito[2:])
    return novas_palavras

######################### Função gerador_palavras() ###########################

# Refatorando outra vez a função gerador_palavras()
def gerador_palavras(palavra):
    fatias = []
    for i in range(len(palavra) + 1):
        fatias.append((palavra[:i], palavra[i:]))
    palavras_geradas = insere_letras(fatias)
    palavras_geradas += deletando_caracter(fatias)
    palavras_geradas += troca_caracter(fatias)
    palavras_geradas += invertendo_caracter(fatias)
    return palavras_geradas

############################# Função avaliador() ###############################

def avaliador(testes, vocabulario):
    numero_palavras = len(testes)
    acertou = desconhecidas = 0
    for correta, errada in testes:
        palavra_corrigida = corretor(errada)
        desconhecidas += (correta not in vocabulario)
        if palavra_corrigida == correta:
            acertou += 1
    taxa_acerto = round(acertou * 100 / numero_palavras, 2)
    taxa_desconhecidas = round(desconhecidas * 100 / numero_palavras, 2)
    print(f'{taxa_acerto}% de {numero_palavras} das palavras conhecidas\n'
          f'e {taxa_desconhecidas}% das palavras desconhecidas')

vocabulario = set(lista_normalizada)

avaliador(lista_teste, vocabulario)


teste = 'odontoolgia'

print(f'Entrada =================> {teste}\nResposta do corretor() ==> {corretor(teste)}')

