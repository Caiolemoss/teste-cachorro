print("Bem-vindo ao PETSHOP!")

# 1. Nome e idade do pet
nome = input("Qual o nome do pet? ")
idade_humana = int(input("Qual a idade do pet (em anos)? "))

idade_cachorro = idade_humana * 7

# 2. Porte do cachorro
print("Qual o porte do cachorro?")
print("1 - Grande")
print("2 - Médio")
print("3 - Pequeno")
porte = input("Digite a opção: ")

if porte == "1":
    valor_banho = 75.00
    custo_banho = 20.00
elif porte == "2":
    valor_banho = 60.00
    custo_banho = 15.00
elif porte == "3":
    valor_banho = 50.00
    custo_banho = 5.00
else:
    print("Opção inválida!")
    exit()

# 3. Banhos e lucro
qtd_banhos = int(input("Quantos banhos nos últimos 12 meses? "))

lucro_por_banho = valor_banho - custo_banho
lucro_total = lucro_por_banho * qtd_banhos

# 4. Mensagem final
lucro_formatado = f"{lucro_total:.2f}".replace(".", ",")

print(f"Olá, {nome} tem {idade_cachorro} anos e nos últimos 12 meses o lucro com este animal foi de R${lucro_formatado}")
