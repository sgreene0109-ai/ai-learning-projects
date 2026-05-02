life = input("What is the Answer to the Great Question of Life, the Universe and Everything? ").strip().lower()
if life not in ("42", "forty-two", "forty two"):
    print("No")

else:
    print("Yes")
