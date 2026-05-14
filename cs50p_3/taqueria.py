menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main ():
    get_menu()


def get_menu():
   bill_total = 0
   while True: 
        try:
            item = input("Item: ").title()
            m = (menu[item])
            bill_total += m
            print(f"Total: ${bill_total:.2f}")
                      
        except (EOFError):
            return
        except (KeyError):
            continue

if __name__ == "__main__":
    main()  