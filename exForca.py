import random

nomes = ['abacaxi', 'acerola', 'goiaba', 'melancia', 'recife', 'cuiaba', 'bahia', 'amazonas']
categoria = ['Fruta', 'Fruta', 'Fruta', 'Fruta', 'Lugar', 'Lugar', 'Lugar', 'Lugar']
nome = random.choice(nomes)
chave = list(nome)
qtd = len(chave)
cate = ''
recebidos = []
chute = ''
fruta = []
vida = 6
for p in range (0, qtd):
    fruta.append('- ')
for cat in range (0, len(nomes)):
    if nome == nomes[cat]:
        cate = categoria[cat]
while fruta != chave and vida != 0:
    print(('{:🌟' '^50}\n{:-^15}\n{}        Vida: {}'.format('', cate, fruta, vida)))
    chute = str(input('Digite uma letra: ')).strip().lower()
    if len(chute) == 1:
        if chute in recebidos:
            print('Essa letra já foi usada. Tente outra!')
        elif chute in chave:
             for c in range(0, qtd):
                if chave[c] == chute:
                   fruta[c] = chute
                   recebidos.append(chute)
        else:
                vida -= 1
                print('Você errou...')
                recebidos.append(chute)
    else:
          print('Valor informado não é válido. A rodada não foi contabilizada.')
    if ''.join(fruta) == ''.join(chave):
        print('{}\nVocê ganhou!'.format(fruta))
    elif vida <= 0:
        print('{}\nVocê perdeu...'.format(fruta))
