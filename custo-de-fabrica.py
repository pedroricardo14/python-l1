fabrica = float(input("Preço de fábrica: "))
distrib = fabrica * 12 / 100
imposto = fabrica * 45 / 100
total = fabrica + distrib + imposto
print(f"Total a pagar: R$ {total:.2f}")
