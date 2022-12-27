
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