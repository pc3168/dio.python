def sacar(valor: float):
    saldo = 500
    if (saldo >= valor):
        saldo -= valor
        print(saldo)

sacar(100)