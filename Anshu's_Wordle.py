<body>
import random
ls = ["UMBRELLA","SHADENFREUDE","CORNUCOPIA","OCCUR","RUIN","PIANO","SYNDICATE","LIBERALISM","SOCIALISM","CAPITALISM"]
word = random.choice(ls)
turns = 15
guesses = ''

while turns>0:
    print(f"You have {turns} turns left")
    print(f"Number of CHARs:{len(word)}")
    guessed_all = True
    for c in word:
        if c in guesses:
            print(c, end=' ')
        else:
            print('_',end=' ')
            guessed_all = False
    print()
    if not guessed_all:

         gs1 = input("Guess a char:")
         guesses = guesses+gs1
         if gs1 not in word:
            turns = turns-1
    else:
        turns = 0
        <b> <font color ="RED">
         print("YOU WON BABY ;)")</font>
</body>



