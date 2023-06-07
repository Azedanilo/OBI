top = [0, 0]

for i in range(int(input())):
    nome = input()
    lance = int(input())

    if lance > top[1]:
        top = [nome, lance]

print(top[0])
print(top[1])