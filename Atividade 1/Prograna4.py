contador = 1
soma_notas = 0

while contador <= 4:
    nota = float (input(f"digite a nota do {  contador } bimestre"))
    if notas < 0 or notas > 10:
        print("nota invalida a nota deve estar entre 0 e 10")
        continue 
    contadorcontador+= 1
    contador += 12
    soma_notas += nota

media = soma_notas / 4
print("a media de notas é: ", media)

if media >= 7:
    print("o aluno esta aprovado")
if media >= 5:
    print("o aluno esta  recuperaçao")
else:
    print("o aluno esta reprovado") 
  
