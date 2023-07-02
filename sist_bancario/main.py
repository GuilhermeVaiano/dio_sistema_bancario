from Conta import Conta
from Usuario import Usuario
import time


def exibir_menu():
    while(True):
        print(""" O que deseja fazer?
            (1) Consultar extrato
            (2) Depositar
            (3) Sacar
            (4) Exibir saldo
            (5) Sair
        """)
        acao = int(input())
        if (acao > 0) and (acao <= 5): return acao
        print("Comando inválido! Por favor, digite um numero correspondente a uma dos comandos válidos")

def valida_cpf():
    while True:
        entrada = str(input("Digite seu CPF (apenas números): "))
        if (len(entrada) != 11) or entrada.isdigit() == False:
            print("Entrada inválida! Por favor, digite um CPF válido (apenas números)")
            continue
        return entrada

def cadastrar_endereco():
    logradouro = str(input("Digite o nome do seu endereço: "))
    num = int(input("Digite o numero do seu endereço: "))
    bairro = str(input("Digite o nome do seu bairro: "))
    cidade = str(input("Digite o nome do sua cidade: "))

    endereco = {"logradouro": logradouro, "numero": num, "bairro": bairro, "cidade":cidade}
    return endereco


def criar_conta():
    nome = str(input("Digite seu nome: "))
    cpf = valida_cpf()
    endereco = cadastrar_endereco()
    dt_nasc = str(input("Digite sua data de nascimento (formato xx/xx/xxxx): "))
    usuario = Usuario(nome, dt_nasc, cpf, endereco)
    conta = Conta(usuario) 
    return conta  

def acessar_conta():
    cpf = str(input("Digite seu CPF: "))
    contas = Conta.get_contas_por_cpf(cpf)

    if len(contas) == 1:
        print("Conta encontrada, redirecionando ao menu principal.")
        return contas[0]
    
    elif len(contas) > 1:
        print("Mais de uma conta foi encontrada. Por favor, selecione uma de acordo com a agência: ")
        for conta in contas:
            print(f"Id da conta: {conta.id}, agência: {conta.agencia}")

        while True:
            num_agencia = str(input("Selecione a conta desejada: "))
            for conta in contas:
                if conta.agencia == num_agencia:
                    print("Acessando a conta selecionada...")
                    time.sleep(2)
                    return conta
                
            print("Agência inválida! Por favor, selecione um número de agência correspondente à conta desejada.")
    
    else:
        print("Conta não encontrada, redirecionando ao menu do inicio.")    

    return None


def consultar_conta(conta):
    while(True):
        acao = exibir_menu()
        if   acao == 1: conta.exibe_extrato()
        elif acao == 2: conta.depositar()
        elif acao == 3: conta.sacar()
        elif acao == 4: conta.exibe_saldo()
        elif acao == 5:
            print("Retornando ao menu inicial")
            break
        else: print("Acao inválida!")

        time.sleep(2)

def main():
    conta = None
    tentativas = 0
    while tentativas < 3:
        print("""Bem-vindo! O que deseja fazer?:
                (1) Criar conta
                (2) Acessar conta
                (3) Sair
        """)
        cmd = int(input())
        if cmd == 1:
            conta = criar_conta()

        elif cmd == 2:
            conta = acessar_conta()
            if conta is not None:
                consultar_conta(conta)
            else:
                tentativas += 1
                continue

        elif cmd == 3: break

        else:
            print("Comando inválido! Por favor, selecione um dos comandos existentes.")
            tentativas += 1
        
    if tentativas == 3: print("Limite de tentativas ultrapassado (3). Encerrando sessão.")

    print("Obrigado por contar com os nossos serviços. Tenha um bom dia!")

if __name__ == "__main__":
    main()