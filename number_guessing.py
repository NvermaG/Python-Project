import random
n=random.randint(1,10)
count=0
while (n!="guess"):
    if(count==3):
        print("you loose the game")
        break
    guess = int(input("Enter the guessing number"))
    if(guess<n):
        print('guess is low')
    elif(guess>n):
        print('guess is high')
    elif(guess==n):
        print('you guessed it')
        break
    count+=1