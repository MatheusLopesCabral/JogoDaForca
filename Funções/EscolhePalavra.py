import random

palavras = {'Fruta': ['abacaxi', 'acerola', 'goiaba', 'melancia'], 'Lugar': ['recife', 'cuiaba', 'bahia', 'amazonas'], 'Cor': ['amarelo', 'vermelho', 'cinza', 'preto'], 'Profissão': ['medico', 'bombeiro', 'administrador', 'pedreiro']}


def palavraSecreta(dica='', secreta=''):
        dica = random.choice(list(palavras.keys()))
        secreta = random.choice(palavras[dica])
        return dica, secreta
