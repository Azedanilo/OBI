info = [int(x) for x in input().split()]
tuneis = {}
possivel = 0

for i in range(info[1]):
    tunel = [x for x in input().split()]
    try: 
        tuneis[tunel[0]].append(tunel[1])
    except: 
        tuneis.update({tunel[0]: [tunel[0], tunel[1]]})

    try: 
        tuneis[tunel[1]].append(tunel[0])
    except: 
        tuneis.update({tunel[1]: [tunel[0], tunel[1]]})
 
# print(tuneis)

# for i in range(int(input())):
#     firstRun = True
#     previousCell = None
#     possible = True
#     # caminho = [int(x) for x in input().split()]

#     for i in input().split()[1:]:
#         if firstRun:
#             previousCell = i
#             firstRun = False
#             continue

#         # print(i)

#         # print(i, previousCell)
#         # print(previousCell in tuneis[i])

#         if previousCell in tuneis[i]:
#             previousCell = i
#         else:
#             possible = False
#             break
        
    
#     if possible: possivel += 1

# print(possivel)

for i in range(int(input())):
    caminho = input().split()[1:]
    # print(caminho)
    possible = True
    # caminho = [int(x) for x in input().split()]

    for i,ii in enumerate(caminho[:-1]):
        if ii not in tuneis[caminho[i+1]]:
            possible = False
            break
    
    if possible: possivel += 1

print(possivel)