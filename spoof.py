import random
player = 1
coins = 8

def modified_spoof(coins,player):
  while coins > 0:
    print(f"Player {player}, there are {coins} coins left.")
    if player == 1:
      move = int(input("Enter number of coins to take (1-3): "))
      
      if move < 1 or move > 3:
        print("Invalid move. Try again.")
        continue
      else:
        coins -= move
        print(f"Player {player} takes {move} coins.\n")
    else:
      move = ai_strategy(move)
      coins -= move
      print(f"AI takes {move} coins.\n")
    if coins<1:
      print(f"Player {player} loses!")
    else:
      player = 2 if player == 1 else 1

def ai_strategy(coins_left):
    if coins_left % 4 == 0:
      # If there are 4 or more coins remaining, take 3 to leave opponent with 4 coins
      return 3
    elif coins_left % 4 == 1:
      # If there are 3 coins remaining, take 2 to leave opponent with 1 coin
      return 2
    else:
      # Otherwise, take 1 coin
      return 1
  

# Start game with a random number of coins

modified_spoof(coins,player)
