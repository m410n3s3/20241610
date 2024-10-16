def Insercao_dados():
    vC = [1 , 3.4 , 'A' , " IFSC " ]
    print("Vetor Original: ", vC)
    input("Digite enter para prossegir: ")
    vC.insert(0,56) #Adiciona na posição 0 o inteiro 56.
    vC.insert(3,'B')
    vC.append(11)
    for i in vC :
        print ( i )










if __name__=="__main__":
    Insercao_dados()