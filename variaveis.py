a = input("Valor de A: ")

b = input("Valor de B: ")

#trocando

c = a      # c é variável auxiliar

a = b

b = c          # a, b = b,a   # poderia ser assim também

print(f"Novo valor de A: {a}")

print(f"Novo valor de B: {b}")
