max = 0
i = 0

with open('input.txt') as file:
    for line in file:
        if line != '\n':
            aux = int(line)
            i = i + aux
        else:
            if max < i:
                max = i
            i = 0

print(f"The most calories carryed is {max}")