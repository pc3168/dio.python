
opcao = int(input("informe a opcao: "))
valor = ""

if opcao == 1:
    valor = " 1 faça alguma coisa"
elif opcao == 2:
    valor = "2 faça outra coisa"
else: 
    valor = "não faz nada"

print(valor)


print("if ternário")
saldo = 8000
saque = 100

status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar o saque!")