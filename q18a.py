import random
# print("\u25CF \u250C \u2500 \u2150 \u2502 \u2514 \u2518") #Some ASCII needed for our question!!
# ● ┌ ─ ┐ │ └ ┘

dice_art = {
1:(       "┌─────────┐",
          "│         │",
          "│    ●    │",
          "│         │",
          "└─────────┘"),     #Intresting ASCII art ryt!

2:(       "┌─────────┐",
          "│  ●      │",
          "│         │",
          "│      ●  │",
          "└─────────┘"),

3:(       "┌─────────┐",
          "│  ●      │",
          "│    ●    │",
          "│      ●  │",
          "└─────────┘"),

4:(       "┌─────────┐",
          "│  ●   ●  │",
          "│         │",
          "│  ●   ●  │",
          "└─────────┘"),

5:(       "┌─────────┐",
          "│  ●   ●  │",
          "│    ●    │",
          "│  ●   ●  │",
          "└─────────┘"),

6:(       "┌─────────┐",
          "│  ●   ●  │",
          "│  ●   ●  │",
          "│  ●   ●  │",
          "└─────────┘")
}
dice=[]
total=0
dice_num=int(input("How many dices u wanna roll?: "))

for die in range(dice_num):
    r = random.randint(1,6)
    dice.append(r)

for die in range(dice_num):
    for line in dice_art.get(dice[die]):
        print(line)

for die in dice:
    total += die
    
print(dice)
print(f"Total: {total}")

# EXPLAINATION for the lines 50 to 52!!!
# dice_num = 2
# dice = [5, 2]

# die = 0:
    # dice[0] = 5
    # dice_art.get(5) → prints face 5

# die = 1:
    # dice[1] = 2
    # dice_art.get(2) → prints face 2