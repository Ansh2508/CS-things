import random
ls = ["umbrella","good","japan","laptop"]
x = random.choice(ls)
a = ''.join(random.sample(x, len(x)))
print(a)
b = input("Guess the correct word:"    )
if b == x:
    print("Correct")
else:
    print("Incorrect")
