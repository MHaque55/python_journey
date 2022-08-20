import random

#Guess a random number from range 1 to 100

# def show_score():
#     print('Your current score: ', score)

def game():
    answer = random.choice(range(1,101))
    score = 20
    number = input('Choose a number: ')
    while (int(number) != answer) & (score > 0):
        if int(number) > answer:
            print('You are ahead')
            score = score - 1
            print('Attempt left:', score, '\n')

        elif int(number) < answer:
            print('Now you are behind')
            score = score - 1
            print('Attempt left:', score, '\n')

        number = input('Choose another number: ')
    
    if score == 0:
        print('Ran out of attempt')
    else:
        print('Conrgatulations')
        print('Correct number:', answer)
        print('Your answer: ' + number)
        print('Your score:', score)


game()

replay = input('Want to play again? (Y for yes) ')

while replay == 'Y':
    game()
    replay = input('Want to play again? (Y for yes) ')

print('Thanks for playing')



