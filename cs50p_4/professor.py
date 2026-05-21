import random


def main():
    math_level = get_level()
    score = 0
    for i in range(10):
        x = generate_integer(math_level)
        y = generate_integer(math_level)
        for j in range(3):        
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == x + y:
                    score += 1
                    break
                else:
                    print("EEE")
            except (ValueError):
                print("EEE")
                continue
        else:
            print(f"{x} + {y} = {x + y}") 
    print(f"Score: {score}")           
    
def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n in (1, 2, 3):
             return n
            else:
               continue
        except (ValueError):
            continue
            
def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)        
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Invalid level")
    
  
  
if __name__ == "__main__":
    main()  