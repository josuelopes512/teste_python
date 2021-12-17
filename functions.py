def separa_palavras(lista_tokens):
    return [token for token in lista_tokens if token.isalpha()]

def normalizacao(lista_palavras):
    return [palavra.lower() for palavra in lista_palavras]

def insere_letras(fatias):
    letras = 'abcedfghijklmnopqrstuvwxyzáâàãéêèíîìóôòõúûùç'
    return [esquerdo + letra + direito for esquerdo, direito in fatias for letra in letras]

def gerador_palavras(palavra):
    return insere_letras([(palavra[:i], palavra[i:]) for i in range(len(palavra) + 1)])

def probabilidade(palavra_gerada):
    return frequencia[palavra_gerada] / total_palavras

def corretor(palavra_errada):
    return max(gerador_palavras(palavra_errada), key=probabilidade)

def cria_dados_teste(nome_arquivo):
    lista_palavras_teste = []
    f = open(nome_arquivo, 'r')
    for linha in f:
        correta, errada = linha.split()
        lista_palavras_teste.append((correta, errada))
    f.close()
    return lista_palavras_teste

def avaliador(testes):
    numero_palavras = len(testes)
    acertou = 0
    for correta, errada in testes:
        palavra_corrigida = corretor(errada)
        if palavra_corrigida == correta:
            acertou += 1
    taxa_acerto = round(acertou * 100 / numero_palavras, 2)
    print(f'{taxa_acerto}% de {numero_palavras} palavras')

def deletando_caracter(fatias):
    return [esquerdo + direito[1:] for esquerdo, direito in fatias]

def gerador_palavras(palavra):
    fatias = [(palavra[:i], palavra[i:]) for i in range(len(palavra) + 1)]
    palavras_geradas = insere_letras(fatias)
    palavras_geradas += deletando_caracter(fatias)
    return palavras_geradas

def troca_caracter(fatias):
    letras = 'abcedfghijklmnopqrstuvwxyzáâàãéêèíîìóôòõúûùç'
    return [esquerdo + letra + direito[1:] for esquerdo, direito in fatias for letra in letras]

def gerador_palavras(palavra):
    fatias = [(palavra[:i], palavra[i:]) for i in range(len(palavra) + 1)]
    palavras_geradas = insere_letras(fatias)
    palavras_geradas += deletando_caracter(fatias)
    palavras_geradas += troca_caracter(fatias)
    return palavras_geradas

def insere_letras(fatias):
    letras = 'abcedfghijklmnopqrstuvwxyzáâàãéêèíîìóôòõúûùç'
    return [esquerdo + letra + direito for esquerdo, direito in fatias for letra in letras]

def deletando_caracter(fatias):
    return [esquerdo + direito[1:] for esquerdo, direito in fatias]

def troca_caracter(fatias):
    letras = 'abcedfghijklmnopqrstuvwxyzáâàãéêèíîìóôòõúûùç'
    return [esquerdo + letra + direito[1:] for esquerdo, direito in fatias for letra in letras]

def invertendo_caracter(fatias):
    return [esquerdo + direito[1] + direito[0] + direito[2:] for esquerdo, direito in fatias if len(direito) > 1]

def gerador_palavras(palavra):
    fatias = [(palavra[:i], palavra[i:]) for i in range(len(palavra) + 1)]
    palavras_geradas = insere_letras(fatias)
    palavras_geradas += deletando_caracter(fatias)
    palavras_geradas += troca_caracter(fatias)
    palavras_geradas += invertendo_caracter(fatias)
    return palavras_geradas

def avaliador_v1(testes, vocabulario):
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

def gerador_inception(palavras_geradas):
    novas_palavras = []
    for palavra in palavras_geradas:
        novas_palavras += gerador_palavras(palavra)
    return novas_palavras

def corretor_super_sayajin_v1(palavra_errada):
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

def insere_letras(fatias):
    letras = 'abcedfghijklmnopqrstuvwxyzáâàãéêèíîìóôòõúûùç'
    return [esquerdo + letra + direito for esquerdo, direito in fatias for letra in letras]

def deletando_caracter(fatias):
    return [esquerdo + direito[1:] for esquerdo, direito in fatias]

def troca_caracter(fatias):
    letras = 'abcedfghijklmnopqrstuvwxyzáâàãéêèíîìóôòõúûùç'
    return [esquerdo + letra + direito[1:] for esquerdo, direito in fatias for letra in letras]

def invertendo_caracter(fatias):
    return [esquerdo + direito[1] + direito[0] + direito[2:] for esquerdo, direito in fatias if len(direito) > 1]

def gerador_palavras(palavra):
    fatias = [(palavra[:i], palavra[i:]) for i in range(len(palavra) + 1)]
    palavras_geradas = insere_letras(fatias)
    palavras_geradas += deletando_caracter(fatias)
    palavras_geradas += troca_caracter(fatias)
    palavras_geradas += invertendo_caracter(fatias)
    return palavras_geradas

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









