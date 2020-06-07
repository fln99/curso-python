print('Calcule a média de 2 notas abaixo:')

nota_1 = float(input('Primeira nota: '))
nota_2 = float(input('Segunda nota: '))

media = (nota_1 + nota_2) / 2

if media < 5:
    print('Que triste! Sua média não atingiu o mínimo de 5 pontos.')
    print('Situação: reprovado!')
elif media >= 5 and media < 7:
    print('Você pode melhorar! Sua média foi de {} pontos!'.format(media))
    print('Situação: recuperação!')
else:
    print('Muito bom! Você atingiu uma média de {} pontos!'.format(media))
    print('Situação: aprovado!')