from math import sqrt
from time import sleep


def verifiy_position():
    p = int(input("Enter the position of the triangular number you want to check: "))
    s = (p * (p + 1)) / 2
    print(f"The triangular number in position {p} is {s:.0f}.")


def verify_if_triangular():
    num = int(input("Enter a number to check if it is triangular: "))
    T = num * (-2)
    n = (-1 + sqrt(1 ** 2 - 4 * 1 * T)) / 2

    if n % 1 == 0:
        print(f"{num} is a triangular number and is in position {n:.0f}")
    else:
        print(f"{num} is not a triangular number!")


while True:

    print()
    print("""What do you want to do?

            1 - Check which triangular number is in a given position
            2 - Check if a number is triangular
            3 - Exit the program""")
    print()

    escolha = str(input("Option: ")).strip()

    if escolha == "1":
        verifiy_position()
        sleep(2)

    elif escolha == "2":
        verify_if_triangular()
        sleep(2)

    elif escolha == "3":
        print("Leaving the program... Goodbye!")
        sleep(1)
        break

    else:
        print("Invalid option. Please check that you typed it correctly.")
        sleep(2)
