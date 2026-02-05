
import pyfiglet
import sys
import random

fonts = pyfiglet.FigletFont.getFonts()

if len(sys.argv) == 3:
    if sys.argv[1] != "-f" and sys.argv[1] != "--font":
        sys.exit(1)
    elif sys.argv[2] not in fonts:
        sys.exit(1)
    else:
        text = input("Write a text: ")
        user_font = sys.argv[2]  
        print(user_font)                                               
        print(pyfiglet.figlet_format(text, font=user_font))
elif len(sys.argv) == 1:
    text = input("Write a text: ")
    random_font = random.choice(fonts)
    print(pyfiglet.figlet_format(text, font=random_font))
else: 
    sys.exit(1)