import random
score_user = 0
score_comp = 0
print('Welcome to Rock, Paper, and Scissors game')

def user():
    user = input('Choose \'Rock\', \'Paper\', or \'Scissors\': ')
    return user

def comp():
    options = ['Rock', 'Paper', 'Scissors']
    computer = random.choice(options)
    return computer

def is_valid(user):
    if (user != 'Rock') & (user != 'Scissors') & (user != 'Paper'):
        print('Not valid choice, try again')
        return 1
    return 0

def series():
    user = input('How many series do you want to play? ')
    return int(user)

def game():
    global score_comp
    global score_user
    user_input = user()
    while is_valid(user_input) != 0:
        user_input = user()
    comp_input = comp()
    print('Computer chose ' + comp_input) 
    if (user_input == 'Scissors') & (comp_input == 'Rock'):
        print('Rock smash Scissors')
        print('Computer won this round')
        score_comp += 1 
    elif (user_input == 'Rock') & (comp_input == 'Paper'):
        print('Paper beats Rock')
        print('Computer won this round')
        score_comp += 1
    elif (user_input == 'Paper') & (comp_input == 'Scissors'):
        print('Scissors cut Paper')
        print('Computer won this round')
        score_comp += 1
    
    elif (comp_input == 'Scissors') & (user_input == 'Rock'):
        print('Rock smash Scissors')
        print('You won this round')
        score_user += 1
    elif (comp_input == 'Rock') & (user_input == 'Paper'):
        print('Paper beats Rock')
        print('You won this round')
        score_user += 1
    elif (comp_input == 'Paper') & (user_input == 'Scissors'):
        print('Scissors cut Paper')
        print('You won this round')
        score_user += 1
    
    else:
        print('You chose ' + user_input + ' Computer chose ' + comp_input)
        print('It\'s a draw this round')


def result(score_u, score_c):
    print('Your score:', score_u, '\nComputer\'s score:', score_c)
    if score_u > score_c:
        print('Congratulations, you won this series')
    elif score_u < score_c:
        print('Better luck next time')
    else:
        print('It\'s a draw SMH')


series_input = series()
for _ in range(series_input):
    game()

result(score_user, score_comp)
