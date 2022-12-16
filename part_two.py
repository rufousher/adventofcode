with open('input.txt') as f:
    data = f.readlines()

print(sorted(data)[-3:])
