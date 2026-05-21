from pyfiglet import Figlet
import sys
import random
text = input("Input: ")
figlet = Figlet()

if len(sys.argv) == 1 :
    fonts = figlet.getFonts()
    style = random.choice(fonts)
    figlet.setFont(font = style)
    print(figlet.renderText(text))
elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] in figlet.getFonts():
            figlet.setFont(font = sys.argv[2])
            print(figlet.renderText(text))
        else:
            sys.exit("Not a font")
    else:
        sys.exit("Not a font")
    



