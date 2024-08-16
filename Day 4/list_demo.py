import random as rd
friends = ["Alice","Bob","Charlie","David","Emanuel"]
#Use this simple approach to generate random number between 0 to N.
who_pay_bill = friends[rd.randint(0,4)]
print(who_pay_bill)
print(f"Today bill is paid by {who_pay_bill}")

#alternate approach to get random item from the sequence data type
who_pay_bill1 = rd.choice(friends)
print("Alternate person who will pay bill is ", who_pay_bill1)