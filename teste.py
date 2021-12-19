import nltk
import json
from unicodedata import normalize

nltk.download('punkt')

class CorretorNLP:
    def __init__(self, text='') -> None:
        self.text_tokenize = nltk.tokenize.word_tokenize(text)
        self.listar_palavras_text = [i.lower() for i in self.text_tokenize if i.isalpha()]

        self.dados_treinamento = self.lerArquivo('br-sem-acentos.txt')+self.lerArquivo('br-utf8.txt')
        self.tokenize_dataset = nltk.tokenize.word_tokenize(self.dados_treinamento)
        self.listar_palavras_dataset = list(set([i.lower().strip() for i in self.tokenize_dataset if i.isalpha()]))
        self.frequencia_text = nltk.FreqDist(self.listar_palavras_dataset)
        self.vocabulario = set(self.listar_palavras_dataset)
        self.palavras_geradas = self.gerador_inception(self.gerador_palavras(text))
    
    def teste_file(self, file):
        return [(k.lower(), v.lower()) for k, v in [tuple(i.split()) for i in open(file, mode='r', encoding="utf-8")]]
        
    def teste(self, file):
        self.dataset_test = self.teste_file(file)
        with open("dumps/avaliacao.json", "w", encoding="utf-8") as f:
            f.write(json.dumps([self.avaliador([i]) for i in self.dataset_test]))

    def norm_text(self, text):
        return normalize(
            'NFKD', text.lower().strip()).encode(
                'utf8','ignore').decode('utf8')
            
    def verifica_similaridade(self, errado, predito):
        teste = [(predito, errado)]
        print(self.avaliador(teste))

    def lerArquivo(self, arquivo):
        with open(arquivo, mode='r', encoding="utf-8") as f:
            file = f.read()
        return file

    def probabilidade(self, palavra_gerada):
        return self.frequencia_text[palavra_gerada] / len(self.listar_palavras_dataset)

    def corretor(self, palavra_errada):
        return max(self.gerador_palavras(palavra_errada), key=self.probabilidade), self.gerador_palavras(palavra_errada)

    def insere_letras(self, fatias):
        letras = 'abcedfghijklmnopqrstuvwxyzáâàãéêèíîìóôòõúûùç'
        return [esquerdo+letra+direito for esquerdo, direito in fatias for letra in letras]

    def deletando_caracter(self, fatias):
        return [esquerdo+direito[1:] for esquerdo, direito in fatias]

    def troca_caracter(self, fatias):
        letras = 'abcedfghijklmnopqrstuvwxyzáâàãéêèíîìóôòõúûùç'
        return [esquerdo+letra+direito[1:] for esquerdo, direito in fatias for letra in letras]

    def invertendo_caracter(self, fatias):
        return [esquerdo+direito[1]+direito[0]+direito[2:] for esquerdo, direito in fatias if len(direito) > 1]

    def gerador_inception(self, palavras_geradas):
        novas_palavras = []
        for palavra in palavras_geradas:
            novas_palavras += self.gerador_palavras(palavra)
        return novas_palavras

    def gerador_palavras(self, palavra):
        fatias = [(palavra[:i], palavra[i:]) for i in range(len(palavra) + 1)]
        palavras_geradas = self.insere_letras(fatias)
        palavras_geradas += self.deletando_caracter(fatias)
        palavras_geradas += self.troca_caracter(fatias)
        palavras_geradas += self.invertendo_caracter(fatias)
        return palavras_geradas

    def corretor_super_sayajin(self, palavra_errada):
        palavras_geradas = self.gerador_palavras(palavra_errada)
        palavras_inception = self.gerador_inception(palavras_geradas)
        todas_palavras = set(palavras_geradas + palavras_inception)
        candidatos = []
        for palavra in todas_palavras:
            if palavra in self.vocabulario:
                candidatos.append(palavra)
        if not candidatos:
            result, candidatos = self.corretor(palavra_errada)
            return self.corretor(palavra_errada)
        return max(candidatos, key=self.probabilidade), candidatos

    def avaliador(self, testes):
        numero_palavras = len(testes)
        acertou = desconhecidas = 0
        acertou = 0
        matches = []
        candidatos_list = []
        for correta, errada in testes:
            try:
                palavra_corrigida, candidatos  = self.corretor_super_sayajin(errada)
            except:
                palavra_corrigida, candidatos = self.corretor(errada)
            
            desconhecidas += (correta not in self.vocabulario)
            if palavra_corrigida == correta:
                matches.append(palavra_corrigida)
                acertou += 1
            else:
                candidatos_list.append(candidatos)
        taxa_acerto = round(acertou * 100 / numero_palavras, 2)
        taxa_desconhecidas = round(desconhecidas * 100 / numero_palavras, 2)
        data = {
            "Correta": [i for i, _ in testes],
            "Errada": [j for _, j in testes],
            "Matches": matches,
            "Corretor": [self.corretor(j)[0] for _, j in testes],
            "Candidatos": [i for i in list(set(sum(candidatos_list, []))) if i in self.vocabulario],
            "TaxaDeAcerto": taxa_acerto,
            "TaxaDesconhecidas": taxa_desconhecidas,
        }

        data.update({
            "targetMatches": int(data["Correta"][0] == data["Matches"][0]) if data["Matches"] else 0,
            "targetCorretor": int(data["Correta"][0] == data["Corretor"][0]) if data["Corretor"][0] else 0
        })

        return data

def train():
    with open("dumps/avaliacao.json", 'r', encoding="utf-8") as f:
        aaa = json.loads(f.read()) 
    targetMatches = [i["targetMatches"] for i in aaa]
    targetCorretor = [i["targetCorretor"] for i in aaa]
    a = [(targetMatches[i], targetCorretor[i]) for i in range(len(targetMatches))]
    zero = [(i, j) for i, j in a if i == j == 0]
    um = [(i, j) for i, j in a if i == j == 1]
    others = [(i, j) for i, j in a if i != j]
    um_esquerda = [(i, j) for i, j in others if j == 1]
    um_direita = [(i, j) for i, j in others if i == 1]
    zeros_err = [i for i in aaa if i["targetMatches"] == 0 and i["targetCorretor"] == 0]

    print(sum(targetMatches)*100/len(targetMatches), sum(targetCorretor)*100/len(targetCorretor))
    print(sum(targetMatches), sum(targetCorretor), len(targetMatches))
    
    with open("dumps/0_0.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(zeros_err))
    with open("dumps/treinamento_erros.txt", "w", encoding="utf-8") as f:
        for i in zeros_err:
            f.write(f"{i['Correta'][0]} {i['Errada'][0]}\n")

a = CorretorNLP()
a.teste("palavras.txt")
train()
for i in range(5):
    a.teste("dumps/treinamento_erros.txt")
    train()