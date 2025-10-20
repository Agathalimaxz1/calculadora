from operacoes import *
import emoji

n1 = int(input("Digite o número: "))
n2 = int(input("Digite o número: "))
    
print('''
          
CALCULADORA - HTA DIVONICA       
          [1] SOMA
          [2] SUBTRAÇÃO
          [3] MULTIPLICAÇÃO
          [4] DIVISÃO
          [0] SAIR
          ''')
    
while True:
    num  = input("Escolha uma opção de 1 a 4 e 0 para sair: ")
    if num == "1":
        print(f'Resultado: {soma(n1, n2)}')
        break
    elif num == "2":
        print(f"Resultado: {subtracao(n1, n2)}")
        break  
    elif num == "3":
        print(f"Resultado: {multiplicacao(n1, n2)}")
        break
    elif num == "4":
        print(f"Reultado: {divisao(n1, n2)} ")
        break
    elif num == "0":
        print("Programa finalizado")
        break
print(emoji.emojize("programa finalizado :red_heart: "))