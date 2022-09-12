
#CASO O ARQUIVO arquivoZen.txt NÃO ESTEJA CRIADO
arquivoZen = open('Zen.txt','w')
arquivoZen = open('Zen.txt','r')
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

arquivoZen = open('Zen.txt','w')
arquivoZen.writelines(conteudo)


from googletrans import Translator
google = Translator()

escolha = 0
while True:
    escolha = int(input("Digite um 1 para Portugues ou 2 para Espanhol: "))
    if 1 < escolha > 2:
        print('Valor incorreto!')
    else:
        break
arquivoTraduzido = open('arquivoTraduzido.txt','w')
arquivoZen = open('zen.txt','r')

if escolha == 1:
    while True:

        try:
            conteudo = arquivoZen.readline()
            conteudo1 = (google.translate(conteudo, dest='pt').text)
            arquivoTraduzido = open('arquivoTraduzido.txt', 'a')
            arquivoTraduzido.writelines(conteudo1+'\n')
        except EOFError:
            break
elif escolha == 2:
    while True:

        try:
            conteudo = arquivoZen.readline()
            conteudo1 = (google.translate(conteudo, dest='es').text)
            arquivoTraduzido = open('arquivoTraduzido.txt', 'a')
            arquivoTraduzido.writelines(conteudo1+'\n')
        except EOFError:
            break

arquivoTraduzido.close()
arquivoZen.close()