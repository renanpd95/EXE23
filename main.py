import os

print("**LOJA MAMÃO COM AÇUCAR**")
val = float(input("Quanto da Compra: R$"))

prest = val/12
os.system("clear")
print("**LOJA MAMÃO COM AÇUCAR**")
print("Valor total do produto: R$",val)
print(f"Valor que será pago na prestação: R${prest:.2f}")