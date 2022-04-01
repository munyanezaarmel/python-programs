unswer=5
print("Please guess a number between 1  nd 10:")
guess=int(input())

if guess<unswer:
    print("Guessing higher")
    guess=int(input())

elif guess>unswer:
    print("guessing lower")
else:
    print("you got it first time")

   

