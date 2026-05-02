math = input("Express: ").split()
x = int(math[0])
y = math[1]
z = int(math[2])

if y == "+":
    result = float(x + z)
    
elif y == "-":
    result = float(x - z)
    
elif y == "*":
    result = float(x * z)
    
elif y == "/":
    result = float(x / z)
    
print(f"{result:.1f}")