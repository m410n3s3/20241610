def forma1_leitura():

    vet = input().split()
    tamanho_vet = len(vet)
    for i in range (tamanho_vet):
        vet[i] = int(vet[i])
    print(vet)

def forma2_leitura():

    vet = list(map(int,input().split()))
    # print(vet)

    tamanho_vet = len(vet)
    for i in range (tamanho_vet):
        #vet[i] = 3*vet[i]
        vet[i]*=3
        print(vet[i], end = " ")
    print()


#forma otimizada
import array as ar
def forma3_leitura_array():
    vet = ar.array('i',map(int,input().split()))
    tamanho_vet = len(vet)
    for i in range (tamanho_vet):
         #vet[i] = 3*vet[i]
        vet[i]*=3
        print(vet[i], end = " ")
    print()

import FuncoesEntrada as FE



if __name__=="__main__":
    forma3_leitura_array()