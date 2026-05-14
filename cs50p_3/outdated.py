months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    get_date()

def get_date():
    
    while True: 
        try:
            date = input("Date: ")
            if  "/" in date:
                m, d, y = date.split("/")
                m = int(m)
                if m < 1 or m > 12:
                    continue
                d = int(d)
                if d < 1 or d > 31:
                    continue
                y = int(y)
                print(f"{y:04}-{m:02}-{d:02}")
                return
                
            else:
                date_replace = date.replace(",", "")
                m, d, y = date_replace.split(" ")
                m = months.index(m) + 1
                if m < 1 or m > 12:
                    continue
                d = int(d)
                if d < 1 or d > 31:
                    continue
                y = int(y)
                print(f"{y:04}-{m:02}-{d:02}")
                return
                  
        except (ValueError):
            continue

if __name__ == "__main__":
    main()  