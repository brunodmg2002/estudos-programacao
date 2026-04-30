def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b


def obter_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada inválida. Digite um número.")


def menu():
    print("\n=== Calculadora ===")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")


def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Encerrando...")
            break

        if opcao in ["1", "2", "3", "4"]:
            a = obter_numero("Digite o primeiro número: ")
            b = obter_numero("Digite o segundo número: ")

            if opcao == "1":
                resultado = soma(a, b)
            elif opcao == "2":
                resultado = subtracao(a, b)
            elif opcao == "3":
                resultado = multiplicacao(a, b)
            elif opcao == "4":
                resultado = divisao(a, b)

            print(f"Resultado: {resultado}")
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()