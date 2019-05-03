# Receba um número inteiro positivo na entrada e imprima os n n primeiros números ímpares naturais. 
# Para a saída, siga o formato do exemplo abaixo.
n = int(input("Digite o valor de n: "))
c = i = 1
while c <= n:
  if i % 2 == 0:
    i += 1
  elif i % 2 == 1:
    print(i)
    i += 1
    c += 1



