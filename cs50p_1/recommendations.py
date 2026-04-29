def main():
    difficulty = input("Difficult or Casual? ").lower() 
    if difficulty not in ("difficult", "casual"):
        print("Enter a valid difficulty")
        return
    players = input("Single or Multiplayer? ").lower()
    if players not in ("single", "multiplayer"):
           print("Enter a valid player mode.") 
           return
    recommend(difficulty, players)               

# We give recommend() both pieces of info it needs to do its job
def recommend(difficulty, players):
    if difficulty == "difficult" and players == "single":
        print("We recommend: Catan")      
    elif difficulty == "difficult" and players == "multiplayer":
        print("We recommend: Euchre")
    elif difficulty == "casual" and players == "single":
         print("We recommend: Solitaire") 
    elif difficulty == "casual" and players == "multiplayer":
        print("We recommend: Old Maid")
              
           
main()



