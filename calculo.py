name = input("Digite seu nome: ")
print(f"Olá, seja bem-vindo {name}!")

idade = int(input("Agora digite para mim a sua idade: "))
print(f"Uau! você tem {idade} anos, que legal!")

print("Agora peço que você efetue um cálculo, ok?")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("Escolha a operação que deseja realizar:")
print(" + para adição")
print(" - para subtração")
print(" * para multiplicação")
print(" / para divisão")

operacao = input("Digite a operação desejada: ")

if operacao == "+":
    resultado = num1 + num2
    print(f"Resultado da adição: {resultado}")
elif operacao == "-":
    resultado = num1 - num2
    print(f"Resultado da subtração: {resultado}")
elif operacao == "*":
    resultado = num1 * num2
    print(f"Resultado da multiplicação: {resultado}")
    if resultado == resultado:
        print(f"o resultado é: {resultado}")
    
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
        print(f"Resultado da divisão: {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Operação inválida. Por favor, tente novamente.")
