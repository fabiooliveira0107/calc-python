# ==============================================================================
# Projeto: Calculadora Simples Desenvolvida em Python
# Descrição: Realiza operações básicas (adição, subtração, multiplicação, divisão)
#            com validação de entrada e menu interativo.
# ==============================================================================


def somar(a, b):
  "Retorna a soma de dois números."
  return a + b


def subtrair(a, b):
  "Retorna a subtração de dois números."
  return a - b


def multiplicar(a, b):
  "Retorna a multiplicação de dois números."
  return a * b


def dividir(a, b):
  "Retorna a divisão de dois números, tratando divisão por zero."
  if b == 0:
    return "Erro: Divisão por zero não é permitida."
  return a / b


def obter_numero(mensagem):
  "Solicita um número ao usuário e valida se a entrada é numérica."
  while True:
    try:
      return float(input(mensagem))
    except ValueError:
      print("Entrada inválida! Por favor, digite apenas números válidos.")


def calculadora():
  "Controla o fluxo principal da calculadora e o menu interativo."
  print("========================================")
  print("      BEM-VINDO À CALCULADORA PYTHON    ")
  print("========================================")

  while True:
    print("\nSelecione a operação desejada:")
    print("1. Adição (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    print("5. Sair")

    opcao = input("\nDigite o número da sua escolha (1-5): ").strip()

    # Condição para encerrar o programa
    if opcao == "5":
      print("\nEncerrando a calculadora. Até logo!")
      break

    # Validação da opção do menu
    if opcao in ("1", "2", "3", "4"):
      num1 = obter_numero("Digite o primeiro número: ")
      num2 = obter_numero("Digite o segundo número: ")

      if opcao == "1":
        resultado = somar(num1, num2)
        print(f"\nResultado: {num1} + {num2} = {resultado}")
      elif opcao == "2":
        resultado = subtrair(num1, num2)
        print(f"\nResultado: {num1} - {num2} = {resultado}")
      elif opcao == "3":
        resultado = multiplicar(num1, num2)
        print(f"\nResultado: {num1} * {num2} = {resultado}")
      elif opcao == "4":
        resultado = dividir(num1, num2)
        print(f"\nResultado: {num1} / {num2} = {resultado}")
    else:
      print(
          "Opção inválida! Escolha um número entre 1 e 5 no menu principal."
      )


# Ponto de entrada do programa
if __name__ == "__main__":
  calculadora()