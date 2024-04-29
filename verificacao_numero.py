from math import sqrt
from time import sleep


def verificar_posicao():
    p = int(input("Digite a posição do número triangular que você quer verificar: "))
    s = (p * (p + 1)) / 2
    print(f"O número triangular na posição {p} é {s:.0f}.")


def verificar_numero_triangular():
    num = int(input("Digite um número para verificar se é triangular: "))
    T = num * (-2)
    n = (-1 + sqrt(1 ** 2 - 4 * 1 * T)) / 2

    if n % 1 == 0:
        print(f"{num} é um número triangular e está na posição {n:.0f}")
    else:
        print(f"{num} não é um número triangular!")


while True:

    print()
    print("""O que você quer fazer? 
    
        1 - Verificar qual o número triangular numa determinada posição
        2 - Verificar se um número é triangular
        3 - Sair do programa""")
    print()

    escolha = str(input("Opção: ")).strip()

    if escolha == "1":
        verificar_posicao()
        sleep(2)

    elif escolha == "2":
        verificar_numero_triangular()
        sleep(2)

    elif escolha == "3":
        print("Saindo do programa... Adeus")
        sleep(1)
        break

    else:
        print("Opção inválida. Verifique se você digitou corretamente.")
        sleep(2)
