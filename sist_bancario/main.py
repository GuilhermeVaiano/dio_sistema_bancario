from Conta import Conta
from Usuario import Usuario
import time


def exibir_menu():
    while(True):
        print(""" O que deseja fazer?
            (1) Consultar extrato
            (2) Depositar
            (3) Sacar
            (4) Sair
        """)
        acao = int(input())
        if (acao > 0) and (acao <= 4): return acao
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
    cidade = str(input("Digite o nome do seu endereco: "))

    endereco = {"logradouro": logradouro, "numero": num, "bairro": bairro, "cidade":cidade}
    return endereco
                        
def main():
    print("Bem-vindo! Crie a sua conta:")
    nome = str(input("Digite seu nome: "))
    cpf = valida_cpf()
    endereco = cadastrar_endereco()
    dt_nasc = str(input("Digite sua data de nascimento (formato xx/xx/xxxx): "))
    usuario = Usuario(nome, dt_nasc, cpf, endereco)
    conta = Conta(usuario)

    while(True):
        acao = exibir_menu()
        if acao == 1: conta.exibe_extrato()
        elif acao == 2: conta.depositar()
        elif acao == 3: conta.sacar()
        elif acao == 4: break
        else: print("Acao inválida!")

        time.sleep(2)

    print("Obrigado por contar com os nossos serviços. Tenha um bom dia!")

if __name__ == "__main__":
    main()