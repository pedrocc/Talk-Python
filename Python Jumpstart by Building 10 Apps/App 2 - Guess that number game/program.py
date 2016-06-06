import random

# Entrada do app
print('------------------------------------')
print('       GUESS THAT NUMBER GAME')
print('------------------------------------', '\n')

# Criação do número randomico
the_number = random.randint(1,100)

guess = 101

while guess != the_number:
    number_user = input('Guess a number between 0 and 100: ')
    guess = int(number_user)

    if the_number == guess:
        break
    elif the_number < guess:
        print('Muito alto, tente novamente.')
    elif the_number > guess:
        print('Muito baixo, tente novamente')


print('Parabéns, você acertou o número é:', guess)
print('Fim')
