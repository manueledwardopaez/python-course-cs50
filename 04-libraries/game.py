import random

while True:
    # Prompt user for positive int.
    try:
        n = int(input("Level: "))
        if n > 0:
            # Generates random int between 1 - n 
            number = random.randint(1, n)
            print(f"Random  number: {number} " )
            while True:
                try: 
                    # Prompt user to guess the number
                    guess = int(input("Guess: "))
                    if guess > 0:
                        # Evaluate users prompt
                        if guess < number:
                            print("Too small!")
                        elif guess > number:
                            print("Too large!")
                        else:
                            print("Just right!")
                            break
                # Re prompt if guess is not an int
                except ValueError:
                    continue
            break
    # Re prompt if n is not an int
    except ValueError:
        continue







