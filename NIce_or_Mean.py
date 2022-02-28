# Python 3.10.2
# Author: Alan F. Mitchell
#
#Purpose: This game was intended to reiterate all Python skills learned
#

# this defines a function
def start(nice=0,mean=0,name=''):
    # get users name
    name=describe_game(name)
    nice,mean,name=nice_mean(nice,mean,name)

def describe_game(name):
    """
        check if this is a new game or not
        If it is new, get the users name
        if it is not a new game, thank the player for
        playing again and contiue with the game

    """
    
#meaning, if we do not already have this user's name,
# then they are a new player and we need to get their name
    if name != "":
        print('\nThank-you for playing again {}'.format(name))
    else:
        stop= True
        if name == "":
            name= input('\nWhat is your name?\n>>>').capitalize()
            if name !="":
                print('n\Welcome {}'.format(name))
                print('\nIn this game, you will be greeted \nby several people. n\You can choose to be nice or mean')
                print('but at the end of the game your fate n\will be sealed by your action')
                stop=False
    return name

def nice_mean(nice,mean,name):
    stop=True
    while stop:
        show_score(nice,mean,name)
        pick= input('\n A stranger approaches you for a conversation \nWill you be nice \nor mean (N/M)\n>>>').lower()
        if pick=='n':
            print('\n The stranger walks away smiling...')
            nice =(nice + 1)
            stop = False
        if pick == 'm':
            print('n\The stranger glares at you \nmenaceingly and storms off...')
            mean=(mean + 1)
            stop=False
    score(nice,mean,name) #pass the 3 variables to the score()
def show_score(nice,mean,name):
    print('\n{} your current total:\n({}, Nice) and ({},Mean)'.format(name,nice,mean))
    
def score(nice,mean,name):
    # score function is being passed the values stored within the 3 variables
    if nice > 2: # if condition is valid, call win function passing in the variables so it can use them.
        win(nice,mean,name)
    if mean > 2: # if condition is valid, call lose function passing in the variables so it can use them.
        lose(nice,mean,name)
    else: # else, call the nice_mean fucntion passing in the variables so it can be used.
        nice_mean(nice,mean,name)

def win(nice,mean,name):
    # Substitute the {} wildcards with our variable values
    print('Nice job {},you win! Everyone loves you and made lots of friends along the way'.format(name))
    # call again function and pass in our variables
    again(nice,mean,name)
    
def lose(nice,mean,name):
    #Substitute the {} wilcards with our variable values
    print('\nAhhh too bad, Game Over \n{}, you live in a van alone \nby the river meanie'.format(name))
    #call again function and pass in our variable values
    again(nice,mean,name)
    
    
def again(nice,mean,name):
    stop=True
    while stop:
        choice= input('\nDo you want to play again? (y/n):\n>>>').lower()
        if choice == 'y':
            stop = False
            reset(nice,mean,name)
        if choice == 'n':
            print('\nOh, so sad sorry to see you go!')
            stop=False
            quit()
        else:
            print('\nEnter (Y) for Yes , (N) for No:\n>>>')

def reset(nice,mean,name):
    nice = 0
    mean = 0
    #Notice, name variable not reset, because the playes has opted to play again.
    start(nice,mean,name)
    
    
    
            
        
    
    
                

















#this tells our interpreter where to start. 
if __name__ == '__main__':
   start()
