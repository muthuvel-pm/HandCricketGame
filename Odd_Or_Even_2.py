#ODD OR EVEN 2.0 (hand cricket)

#FUNCTIONS

def line():
    print('-' *88)


def line1():
    print('-' *50)

def choice1or2():
    while True:
        try:
            while True:
                value=int(input('1 0r 2:'))
                if value == 1 or value == 2:
                    return value

                else:
                    raise ValueError

        except:
            print('Error Try Again')

def rules():
    print("Rules of Odd or Even (Hand Cricket):")
    print(1, ") This game is played between a player and Python.")
    print(2, ") The game starts with a toss using 'odd' or 'even'.")
    print(3, ") Both player and Python choose a number (from 0 to 10) for the toss.")
    print(4, ") The sum of both numbers is calculated.")
    print(5, ") If the sum is odd and the player chose 'odd', the player wins the toss (same for 'even').")
    print(6, ") The toss winner decides to bat or bowl first.")
    print(7, ") In each turn, both player and Python choose a number (from 0 to 10).")
    print(8, ") If both choose the same number, the batsman is OUT.")
    print(9, ") If the numbers are different, the batsman gets the number they chose as runs.")
    print(10, ") The batting continues until the batsman is out.")
    print(11, ") Then roles switch – the one who was bowling now bats.")
    print(12, ") The second innings continues until the new batsman is out or beats the first score.")
    print(13, ") The one with the higher score at the end wins the game.")


def choice0to10():
    while True:
        try:
            while True:
                value=int(input('Enter a Number From 0 to 10:'))
                if value >= 0 and value <= 10:
                    return value

                else:
                    raise ValueError

        except:
            print('Error Try Again')


def random0to10():
    return random.randint(0,10)    


def tosswin():
    if toss == 1:
        if toss_result%2 == 1:
            return 1   #Player win toss

        else:
            return 2   #Python win toss

    elif toss == 2:
        if toss_result%2 == 0:
            return 1   #Player win toss

        else:
            return 2   #Python win toss
    

def bat_or_bowl():
    if toss_winner == 1:
        print('Bat(1) Or Bowl(2)')
        player = choice1or2()
        print('Player Status : First', dict3[player])
        return player  # 1 - Player choose bat , 2 - Player choose bowl

    elif toss_winner == 2:
        python = random.randint(1,2)
        if python == 1:
            print('Python choose :' , dict3[python])
            print('Player Status : First', dict4[python])
            return 2   # Player - bowl , Python - bat
        
        elif python == 2:
            print('Python choose :' , dict3[python])
            print('Player Status : First', dict4[python])
            return 1   # Player - bat , Python - bowl
            

def bat():
    print('Player Status :' , dict3[bat_or_bowl])
    print('Python Status :' , dict4[bat_or_bowl])

    global no_of_balls_pl , no_of_balls_py , player_runs , python_runs , strike_rate_pl , strike_rate_py , winner

    while True:
        print('Current Score of Player :', player_runs)
        print('No. of Balls Faced by Player :' , no_of_balls_pl)
        print('Current Strike Rate of Player :',strike_rate_pl)
        line1()
        
        no_of_balls_pl += 1
        print('Ball No. :' , no_of_balls_pl)
        player = choice0to10()
        python = random0to10()
        print('Python :' , python)

        if player != python:
            if player == 0:
                player_runs += python
            else:
                player_runs += player

        else:
            strike_rate_pl = (player_runs/no_of_balls_pl)*100
            line()
            print('OOPS out!!!')
            print('Total Score of Player :', player_runs)
            print('No. of Balls Faced :' , no_of_balls_pl)
            print('Strike Rate :',strike_rate_pl)
            print('Python needs', player_runs + 1 , 'Runs to Win')
            line()
            break

        strike_rate_pl = (player_runs/no_of_balls_pl)*100
            
    print('Player Status :' , dict4[bat_or_bowl])
    print('Python Status :' , dict3[bat_or_bowl])                
    while True:
        while python_runs <= player_runs:
            print('Current Score of Python:', python_runs)
            print('No. of Balls Faced by Python:' , no_of_balls_py)
            print('Current Strike Rate of Python:',strike_rate_py)
            line1()
            
            no_of_balls_py += 1
            print('Ball No. :' , no_of_balls_py)
            player = choice0to10()
            python = random0to10()
            print('Python :' , python)

            if player != python:
                if python == 0:
                    python_runs += player
                else:
                    python_runs += python

            else:
                strike_rate_py = (python_runs/no_of_balls_py)*100
                print('OOPS out!!!')
                print('Total Score of Python :', python_runs)
                print('No. of Balls Faced by Python:' , no_of_balls_py)
                print('Strike Rate of Python:',strike_rate_py)
                print('GAME OVER!!!')
                winner = 1
                line()
                break
                
            strike_rate_py = (python_runs/no_of_balls_py)*100

        if python_runs > player_runs:            
            print('Current Score of Python:', python_runs)
            print('No. of Balls Faced by Python:' , no_of_balls_py)
            print('Current Strike Rate of Python:',strike_rate_py)
            print('GAME OVER!!!')
            winner = 2
        line()
        break


