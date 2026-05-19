def main():
    amount_due = 50
   
    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        coke = int(input("Insert Coin: "))
        if coke in (25, 10, 5):
            amount_due = amount_due - coke
           
        
    print(f"Change Owed: {-amount_due}")

main()