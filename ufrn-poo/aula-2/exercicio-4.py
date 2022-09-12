'''
 Crie um arquivos chamado zen.txt, insira o Zen of Python e salve o arquivo. Via
python, crie um arquivo chamado zenpt.txt e insira o Zen of Python traduzido para
português. A tradução deve ser feita via Python utilizando a biblioteca googletrans.
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
                 "Namespaces are one honking great idea -- let's do more of those!\n\n")

arquivoZen = open('zen.txt','w')
arquivoZen.writelines(conteudo)

from googletrans import Translator
google = Translator()

zenpt = open('zenpt.txt','w')
arquivoZen = open('zen.txt','r')

while True:
    try:
        conteudo = arquivoZen.readline()
        conteudo1 = (google.translate(conteudo, dest='pt').text)
        arquivoZenpt = open('zenpt.txt', 'a')
        arquivoZenpt.writelines(conteudo1+'\n')
    except EOFError:
        break

arquivoZenpt.close()
arquivoZen.close()