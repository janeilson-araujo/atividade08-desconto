# Informe um valor e veja quanto de desconto você terá em R$, receba a % do desconto que quer receber;

print("Calculadora de descontos")
valor = float(input("Digite o valor em reais:"))
porcentagem = int(input("Digite a porcentagem de desconto:"))
desconto = (porcentagem/100)*valor
desconto_final = valor - desconto
print(f'voce tera um vlor final de: {desconto_final} reais.')