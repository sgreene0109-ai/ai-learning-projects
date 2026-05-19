def main():
    twttr = input("Input: ")
    output = ""
    for letter in twttr:
        if letter.lower() not in ("a", "e", "i", "o", "u"):
          output += letter
   
    print(f"Output: {output}")
main()