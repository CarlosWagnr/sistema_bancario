# Menu de opções
menu = """
####### Olá! Seja Bem Vindo(a) ao Holt Bank #######
Por gentileza, selecione a opção desejada:
    [1] - Depositar
    [2] - Sacar
    [3] - Extrato
    [4] - Sair
=> """

# Criação das variáveis das operações
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# Criação do ciclo de operações
while True:
    opcao = int(input(menu))

    # Operação de depósito
    if opcao == 1:
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação Falhou! O valor informado é inválido!")

    # Operação de Saque
    elif opcao == 2:
        valor = float(input("Informe o valor do saque: "))

        excedeu_sado = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_sado:
            print("Operação Falhou! Você não tem saldo suficiente!")

        elif excedeu_limite:
            print("Operação Falhou! O valor do saque excede o limite!")

        elif excedeu_saques:
            print("Operação Falhou! Número máximo de saques excedido!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação Falhou! O valor informado é inválido!")

    # Operação de Exibição de Extrato
    elif opcao == 3:
        print("\n************** EXTRATO **************")
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("\n*************************************")

    # Operação Sair 
    elif opcao == 4:
        break

    else:
        print("Operação Inválida! Por favor selecione novamente a operação desejada.")
