from operacoes import *

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
    num  = input("Escolha uma opção de 1 a 4, e 0 para sair: ")
    if num == "1":
        print(f'Resultado: {soma(n1, n2)}')
        break
  

