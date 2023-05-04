import random

NUM_DIGIST=1
MAX_GUESSES=10

while True:
        secretNum=getSecretNum()
        print('Я задумал число.')
        print('У тебя есть {} попыток чтобы отгадать его'.format(MAX_GUESSES))

        numGuesses=1
while numGuesses<=MAX_GUESSES:
     guess=''
     while len(guess) != NUM_DIGIST or not guess.isdecimal():
                print('Попытка №{}: '.format(numGuesses))
                guess=input('> ')
                clues = getClues(guess, secretNum)
print(clues)
numGuesses+=1

if guess==secretNum:
    break
    if numGuesses>MAX_GUESSES:
                print('У тебя закончились попытки')
                print('Ответом было {}.'.format(secretNum))

        print('Вы хотите сыграть ещё раз?(да или нет)')
        if not input('> ').lower().startswith('y'):
            break
        print('Спасибо за игру!')

def getSecretNum():
    numbers=[0,1,2,3,4,5,6,7,8,9]
    random.shuffle(numbers)
    secretNum=''
    for i in range(NUM_DIGIST):
        secretNum+=str(numbers[i])
        return secretNum

def getClues(guess, secretNum):
    if guess==secretNum:
        return 'Ты угадал'

    clues=[]

    for i in range(len(guess)):
        if guess[i]==secretNum[i]:
            clues.append('Ферми')
        elif guess[i] in secretNum:
            clues.append('Пико')
    if len(clues)==0:
        return 'Бейглз'
    else:
        clues.sort()
        return ' '.join(clues)


if __name__=='__main__':
    main()