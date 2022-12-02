top1 = 0
top2 = 0
top3 = 0
i = 0

with open('input.txt') as file:
    for line in file:
        if line != '\n':
            aux = int(line)
            i = i + aux
        else:
            if top1 < i:
                top3 = top2
                top2 = top1
                top1 = i
            elif top2 < i:
                top3 = top2
                top2 = i
            elif top3 < i:
                top3 = i
            i = 0

print(f"The calories that carryed the 3 Elf is {top1 + top2 + top3}")