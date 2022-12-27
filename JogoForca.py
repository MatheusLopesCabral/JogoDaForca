from Funções.EscolhePalavra import *
from Funções.ocultaPalavra import *
from Funções.PrintTela import *

dica, secreta = palavraSecreta()
ocultar(secreta)
vida = 6

while True:
    segredo = oculto
    if vida <= 0:
        print('\033[31mOh, não! Suas vidas acabaram... Boa sorte na próxima!\033[m')
        break
    if '-' not in segredo:
        print('\033[36mParábens! Todas as letras foram acertas!\033[m')
        break

    tela(dica, segredo, vida)
    letra = str(input('\n\033[34mTente uma letra: \033[m'))
    if letra.isnumeric():
         print('\033[33mValor digitado está incorreto... Use apenas letras!\033[m')
         continue
    if autenticar(secreta, letra, vida)








