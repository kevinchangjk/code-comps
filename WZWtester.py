import random

numberso = '9822'*20000
index = random.randint(0, 79999)
original = numberso[index]
applicable = [str(i) for i in range(10)]
applicable.remove(original)
changed = random.choice(applicable)

numberso = list(numberso)
numberso[index] = changed
numberso = "".join(numberso)

numbers = numberso

solving = True
index = 0
while solving:
    if len(numbers) == 0:
        print('No different number.')
        solving = False
    elif len(numbers) < 4:
        print('Missing number?')
        solving = False
    if numbers[:4] == "9822":
        numbers = numbers[4:]
        index +=4
    else:
        if numbers[0] != '9':
            index +=1
            numberss = '9'
        elif numbers[1] != '8':
            index +=2
            numberss = '8'
        elif numbers[2] != '2':
            index +=3
            numberss = '2'
        elif numbers[3] != '2':
            index +=4
            numberss = '2'
        solving = False
        print(f"Different number at the {index} digit.")
        print(numberso[index-1]+" but supposed to be "+numberss)