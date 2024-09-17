menu = """
    [0] Sair
    [1] Depositar
    [2] Sacar
    [3] Extrato

"""
LIMITE_SAQUES = 3
limite = 500
numero_saque = 0
saldo = 0
extrato = ""


def sacar():
    global saldo, extrato, numero_saque, limite, LIMITE_SAQUES

    valor = float(input("Informe o valor do Saque: "))

    saldo_insuficiente = valor > saldo

    saques = numero_saque >= LIMITE_SAQUES

    extourou_limite = valor > limite

    if saldo_insuficiente:
        print("Saldo insuficiente.")
    elif saques:
        print("Ultrapassou o número de saques.")
    elif extourou_limite:
        print("O valor excede o limite.")
    elif valor > 0:
        texto = "Saque: "
        saldo -= valor
        extrato += f"{texto.ljust(10)} R$ {valor:.2f}\n"
        numero_saque += 1
    else:
        print("O valor informado é inválido.")

def depositar():
    global saldo, extrato

    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        texto = "Depósito: "
        saldo += valor
        extrato += f"{texto.ljust(10)} R$ {valor:.2f}\n"
    else:
        print("O valor informado é inválido.")


def visualizar_extrato():
    texto = " Extrato "
    print("\n",texto.center(30, "="))
    print("Não foram realizadas movimentações." if not extrato else extrato)
    texto = "Saldo: "
    print(f"{texto.ljust(10)} R$ {saldo:.2f}\n")
    texto = ""
    print("\n",texto.center(30, "="))


while True:
    print(menu)
    opcao = input(">> ")
    

    if opcao == "0":
        print("Programa Finalizado!")
        break

    elif opcao == "1":
        depositar()

    elif opcao == "3":
        visualizar_extrato()

    elif opcao == "2":
        sacar()

    else:
        print("Opção inválida: Selecina somente os números informados no menu.")


    