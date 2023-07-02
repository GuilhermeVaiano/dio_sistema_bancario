import random

class Extrato:
    def __init__(self):
        self.transacoes = []

    def add_transacao(self, tipo, valor):
        transacao = {
            'tipo': tipo,
            'valor': valor
        }
        self.transacoes.append(transacao)

        
class Conta:
    numero_conta = 0
    lista_de_contas = []

    def __init__(self, usuario):
        Conta.numero_conta += 1
        self.id = Conta.numero_conta
        self.usuario = usuario
        self.agencia = Conta.set_agencia()
        self.saldo = 0
        self.qtd_saques = 3
        self.extrato = Extrato()
        Conta.lista_de_contas.append(self)

##################### GETTERS AND SETTERS #############################
    def set_agencia():
        agencia = str(random.radint(1,9999))
        if len(agencia) < 4:
            agencia = agencia.zfill(4)
        return agencia

    def get_lista_de_contas():
        return Conta.lista_de_contas
    
    def get_contas_por_cpf(cpf):
        contas_encontradas = []
        for conta in Conta.lista_de_contas:
            if conta.usuario.cpf == cpf:
                contas_encontradas.append(conta)
        
        return contas_encontradas

############################## METODOS ################################

    def exibe_saldo(self):
        print(f"Saldo disponível: R$ {self.saldo:.2f}")
    
    def sacar(self):
        if self.qtd_saques == 0:
            print("Limite de saques diários atingido. Não é possível sacar")
            return
        
        valor = float(input("Digite o valor que deseja sacar (limite de R$ 500,00 por saque): "))
        while (valor < 0) or (valor > 500):
            print("Valor inválido de saque! Por favor, digite um valor válido! (limite de R$ 500,00 por saque)")
            valor = (float(input()))

        if valor > self.saldo:
            print("Saldo indisponível.")
        else:
            self.saldo -= valor
            self.qtd_saques -= 1
            self.extrato.add_transacao("Saque", valor)
            print("Valor retirado com sucesso.")

        self.exibe_saldo()
        return

    def depositar(self):
        valor = float(input("Digite o valor que deseja depositar: "))
        while valor <= 0:
            valor = float(input("Valor invalido! Por favor, digite um valor positivo de deposito: "))

        self.saldo += valor
        self.exibe_saldo
        self.extrato.add_transacao("Depósito", valor)
        print("Valor depositado com sucesso.")
    
    def exibe_extrato(self):
        print("Transações dessa conta (hoje):")
        for transacao in self.extrato.transacoes:
            tipo = transacao['tipo']
            valor = transacao['valor']
            print(f"Tipo: {tipo}, Valor: R${valor:.2f}")

    