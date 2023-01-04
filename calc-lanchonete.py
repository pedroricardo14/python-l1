hamb = int(input("Quantos Hambúrgueres? "))
ches = int(input("Quantos Cheeseburgueres? "))
frit = int(input("Quantas Batatas? "))
refr = int(input("Quantos refrigerantes? "))
shak = int(input("Quantos Milkshakes? "))

total = hamb*9.00 + ches*7.50 + frit*8.50 + refr*5.5 + shak*14.00

print(f"Total da conta: R$ {total:.2f}")
