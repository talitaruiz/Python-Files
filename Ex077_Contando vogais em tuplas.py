palavras = ('Amor', 'Caridade', 'Alegria', 'Fraternidade',
         'Honestidade', 'Paz', 'Solidariedade', 'Tranquilidade',
         'Positividade', 'Empatia', 'Serenidade', 'Altruismo')
for pos in palavras:
    print(f'\n Na palavra {pos.upper()} temos:', end = '')
    for letra in pos:
        if letra.lower() in 'aeiou':
            print(f' {letra.upper()}', end = '')
