import csv
import time

def mainFunction(ds):

    conjunto = []

    valor =0

    cont = 0

    linha1 = "False"
    linha2 = 0
    linha3 = 0
    

    arquivo = open(ds + '.csv', 'r')

    linhas = csv.reader(arquivo)

    for linha in linhas:
        conjunto.append(linha)


    valor = conjunto[0]

    print(valor)

    conjunto.pop(0)
    conjunto.pop(0)

    print(conjunto)

    for element in conjunto:

        if(element == valor):
            linha1 = "True"
            linha2 = cont
            linha3 = time.time()
            print(linha1)
            print(linha2)
            print(linha3)

        if(linha1 == "False"):
            linha2 = -1
            
        cont = cont + 1
        
    arquivo.close()

    
    arquivoNovo = open('resposta-' + ds + '.txt', 'w')

    arquivoNovo.write(str(linha1) + "\n")
    arquivoNovo.write(str(linha2) + "\n")
    arquivoNovo.write(str(linha3) + "\n")

    arquivoNovo.close()

dsA = 'dataset-1-a'
dsB = 'dataset-1-b'
dsC = 'dataset-1-c'

mainFunction(dsA)
mainFunction(dsB)
mainFunction(dsC)