def bowl():
    print('Player Status :' , dict3[bat_or_bowl])
    print('Python Status :' , dict4[bat_or_bowl])

    global no_of_balls_pl , no_of_balls_py , player_runs , python_runs , strike_rate_pl , strike_rate_py , winner

    while True:
        print('Current Score of Python:', python_runs)
        print('No. of Balls Faced by Python :' , no_of_balls_py)
        print('Current Strike Rate of Python :',strike_rate_py)
        line1()
        
        no_of_balls_py += 1
        print('Ball No. :' , no_of_balls_py)
        player = choice0to10()
        python = random0to10()
        print('Python :' , python)

        if player != python:
            if python == 0:
                python_runs += player
            else:
                python_runs += python

        else:
            strike_rate_py = (python_runs/no_of_balls_py)*100
            line()
            print('OOPS out!!!')
            print('Total Score of Python :', python_runs)
            print('No. of Balls Faced by Python :' , no_of_balls_py)
            print('Strike Rate of Python :',strike_rate_py)
            print('Player needs', python_runs + 1 , 'Runs to Win')
            line()
            break

        strike_rate_py = (python_runs/no_of_balls_py)*100
            
    print('Player Status :' , dict4[bat_or_bowl])
    print('Python Status :' , dict3[bat_or_bowl])                
    while True:
        while python_runs >= player_runs:
            print('Current Score of Player:', player_runs)
            print('No. of Balls Faced by Player:' , no_of_balls_pl)
            print('Current Strike Rate of Player:',strike_rate_pl)
            line1()
            
            no_of_balls_pl += 1
            print('Ball No. :' , no_of_balls_pl)
            player = choice0to10()
            python = random0to10()
            print('Python :' , python)

            if player != python:
                if player == 0:
                    player_runs += python
                else:
                    player_runs += player

            else:
                strike_rate_pl = (player_runs/no_of_balls_pl)*100
                print('OOPS out!!!')
                print('Total Score of Player :', player_runs)
                print('No. of Balls Faced by Player :' , no_of_balls_pl)
                print('Strike Rate of Player :',strike_rate_pl)
                print('GAME OVER!!!')
                winner = 2
                line()
                break
                
            strike_rate_pl = (player_runs/no_of_balls_pl)*100

        if python_runs < player_runs:            
            print('Current Score of Player:', player_runs)
            print('No. of Balls Faced by Player:' , no_of_balls_pl)
            print('Current Strike Rate of Player:',strike_rate_pl)
            print('GAME OVER!!!')
            winner = 1
        line()
        break
    

def scorecard():
    print('ODD OR EVEN :: SCORECARD')
    print('PLAYER CHOOSE :' , dict1[toss])
    print(dict2[toss_winner], 'won toss')
    if toss_winner == 1:
        print('PLAYER VOTE FOR', dict3[bat_or_bowl])
    else:
        print('PYTHON VOTE FOR', dict4[bat_or_bowl])
    print()
    if bat_or_bowl == 1:
        print('Total Score of Player :', player_runs)
        print('No. of Balls Faced by Player :' , no_of_balls_pl)
        print('Strike Rate of Player :',strike_rate_pl)
        print()
        print('Python needed', player_runs + 1 , 'Runs to Win')
        print()
        print('Total Score of Python :', python_runs)
        print('No. of Balls Faced by Python:' , no_of_balls_py)
        print('Strike Rate of Python:',strike_rate_py)
        print()
    else:
        print('Total Score of Python :', python_runs)
        print('No. of Balls Faced by Python:' , no_of_balls_py)
        print('Strike Rate of Python:',strike_rate_py)
        print()
        print('Player needed', python_runs + 1 , 'Runs to Win')
        print()
        print('Total Score of Player :', player_runs)
        print('No. of Balls Faced by Player :' , no_of_balls_pl)
        print('Strike Rate of Player :',strike_rate_pl)
        print()
    print(dict2[winner],'Won the Game!!!!!')


#Variables
no_of_balls_pl = 0
no_of_balls_py = 0
strike_rate_pl = 0
strike_rate_py = 0
player_runs = 0
python_runs = 0
winner = None
dict1 = {1 : 'Odd' , 2 : 'Even' }
dict2 = {1 : 'Player' , 2 : 'Python'}
dict3 = {1 : 'Batting' , 2 : 'Bowling'}
dict4 = {1 : 'Bowling' , 2 : 'Batting'}


#__main__.py

import random

rules()
line()

print('ODD(1) or EVEN(2) for toss:')
toss = choice1or2()
print('Player choose :' , dict1[toss])
line()

print('Enter a number from 0 to 10 to check whether odd or even:')
toss_pl = choice0to10()
print('Player :' , toss_pl)


toss_py = random0to10()
print('Python :', toss_py)
line()

toss_result = toss_pl + toss_py
toss_winner= tosswin()
print('Toss winner is :',dict2[toss_winner])
line()


bat_or_bowl = bat_or_bowl()   # 1 - Player first batting , 2 - Player first bowling
line()

if bat_or_bowl == 1:
    bat()
else:
    bowl()

print(dict2[winner],'Won the Game!!!!!')

scorecard()



#MUTHUVEL P
#9.2
  
