menu = """
    ==================== MENU ====================
    [d] Depósito
    [s] Saque
    [e] Extrato
    [q] Sair
    ==============================================
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    print(menu)
    opcao = input("Escolha uma opção: ").lower()

    if opcao == "d":
        valor = float(input("\nInsira o valor que será depositado: R$ "))

        if valor >= 1:
            saldo += valor
            extrato += f"Depósito de R${valor:.2f}\n"
            print(f"\n✅ Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("\n⚠️ Valor inválido, tente novamente.")

    elif opcao == "s":
        valor = float(input("\nInsira o valor do saque: R$ "))
        exedeu_saldo = valor > saldo
        exedeu_limite = valor > limite
        exedeu_saques = numero_saques >= LIMITE_SAQUES

        if exedeu_saldo:
            print("\n⚠️ Operação falhou. Saldo insuficiente.")
        elif exedeu_limite:
            print("\n⚠️ Operação falhou. Valor do saque supera o limite.")
        elif exedeu_saques:
            print("\n⚠️ Operação falhou. Limite diário de saques atingido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque de R${valor:.2f}\n"
            numero_saques += 1
            print(f"\n✅ Saque de R${valor:.2f} realizado com sucesso!")
        else:
            print("\n⚠️ Operação falhou. Valor inserido é inválido.")

    elif opcao == "e":
        print("\n********** EXTRATO **********")
        if not extrato:
            print("🚫 Não foram registradas movimentações.")
        else:
            print(extrato)
        print(f"\nSaldo atual: R${saldo:.2f}")
        print("*****************************\n")

    elif opcao == "q":
        print("\n👋 Saindo do sistema. Até logo!")
        break
    else:
        print("\n❌ Opção inválida, tente novamente.")
