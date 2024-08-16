import random as rd
friends = ["Alice","Bob","Charlie","David","Emanuel"]
who_pay_bill = friends[rd.randint(0,4)]
print(who_pay_bill)
print(f"Today bill is paid by {who_pay_bill}")