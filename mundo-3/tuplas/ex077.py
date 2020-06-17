words = ('agua', 'abacate', 'abacate', 'escola', 'caderno', 'garota', 'elefante', 'jovem', 'ornitorrinco')

for word in words:
    print(f'\nA palavra {word.upper()} tem as seguintes vogais:', end=' ')

    for letter in word:
        if letter in 'aeiou':
            print(letter, end=' ')