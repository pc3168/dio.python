print("estrutura de repetição")
print("for")
print("----------------------------------------")

palavra = "paulo"
VOGAIS = "AEIOU"

for letra in palavra:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()
    print("fim")

for numero in range(0, 10,2):
    print(numero, end=" ")
print("\n")

for numero in range(10):
    print(numero, end=" ")
print("\n")

for numero in range(0,10,5):
    print(numero, end=" ")
print("\n")

print("----------------------------------------")
print("While")

opcao = -1

while opcao != 0:
    opcao = int(input("digite um número diferente de zero"))
    if opcao == 0:
        print("saiu do sistema")
    else:
        print("continua")

print("----------------------------------------")