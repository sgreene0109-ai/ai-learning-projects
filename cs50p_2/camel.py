def main():
    camel = input("camelCase: ")
    snake = ""
    for letter in camel:
        if letter.isupper():
          snake += "_" + letter.lower()
        else:
            snake += letter.lower()
    print(snake)
main()