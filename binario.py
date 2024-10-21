def decimal_para_binario(numero):
    return bin(numero).replace("0b", "").zfill(5)

def binario_para_decimal(binario):
    decimal = 0
    for digito in binario:
        decimal = decimal * 2 + int(digito)
    return decimal

def checar_binario(binario):
    return all(digito in '01' for digito in binario)

while True:
    opcao = input("Escolha a conversão (1 para decimal para binário, 2 para binário para decimal): ")
    if opcao in ["1", "2"]:
        break
    else:
        print("Opção inválida. Por favor, escolha 1 ou 2.")

if opcao == "1":
    numero_decimal = int(input("Digite um número decimal: "))
    numero_binario = decimal_para_binario(numero_decimal)
    print(f"O número {numero_decimal} em binário é: {numero_binario}")

elif opcao == "2":
    while True:
        binario = input("Digite um número binário: ")
        if checar_binario(binario):
            break
        else:
            print("Número binário inválido. Tente novamente.")
    decimal = binario_para_decimal(binario)
    print(f"O número binário {binario} em decimal é: {decimal}")
