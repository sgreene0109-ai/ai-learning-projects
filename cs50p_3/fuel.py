def main():
    x, y = get_fraction()
    percentage = calculate_percentage(x,y)
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")

def get_fraction():
   while True: 
        try:
            fraction = input("Fraction: ")
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)
            if y == 0 or x > y or x < 0:
                continue
            return x, y
        except (ValueError, ZeroDivisionError):
            continue 

def calculate_percentage(x, y):
    percentage = round((x / y) * 100)
    return percentage
if __name__ == "__main__":
    main()  