info = [int(x) for x in input().split()]

estoque = [[int(ii) for ii in input().split()] for i in range(info[0])]
vendas = 0

for i in range(int(input())):
    pedido = [int(x) for x in input().split()]
    if estoque[pedido[0]-1][pedido[1]-1] > 0:
        estoque[pedido[0]-1][pedido[1]-1] -= 1
        vendas += 1

print(vendas)