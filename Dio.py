menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [s] Sair
    
    => """

saldo = 0
limite = 500
extrato = ""
numeros_saques = 0
LIMITES_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor que deseja depositar: "))
        if valor > 0:
            valor += saldo
            extrato += valor(f"Depósito: R$ {valor: .2f}")
        else:
            print("Vallor Informado não pode ser depositado, tente novamente")
    elif opcao == "s":
        valor = float(input("Qual Valor Deseja Sacar: "))
        excedeu_saldo = valor > saldo
        excedeu_limites = valor > limite
        excedeu_saques = numeros_saques >= LIMITES_SAQUES
        if excedeu_saldo:
            print("Voce não possui Saldo suficiente")
        elif excedeu_limites:
            print("Valor não permitido Tente Outro Valor")
        elif excedeu_saques:
            print("Você excedeu o numero maximo de saque tente outro dia.")
        elif valor > 0:
            saldo -= valor
            extrato += valor(f"Saque R$ {valor:.2f}")
        else:
            print("Valor informado invalido")
        print("Saque Efetuado com sucesso.")
    elif opcao == "e":
        print("\n=============== EXTRATO=============")
        print("não foi realizada movimentação." if not extrato else extrato)
        print(f"\nsaldo: R$ {saldo: .2f}")
        print("Extrato")
    elif opcao == "s":
        break
    else:
        print("Operação Selecionado invalido")
