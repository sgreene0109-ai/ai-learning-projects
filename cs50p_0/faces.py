

def main ():
    faces = input("Are you happy or sad? ")
    print(convert(faces))

def convert(s):
    s = s.replace(":)", "🙂" )
    s = s.replace(":(", "🙁")
    return s

main()


