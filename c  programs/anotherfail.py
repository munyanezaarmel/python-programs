answer=5
print("please guess a number between 1 and 10")
guess=int(input())
if guess!=answer:
    if guess<answer:
        print('PLEASE GUESS HIGHER')
        else:
            print("please guess lower")
            guess=int(input())
            if guess==answer:
                print('well done,you guessed it')
                else:
                    print("sorry, you have not guessed correctly")
                    else:
                        print("you got it first time")
                        

