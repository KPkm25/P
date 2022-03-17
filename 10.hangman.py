

def play_hangman():
    name=input("What's your name?")
    print(f"Hello {name}, time to play hangman!")
    print("Start guessing...")
    print("HINT: Word is name of a fruit\n")

    word="apple"

    guesses=""

    turns=len(word)+2

    while turns>0:
        failed=0
        for char in word:
            if char in guesses:
                print(char)
            else:
                print("_")
                failed+=1
        if failed==0:
            print("You won the game\n")
            break
        guess=input("Guess a char: ")
        guesses+=guess

        if guess not in word:
            turns-=1
            print("Wrong guess")
            print(f"You have {turns} more guesses")
        if turns==0:
            print("You lose")
if __name__=="__main__":
    play_hangman()

