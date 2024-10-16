def decimal_para_binario(numero):
    return bin(numero).replace("0b", "").zfill(5)

numero_decimal = int(input("Digite um número decimal: "))
numero_binário = decimal_para_binario(numero_decimal)
print(f"O número {numero_decimal} em binário é {numero_binário}")