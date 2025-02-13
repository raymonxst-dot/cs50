import random
while True:
    try:
        n =int(input("Level:"))
        if n > 0:    
            System_choise=random.randint(1,n)
    except (ValueError):
        continue
    else:
        break
while True:
    try:
        user_choise=int(input("Guess:"))
    except(ValueError):
        continue
    if user_choise < System_choise:
        print("Too small!")
    elif user_choise > System_choise:
        print("Too large!")
    else:
        print("Just right!")
        break