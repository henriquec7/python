nome = input("Escreva seu nome: ")
resposta = input(f"Olá! O seu nome é {nome} mesmo? Se sim digite SIM, caso contrário NÃO \nR: ").strip().lower()
if resposta == "sim":
    print(f"Bem vindo {nome}!")
else:
    print("Por favor, digite seu nome novamente.")

cpf= int(input("Digite seu CPF: "))
endereco = input("Digite seu endereço: ")
numero_endereco = int(input("Digite o número: "))
cep = int(input("Digite o CEP (somente com números): "))
print(f"\n{cpf}\n{endereco}, {numero_endereco}\n{cep}")
dados = input("Seus dados estão corretos? Digite SIM ou digite NÃO: ")

if dados == "sim":
    print(f"Certo, podemos prosseguir {nome}!")
else:
    print("Por favor, insira seus dados novamente.")

