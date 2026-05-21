import emoji

while True:
    user_input = input("Input: ")
    if user_input.lower() == "quit":
        break
    else:
        result = emoji.emojize(user_input, language="alias")
        print(f"Output: {result}")