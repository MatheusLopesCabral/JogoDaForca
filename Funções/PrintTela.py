def inicio():
    print(f'-'*40)
    print('{:^40}'.format('BEM VINDO AO JOGO DA FORCA'))



def tela(dica, segredo, vida):
    print('-'*40)
    print(f'DICA: {dica:<20}', end='')
    if vida >= 5:
        print(f'\033[32mVidas: {vida}\033[m')
    elif vida >= 3:
        print(f'\033[33mVidas: {vida}\033[m')
    else:
        print(f'\033[31mVidas: {vida}\033[m')
    print('\n{:^40}'.format(' '.join(segredo)))


def vitoria():
    print('')
    print(f'⭐' * 25)
    print('{:<15}{:^25}{:>28}'.format('⭐', '\033[35mVOCê GANHOU!\033[m', '⭐'))
    print(f'⭐' * 25)

def derrota():
    print('')
    print(f'😩' * 25)
    print('{:<15}{:^25}{:>22}'.format('😩', '\033[32mVOCê PERDEU!\033[m', '😩'))
    print(f'😩' * 25)

