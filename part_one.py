with open('input.txt') as f:
    data = f.readlines()

print(sum(map(int, data)))
