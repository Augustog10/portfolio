usuarios = []

# ---------------- VALIDAÇÕES ---------------- #

def validar_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "").strip()

    if not cpf.isdigit() or len(cpf) != 11:
        return False

    if cpf == cpf[0] * 11:
        return False

    # 1º dígito
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    dig1 = (soma * 10 % 11) % 10

    # 2º dígito
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    dig2 = (soma * 10 % 11) % 10

    return dig1 == int(cpf[9]) and dig2 == int(cpf[10])


def validar_telefone(tel):
    tel = tel.replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
    return tel.isdigit() and (10 <= len(tel) <= 11)


def sem_espacos(texto):
    return " " not in texto.strip()


# ---------------- CADASTRO ---------------- #

def cadastrar():
    print("\n--- CADASTRO DE USUÁRIO ---")

    nome = input("Nome: ").strip()

    while True:
        cpf = input("CPF (somente números): ")
        if validar_cpf(cpf) and sem_espacos(cpf):
            break
        print("❌ CPF inválido!")

    while True:
        telefone = input("Telefone: ")
        if validar_telefone(telefone):
            break
        print("❌ Telefone inválido!")

    endereco = input("Endereço: ").strip()
    numero = input("Número: ").strip()
    escolaridade = input("Escolaridade: ").strip()

    usuarios.append({
        "nome": nome,
        "cpf": cpf,
        "telefone": telefone,
        "endereco": endereco,
        "numero": numero,
        "escolaridade": escolaridade
    })

    print("✅ Usuário cadastrado com sucesso!")


# ---------------- LISTAR ---------------- #

def listar():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return

    print("\n--- LISTA DE USUÁRIOS ---")
    for i, u in enumerate(usuarios, 1):
        print(f"""
{i}. Nome: {u['nome']}
   CPF: {u['cpf']}
   Telefone: {u['telefone']}
   Endereço: {u['endereco']}, Nº {u['numero']}
   Escolaridade: {u['escolaridade']}
        """)


# ---------------- BUSCAR ---------------- #

def buscar():
    cpf = input("Digite o CPF para buscar: ")

    for u in usuarios:
        if u["cpf"] == cpf:
            print(f"\nEncontrado: {u['nome']}")
            return

    print("❌ Usuário não encontrado!")


# ---------------- REMOVER ---------------- #

def remover():
    cpf = input("Digite o CPF para remover: ")

    for u in usuarios:
        if u["cpf"] == cpf:
            usuarios.remove(u)
            print("✅ Usuário removido!")
            return

    print("❌ Usuário não encontrado!")


# ---------------- MENU ---------------- #

def menu():
    while True:
        print("""
1 - Cadastrar
2 - Listar
3 - Buscar por CPF
4 - Remover
5 - Sair
        """)

        op = input("Escolha: ")

        if op == "1":
            cadastrar()
        elif op == "2":
            listar()
        elif op == "3":
            buscar()
        elif op == "4":
            remover()
        elif op == "5":
            print("Saindo...")
            break
        else:
            print("❌ Opção inválida!")


# EXECUTAR
menu()