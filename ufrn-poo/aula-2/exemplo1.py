
#Crie o arquivo helloworld.txt na pasta de projetos do
#python. Escreva Hello World na primeira linha e salve o arquivo.
#Abra o arquivo via python e coloque o valor da primeira linha numa variável. Por fim, imprima o
#conteúdo da variável.

#DESCOMENTE CASO O ARQUIVO NÃO ESTEJA CRIADO

#Criar o arquivo helloworld.txt - se exeistir, sobrepõe.
arquivoHello = open('helloworld.txt', "w")

#Escreva Hello World na primeira linha e salve o arquivo.
arquivoHello = open('helloworld.txt', 'r')
conteudo = arquivoHello.readlines()
conteudo.append('Hello World')
arquivoHello = open('helloworld.txt','w')
arquivoHello.writelines(conteudo)
arquivoHello.close()



arquivoHello = open('helloworld.txt', 'r')
lerArquivo = arquivoHello.readlines()
print(lerArquivo,'\n')
