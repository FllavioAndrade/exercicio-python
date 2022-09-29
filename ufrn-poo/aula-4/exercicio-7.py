'''
Escreva um programa que traduza um arquivo txt com o Zen of Python em 10
línguas diferentes e armazene as traduções em 10 arquivos distintos. Os arquivos
devem ser criados via python.
'''

#CASO O ARQUIVO arquivoZen.txt NÃO ESTEJA CRIADO
arquivoZen = open('zen.txt','w')
arquivoZen = open('zen.txt','r')
conteudo = arquivoZen.readlines()
conteudo.append('Beautiful is better than ugly.\n'
                 'Explicit is better than implicit.\n'
                 'Simple is better than complex.\n'
                 'Complex is better than complicated.\n'
                 'Flat is better than nested.\n'
                 'Sparse is better than dense.\n'
                 'Readability counts.\n'
                 "Special cases aren't special enough to break the rules.\n"
                 'Although practicality beats purity.\n'
                 'Errors should never pass silently.\n'
                 'Unless explicitly silenced.\n'
                 'In the face of ambiguity, refuse the temptation to guess.\n'
                 'There should be one-- and preferably only one --obvious way to do it.\n'
                 "Although that way may not be obvious at first unless you're Dutch.\n"
                 'Now is better than never.\n'
                 'Although never is often better than *right* now.\n'
                 "If the implementation is hard to explain, it's a bad idea\n."
                 "If the implementation is easy to explain, it may be a good idea.\n"
                 "Namespaces are one honking great idea -- let's do more of those!")

arquivoZen = open('zen.txt','w')
arquivoZen.writelines(conteudo)

from random import sample
from googletrans import Translator
google = Translator()

LANGUAGES = [
    'af',
    'sq',
    'ar ',
    'ca',
    'zh-cn',
    'zh-tw',
    'en',
    'fr',
    'mr',
    'my',
    'de',
    'it',
    'ja',
    'ko',
    'kk',
    'la',
    'sr',
    'sn',
    'su',
    'ku',
    'ne',
    'no',
    'or',
    'sm',
    'pt',
    'ru',
    'cy',
    'so',
    'tg',
    'es',]

aleatorio = sample(range(29), 10)

for i in range(10):
    idioma = LANGUAGES[aleatorio[i]]

    zenpt = open(f'zen-{idioma}.txt','w')
    print(f'Traduzindo para o idioma {idioma}')
    arquivoZen = open('zen.txt','r')
    conteudo1 = 'a'
    while True:
        try:
            conteudo = arquivoZen.readline()
            conteudo1 = (google.translate(conteudo, dest=idioma).text)
            arquivoZenpt = open(f'zen-{idioma}.txt', 'a')
            arquivoZenpt.writelines(conteudo1+'\n')
            arquivoZenpt.close()
        except EOFError:

            continue
arquivoZen.close()
