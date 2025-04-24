import os

class ProdutoInexistenteError(Exception):
    pass

class SaldoInsuficienteError(Exception):
    pass


dictprod = {
    'Tshirts': 12.50,
    'Casacos': 15.00,
    'Calças': 10.00,
    'Calçado': 20.00
}


carrinho = {}
saldo = 0.0

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    while True:
        print("=" * 40)
        print("    SISTEMA DE GESTÃO DE UMA LOJA    ")
        print("=" * 40)
        print("\n[0] - Sair do Programa")
        print("[1] - Visualizar produtos")
        print("[2] - Carrinho")
        print("[3] - Adicionar Saldo")
        print("[4] - Pagamento")
        print("=" * 40)

        try:
            escolha = int(input("\nEscolha uma opção: "))
        except ValueError:
            print("\nPor favor, introduza um número válido.")
            continue

        match escolha:
            case 0:
                print("A sair do programa...")
                exit()
            case 1:
                verprodutos()
            case 2:
                carrinho()
            case 3:
                adsaldo()
            case 4:
                pagamento()
            case _:
                print("\nOpção inválida! Por favor, escolha uma opção válida.")

def verprodutos():
    limpar()
    print("\nProdutos disponíveis:")
    for produto, preco in dictprod.items():
        print(f"- {produto}: {preco:.2f}€")
    print("\nDigite o nome do produto que deseja adicionar ao carrinho (ou ENTER para voltar).")
    produto = input("Produto: ").strip().title()

    if produto == "":
        return

    try:
        if produto not in dictprod:
            raise ProdutoInexistenteError("Produto não encontrado.")

        quantidade = int(input("Quantidade: "))
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser positiva.")

        carrinho[produto] = carrinho.get(produto, 0) + quantidade
        print(f"{quantidade}x {produto} adicionado(s) ao carrinho.")

    except ProdutoInexistenteError as pie:
        print(f"Erro: {pie}")
    except ValueError as ve:
        print(f"Erro: {ve}")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    finally:
        input("\nPressione ENTER para continuar...")

def carrinho():
    limpar()
    if not carrinho:
        print("Carrinho ainda vazio.")
    else:
        print("Carrinho de compras:")
        total = 0
        for produto, qtd in carrinho.items():
            preco = dictprod[produto]
            subtotal = preco * qtd
            total += subtotal
            print(f"{qtd}x {produto} = {subtotal:.2f}€")
        print(f"\nTotal: {total:.2f}€")
    input("\nPressione ENTER para voltar ao menu...")

def adsaldo():
    global saldo
    limpar()
    try:
        valor = float(input("Digite o valor a adicionar ao saldo: "))
        if valor <= 0:
            raise ValueError("O valor deve ser maior que zero.")
        saldo += valor
        print(f"Saldo atualizado: {saldo:.2f}€")
    except ValueError as ve:
        print(f"Erro: {ve}")
    finally:
        input("\nPressione ENTER para continuar...")

def pagamento():
    global saldo, carrinho
    limpar()
    try:
        if not carrinho:
            raise Exception("Não é possível pagar com o carrinho vazio.")

        total = sum(dictprod[produto] * qtd for produto, qtd in carrinho.items())

        print(f"Total da compra: {total:.2f}€")
        print(f"Saldo disponível: {saldo:.2f}€")

        if saldo < total:
            raise SaldoInsuficienteError("Saldo insuficiente para realizar a compra.")

        confirmar = input("Deseja confirmar o pagamento? (s/n): ").strip().lower()
        if confirmar == 's':
            saldo -= total
            carrinho = {}
            print("Pagamento realizado com sucesso!")
            print(f"Saldo restante: {saldo:.2f}€")
        else:
            print("Pagamento cancelado.")

    except SaldoInsuficienteError as sie:
        print(f"Erro: {sie}")
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        input("\nPressione ENTER para continuar...")


menu()
