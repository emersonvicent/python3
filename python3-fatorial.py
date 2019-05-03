n = int(input("Digite o valor de n: "))
terminou = False
fator = 0
x = n
while not(terminou):
  if n == 0:
    terminou = True
    fator = 1
  elif x == 0:
    terminou = True
  else:
    fator = n * ( x - 1 )
    x = x - 1
    n = fator
    terminou = False
print(fator)
