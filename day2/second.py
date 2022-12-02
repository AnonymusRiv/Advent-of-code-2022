# A = Rock       |1
# B = Paper      |2
# C = Scissors   |3
# Rock > Scissors || Paper > Rock || Scissors > Paper
# X = lose
# Y = empty
# Z = win
# SCORE = A + 0/3/6

score = 0

with open('input.txt') as file:
    for line in file:
        if line != '\n':
            aux = line.splitlines() and line.split(" ")
            char1 = aux[0]
            char2 = aux[1]
            char2 = char2.strip("\n")

            if char1 == "A":
                if char2 == "X":
                    score = score + 3 + 0
                elif char2 == "Y":
                    score = score + 1 + 3
                elif char2 == "Z":
                    score = score + 2 + 6

            elif char1 == "B":
                if char2 == "X":
                    score = score + 1 + 0
                elif char2 == "Y":
                    score = score + 2 + 3
                elif char2 == "Z":
                    score = score + 3 + 6

            elif char1 == "C":
                if char2 == "X":
                    score = score + 2 + 0
                elif char2 == "Y":
                    score = score + 3 + 3
                elif char2 == "Z":
                    score = score + 1 + 6

print(f"Your score is {score}")