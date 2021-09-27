### Este script tem como objetivo:
# - Ler 2 notas
# - Calcular a média
# - E mostrar o resultado na tela em relação a aprovação ou não do aluno.
# - Se nota menor que 5 = REPROVADO
# - Se nota maior que 5 e menor que 6.9 = RECUPERAÇÃO 
# - Se nota maior que 7 = APROVADO
#
#
#
#
### Autor thieslei@gmail.com

nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
media = (nota1 + nota2) / 2

if media < 5.0:
    print (f'Sua média foi {media}: REPROVADO')
elif media > 5.0 and media < 6.9:
    print (f'Sua média foi {media}: RECUPERAÇÃO')
else:
    print (f'Sua média foi {media}: APROVADO!!!')