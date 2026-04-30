"""Calculadora simples de terminal em Python.

Execute este arquivo para iniciar uma calculadora interativa
com operações básicas: soma, subtração, multiplicação e divisão.
"""


def somar(a: float, b: float) -> float:
    return a + b


def subtrair(a: float, b: float) -> float:
    return a - b


def multiplicar(a: float, b: float) -> float:
    return a * b


def dividir(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Não é possível dividir por zero.")
    return a / b


def obter_numero(mensagem: str) -> float:
    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        try:
            return float(entrada)
        except ValueError:
            print("Entrada inválida. Digite um número válido.")


def exibir_menu() -> None:
    print("\n=== Calculadora em Python ===")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")


def main() -> None:
    operacoes = {
        "1": ("Soma", somar),
        "2": ("Subtração", subtrair),
        "3": ("Multiplicação", multiplicar),
        "4": ("Divisão", dividir),
    }

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            print("Até mais!")
            break

        if opcao not in operacoes:
            print("Opção inválida. Tente novamente.")
            continue

        nome_operacao, funcao = operacoes[opcao]
        print(f"\nVocê escolheu: {nome_operacao}")

        n1 = obter_numero("Digite o primeiro número: ")
        n2 = obter_numero("Digite o segundo número: ")

        try:
            resultado = funcao(n1, n2)
            print(f"Resultado: {resultado}")
        except ZeroDivisionError as erro:
            print(erro)


if __name__ == "__main__":
    main()
