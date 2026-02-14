import random
from collections import Counter

dados = {
    2023:[21,24,33,41,48,56],
    2022:[4,5,10,34,58,59],
    2021:[12,15,23,32,33,46],
    2020:[17,20,22,35,41,42],
    2019:[3,35,38,40,57,58],
    2018:[5,10,12,18,25,33],
    2017:[3,6,10,17,34,37],
    2016:[5,11,22,24,51,53],
    2015:[2,18,31,42,51,56],
    2014:[1,5,11,16,20,56],
    2013:[20,30,36,38,47,53],
    2012:[14,32,33,36,41,52],
    2011:[3,4,29,36,45,55],
    2010:[2,10,34,37,43,50],
    2009:[10,27,40,46,49,58]
}

# Frequência
freq = Counter()
for nums in dados.values():
    freq.update(nums)

# Último ano em que apareceu
anos_desc = sorted(dados.keys(), reverse=True)
last_seen = {}
for ano in anos_desc:
    for n in dados[ano]:
        last_seen.setdefault(n, ano)

ANO_ATUAL = 2025
DEFAULT_LAST = 2008  # pra quem nunca apareceu nesse recorte

def peso(n, alpha=1.0, beta=0.12):
    f = freq.get(n, 0)
    rec = ANO_ATUAL - last_seen.get(n, DEFAULT_LAST)
    return 1.0 + alpha*f + beta*rec

weights = [peso(n) for n in range(1, 61)]

def gera_jogo():
    while True:
        nums = set()
        while len(nums) < 6:
            nums.add(random.choices(range(1, 61), weights=weights, k=1)[0])

        nums = sorted(nums)

        # 3 ímpares e 3 pares
        if sum(n % 2 for n in nums) != 3:
            continue

        # Pelo menos 4 faixas de dezenas diferentes
        dezenas = len(set((n-1)//10 for n in nums))
        if dezenas < 4:
            continue

        return nums

random.seed(42)
for i in range(5):
    print(gera_jogo())
