import json


aaa = ""
with open("dumps/avaliacao.json") as f:
    aaa = f.read()
aaa = json.loads(aaa)

targetMatches = [i["targetMatches"] for i in aaa]
targetCorretor = [i["targetCorretor"] for i in aaa]
a = []

for i in range(len(targetMatches)):
    a.append((targetMatches[i], targetCorretor[i]))

zero = [(i, j) for i, j in a if i == j == 0]
um = [(i, j) for i, j in a if i == j == 1]
others = [(i, j) for i, j in a if i != j]
um_esquerda = [(i, j) for i, j in others if j == 1]
um_direita = [(i, j) for i, j in others if i == 1]

# print(len(zero), len(um), len(others), len(um_esquerda), len(um_direita))
# print((zero), (um), (others), (um_esquerda), (um_direita))

# print(sum(targetMatches)*100/len(targetMatches), sum(targetCorretor)*100/len(targetCorretor))
# print(sum(targetMatches), sum(targetCorretor), len(targetMatches))


zeros_err = []

for i in aaa:
    if i["targetMatches"] == 0 and i["targetCorretor"] == 0:
        print(i['Correta'], i['Errada'], i['Corretor'])
        zeros_err.append(i)
with open("zeros.json", "a") as f:
    f.write(json.dumps(zeros_err))
