# print ("Game Records")
# user_name = input("Enter name: ")
# user_score = input("Enter score: ")
# print("You entered:", user_name , user_score)

# # Initialize an empty dictionary
# game_records = {}

# # Input from user
# user_name = input("Enter name: ")
# user_score = input("Enter score: ")

# # Adding the name and score to the dictionary
# game_records[user_name] = user_score

# # Print the dictionary to confirm
# print("Current game records:", game_records)
import csv

all_low_games= ["uno", "chicken foot"]
all_high_games=["scrabble", "monopoly", "quirkle", "pictionary", "monopoly deal"]

game_name = input("Enter the game name: ")
game_name = game_name.lower()
if game_name not in all_high_games and game_name not in all_low_games:
    print("Game not found")
else:
    num_players = input("Enter no. of players: ")
    my_scorecard = {}
    for player in range(int(num_players)):
        # print (f"hello {player+1}")
        player_name = input(f"Enter player {player+1}:  ")
        player_score = input(f"Enter player {player+1} score: ")
        my_scorecard[player_name] = player_score
        with open("score_file.csv","a") as fh:
            for keys, values in my_scorecard.items():
                # print("hella", keys,values)
                fh.write (f"{keys},{values}\n")

    # print("scorecard after for loop", my_scorecard)
    print("")
    print(f"The {game_name} scores are: ")

    if game_name in all_low_games: 
        ranked_scorecard = sorted(my_scorecard.items(), key = lambda x:x[1])
        print("Ranks: ", ranked_scorecard)

    else:
        ranked_scorecard = sorted(my_scorecard.items(), key = lambda x:x[1], reverse=True)
        print("Ranks: ", ranked_scorecard)

        #hello