from Conta import Conta
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


print("Bem-vindo! Crie a sua conta:")
nome = str(input("Digite seu nome: "))
valor_inicial = int(input("Saldo inicial da conta: "))
conta = Conta(nome,valor_inicial)

while(True):
    acao = exibir_menu()
    if acao == 1: conta.exibe_extrato()
    elif acao == 2: conta.depositar()
    elif acao == 3: conta.sacar()
    elif acao == 4: break
    else: print("Acao inválida!")

    time.sleep(2)

print("Obrigado por contar com os nossos serviços. Tenha um bom dia!")