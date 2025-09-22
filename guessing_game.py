def guessing_game():
    answer=15
    correct=0
    while (correct==0):
        Theirguess=int(input())
        if((Theirguess)==answer):
            correct=1
            return "Congratulations! You guessed it!"
        elif(Theirguess<answer):
            return "Too Low! Guess again."
        elif(Theirguess>answer):
            return "Too High! Guess again."
