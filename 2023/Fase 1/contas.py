disp = int(input())
info = [int(input()) for i in range(3)]
total = 0
quant = 0

info = sorted(info)

for i in info:
    total += i
    if total > disp:
        break
    quant += 1


print(quant)
