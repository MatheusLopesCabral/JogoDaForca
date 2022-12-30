from Funções.EscolhePalavra import *
from Funções.ocultaPalavra import *
from Funções.PrintTela import *

# Obtendo novos dados para o inicio do jogo.
vidas = 6
dica, secreta = palavraSecreta()
ocultar(secreta)
inicio()


while True:
    segredo = oculto
    tela(dica, segredo, vidas)

    if vidas <= 0: #Condição para perder o jogo
         derrota()
         break
    if '-' not in segredo: #Condição para ganhar o jogo
        vitoria()
        break
    #Tratamento de erro para caso o valor informado não seja string, ou tenha mais de um componente.
    try:
        letra = str(input('\n\033[34mTente uma letra: \033[m'))
        if letra.isnumeric():
             print('\033[33mValor digitado está incorreto... Use apenas letras!\033[m')
             continue
    #Ação para caso o jogo seja interrompido pelo usuário
    except KeyboardInterrupt:
            print('💀💀💀')
            print('\n\n\033[1:30:41mVocê escolheu sair do jogo... Espero que possamos jogar de novo!\033[m')
            break
    #Tratamento para caso o valor recebido não seja um tipo primitivo.
    except:
        print('Houve um ERRO com o valor informado. Tente outro por favor.')
    else:
        #Autenticando a Letra jogada
        erro = autenticar(secreta, letra)
        if erro == True:
             vidas -= 1











