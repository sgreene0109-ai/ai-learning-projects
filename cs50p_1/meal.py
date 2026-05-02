def main():
    time = input("What time is it? ")
    result = convert(time)
    if 7.0 <= result <= 8.0:
        print("breakfast time")
    elif 12.0 <= result <= 13.0:
        print("lunch time")
    elif 18.0 <= result <= 19.0:
        print("dinner time")

def convert(time):
    strip = time.replace(".", "")
    parts = strip.split()
    if len(parts) == 1:
        parts = time.split(":")
        x = float(parts[0])
        y = float(parts[1]) / 60
        return x + y
    elif parts[1] == "pm":
        parts2 = parts[0].split(":")
        x = float(parts2[0])
        if x != 12.0:
                x += 12
        y = float(parts2[1]) / 60
        return x + y
    elif parts[1] == "am": 
        parts2 = parts[0].split(":")  
        x = float(parts2[0])
        if x == 12.0:
            x = 0.0
        y = float(parts2[1])/60
        return x + y
    else:
        parts = time.split(":")
        x = float(parts[0])
        y = float(parts[1])/60
        return x + y

main()