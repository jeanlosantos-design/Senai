
valor_total = float(input("Digite o valor total da conta: "))

valor_por_pessoa = valor_total / 3

carlos = int(valor_por_pessoa)
andre = int(valor_por_pessoa)
felipe = valor_total - (carlos + andre)

print("Carlos deve pagar R$ {:.2f}".format(carlos))
print("André deve pagar R$ {:.2f}".format(andre))
print("Felipe deve pagar R$ {:.2f}".format(felipe))