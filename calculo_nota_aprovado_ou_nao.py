nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
media = (nota1 + nota2) / 2

if media < 5.0:
    print (f'Sua média foi {media}: REPROVADO')
elif media > 5.0 and media < 6.9:
    print (f'Sua média foi {media}: RECUPERAÇÃO')
else:
    print (f'Sua média foi {media}: APROVADO!!!')