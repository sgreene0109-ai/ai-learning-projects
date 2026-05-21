import random


def main():
   n = level()
   guess(n)

def level():
    while True:
        try:
            n = int(input("Level: "))
            if n > 0:
             number = random.randint(1, n)
             return number
            else:
               continue
        except (ValueError):
            continue

def guess(number):
    while True:
       try:
          guess = int(input("Guess: "))
          if guess <= 0:
             continue
          elif guess < number:
             print("Too small!")
             continue
          elif guess > number:
             print("Too large!")
             continue
          else:
            print("Just right!")
            break             
       except (ValueError):
         continue
if __name__ == "__main__":
    main()  


   

    

