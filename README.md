# **Sobre o Projeto**
Esse projeto foi desenvolvido como parte de um desafio proposto pelo Bootcamp **Ciência de dados com Python**, no módulo de introdução do Python. Esse bootcamp faz parte da plataforma **DIO (Digital Innovation One)** em parceria com o iFood.

# **Enunciado do projeto**
## Parte 1
Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python. Para a primeira versão do sistema devemos implementar apenas 3 operações:  
* **Depósito:** Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.  
* **Saque:** O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.
* **Extrato:** Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações.
Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo:  
1500.45 = R$ 1500.45  

## Parte 2
Precisamos otimizar o nosso sistema, criando duas novas funções:  
* **Criar usuário (cliente):** Um usuário é composto por nome, data de nascimento, cpf e endereço. Deve ser armazenado somente os números do CPF e não podemos cadastrar dois usuários com o mesmo CPF;  
* **Criar conta corrente:** O programa deve armazenar contas em uma lista, onde uma conta é composta por: agência, número da conta e usuário. O número da conta é sequencial, iniciando em 1. O número da agência é fixo: "0001". Uma conta pertence a somente um usuário. **DICA:** Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF informado para cada usuário da lista.

# **Status do Projeto**  
🚧🚧 **Em Desenvolvimento** 🚧🚧  
Esse desafio passará por evoluções de acordo com o progresso do Bootcamp. No momento, para usar o projeto, basta rodar o arquivo _main.py_.

# Agradecimentos
Agradecimentos à DIO e ao iFood por disponibilizar o bootcamp de forma gratuita e ao [Guilherme Arthur de Carvalho](https://www.linkedin.com/in/decarvalhogui/?originalSubdomain=br) por ter criado o desafio.