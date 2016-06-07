import random

# Entrada do app
print('------------------------------------')
print('       GUESS THAT NUMBER GAME')
print('------------------------------------', '\n')

# Criação do número randomico
the_number = random.randint(1,100)

name = input('Por favor digite o seu nome: ')
guess = 101

while guess != the_number:
    number_user = input('Guess a number between 0 and 100: ')
    guess = int(number_user)

    if the_number == guess:
        break
    elif the_number < guess:
        print('Desculpe {0}, {1} é um valor muito alto, tente novamente.'.format(name, guess))
    elif the_number > guess:
        print('Desculpe {0}, {1} é um valor muito baixo, tente novamente'.format(name, guess))


print('Parabéns, você acertou o número é:', guess)
print('Fim')
