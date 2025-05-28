import random

print("Olá! Escolha 0 para pedra, 1 para papel e 2 para tesoura")

pedra = ''' 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
imagens_jogo = [pedra, papel, tesoura]


sua_escolha = int(input("Sua escolha:"))
if sua_escolha >= 0 and sua_escolha <=2:
    print(imagens_jogo[sua_escolha])
maquina_escolha = random.randint(0, 2)
print(f"A maquina escolheu: {maquina_escolha}")
print(imagens_jogo[maquina_escolha])

if sua_escolha >=3 or sua_escolha <0:
    print("Esse número não existe, você perdeu")
if sua_escolha == 0 and maquina_escolha == 2:
    print("Você venceu!")
elif maquina_escolha == 0 and sua_escolha == 2:
    print("Você perdeu")
elif maquina_escolha > sua_escolha:
    print("A maquina ganhou")
elif sua_escolha > maquina_escolha:
    print("Você ganhou")
elif maquina_escolha == sua_escolha:
    print("Empate")


else:
    print("Você digitou um número inexistente, Você perdeu!")
