menu = """
---- SISTEMA BANCÁRIO ----
------ [1] Depósito ------
------ [2] Saque ---------
------ [3] Extrato -------
------ [0] Sair ----------
"""

saldo = 0
limite_diario = 500
saldo_dict = {}
saque_dict = {}
qnt_saques = 0 
extrato = ""

while True:

     print(menu)
     escolha = int(input('Qual operação deseja realizar? '))

     if escolha == 1:
          print("[1] DEPÓSITO")
          deposito = float(input("Qual valor, em reais, você deseja depositar? R$"))
          if deposito > 0:
               saldo += deposito
               extrato += (f'Depósito de: R${deposito:.2f}\n')
          else:
               print("Valor inválido, operação não concluída. Favor digite um valor válido")


     elif escolha == 2:
          if qnt_saques <= 3:
               saque = float(input("Qual valor, em reais, você deseja sacar? R$"))

               excedeu_saldo = saque > saldo
               excedeu_limite = saque > limite_diario

               if excedeu_saldo:
                    print("Você não possui saldo suficiente")
               elif  excedeu_limite:
                    print("O limite de valor por saque é de R$500.00")
               else:
                    saldo -= saque
                    extrato += (f'Saque de: R${saque:.2f}\n')
               qnt_saques += 1
          else:
               print('Quantidade de saques diários excedidos.')

     elif escolha == 3:
          print('====== EXTRATO ====== ')
          print(extrato)
          print(F'Saldo: R${saldo}')
          print('===================== ')

     elif escolha == 0:
          break

     else:
          print("Operação inválida, escolha outra operação")

