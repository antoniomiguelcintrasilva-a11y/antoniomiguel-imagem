from math import isqrt


def is_prime(number: int) -> bool:
    """Retorna True se o número for primo."""
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    max_divisor = isqrt(number)
    for divisor in range(3, max_divisor + 1, 2):
        if number % divisor == 0:
            return False

    return True


def run_tests() -> None:
    try:
        number = int(input("Digite um número inteiro: "))
        result = is_prime(number)
        if result:
            print(f"O número {number} é primo!")
        else:
            print(f"O número {number} não é primo.")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")


if __name__ == "__main__":
    run_tests()