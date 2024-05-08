
menu = f"""

      [D] Depositar
      [S] Sacar
      [E] Extrato
      [Q] Sair


      """

saldo = 0 
limite = 500
extrato = ""

numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "D":
        
         valor = float(input("Informe o valor do Depósito : "))
         print(f"Seu novo saldo é : {valor}")

         if valor > 0:
             saldo += valor
             extrato += f"Depósito : R$ {valor:.2f}\n"

         else:
             print("Valor inválido.")

    elif opcao == "S":

         valor = float(input("Informe o valor do Saque : "))

         excedeu_saldo = valor > saldo
         excedeu_limite = valor > limite
         excedeu_saques = numero_saques >= LIMITE_SAQUES
         
         

         if excedeu_saldo:
            print("Saldo insuficiente!!")

         elif excedeu_limite:
            print("Valor do saque excede o limite.")
        
         elif excedeu_saques:
            print("Número máximo de saques excedido.")

         elif valor > 0:
             saldo -= valor
             extrato += f"Saque : R$ {valor:.2f}\n"
             numero_saques += 1

         else:
             print("Valor informado inválido.")
            


    elif opcao == "E":
        print("\n  Extrato  ")
        print("Não foram realizadas movimentações." if not  extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        
    elif opcao == "Q":
        break

else:
    print("Operação inválida, por favor selecione novamente a operação desejado.") 

  