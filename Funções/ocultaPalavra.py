tentativas = []
oculto = []


def ocultar(secreta):
    """""""
    global oculto
    for c in range(len(secreta)):
        oculto.append('-')
    return oculto


def autenticar(secreta, letra):
    a = list(secreta)

    if len(letra) != 1:
        print('\033[33mDigite uma letra por vez!.!\033[m')
    elif letra in tentativas:
        print('\033[33mVocê já tentou essa letra. Coloque uma nova!\033[m')

    elif letra not in secreta:
        tentativas.append(letra)
        print('\033[31mLetra errada! Mais sorte na proxíma tentativa.\033[m')
        return True

    else:
        for c in range(0, len(secreta)):
            if a[c] == letra:
                oculto[c] = letra
        tentativas.append(letra)
        return False









