height = int(input("What is your height?"))
bill=0

if height>=120:
    print("You can go for rollercoster ride")
    age = int(input("What is your age? "))
    if age< 12:
        bill = 5
        print("Child ticket is $5")
    elif age <=18:
        print("Youth ticket is 7")
        bill=7
    else:
        print("Adult ticket is $12")
        bill=12
    want_to_take_photo = input("Do you want to take photo? Type y for Yes and n for No")
    if want_to_take_photo == 'y':
        bill += 3
    print(f"Your final bill is ${bill}")
else:
    print("You can't got for ride")