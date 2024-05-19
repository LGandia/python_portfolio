#dice point system
player1_points = 0
player2_points = 0
player_1 = 'a'
player_2 = 'b'
rounds = 0
import random
#Player verification
verified_players=['laura','marta','diana']
number_of_players=0
for i in range(1,3):
    print('Player ',i,":")
    user=str(input('Please enter your username: '))
    user = user.lower()
    if user in verified_players:
        print('Player',i,' access granted')
        if i == 1:
            player_1 = user
        else:
            player_2 = user
        number_of_players=number_of_players+1
    else:
        print('Player',i,' access denied')
        break
#dices
    if number_of_players == 2:
        while rounds != 5:
            rounds=rounds+1
            print ('---------- Round ',rounds,'----------')
            
            dice1 = random.randint(1,12)
            dice2 = random.randint(1,12)
            dice3 = random.randint(1,6)
            dice4 = random.randint(1,6)
#player1 points and dice
            player1_points = player1_points + dice1
            if dice1 % 2 == 0:
                player1_points = player1_points+10
            else:
                if player1_points-5 < 0:
                    player1_points = player1_points+0
                else:
                    player1_points = player1_points-5

#player2 points and dice
            player2_points = player2_points + dice2
            if(dice2 % 2 == 0):
                player2_points = player2_points+10
            else:
                if player2_points-5 < 0:
                    player2_points = player2_points+0
                else:
                    player2_points = player2_points-5
            print("Player One's score: ",player1_points)
            print("Player Two's score: ",player2_points)
#Extra dices
        while player1_points == player2_points:
            print('----------EXTRA ROUND----------')
            #player1
            player1_points = player1_points+dice3
            if(dice3 % 2 == 0):
                player1_points = player1_points+10
            else:
                if player1_points-5 < 0:
                    player1_points = player1_points+0
                else:
                    player1_points = player1_points-5
            #player2
            player2_points = player2_points+dice3
            if(dice4 % 2 == 0):
                player2_points = player2_points+10
            else:
                if player2_points-5 < 0:
                    player2_points = player2_points+0
                else:
                    player2_points = player2_points-5
                break
            print("Player One's score: ",player1_points)
            print("Player Two's score: ",player2_points)
print('...................................')
if player1_points > player2_points:
    print('Player 1 wins with', player1_points,'points')
    winner_points = player1_points
    winner = player_1
elif player1_points < player2_points:
    print('Player 2 wins with', player2_points,'points')
    winner_points = player2_points
    winner = player_2
else:
    print('...................................')

#leaderboard
file=open("score.txt","a")
file.write(str(winner_points)+","+winner+"\n")
file.close()

file=open("score.txt","r")
readthefile = file.readlines()
sortedData = sorted(readthefile,reverse=True)
print("\nTop 5 Scores")
print("Pos\tPoints,Name")
for line in range (5):
    print(str(line+1)+"\t"+str(sortedData[line]))
