import random

palavras = {'Fruta': ['abacaxi', 'acerola', 'goiaba', 'melancia'], 'Lugar': ['recife', 'cuiaba', 'bahia', 'amazonas'], 'Cor': ['amarelo', 'vermelho', 'cinza', 'preto'], 'Profissão': ['medico', 'bombeiro', 'administrador', 'pedreiro']}


def palavraSecreta(dica='', secreta=''):
        """Função para escolher aleatoriamente uma das palavras secretas,
         retornando a Categoria e a Palavra"""
        dica = random.choice(list(palavras.keys()))
        secreta = random.choice(palavras[dica])
        return dica, secreta
