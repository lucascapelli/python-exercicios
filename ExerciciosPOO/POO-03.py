'''
Exercício OO nível intermediário:

Crie uma classe ContaBancaria que tenha:

    Atributos:

        titular (nome da pessoa)

        saldo (valor atual da conta, inicialize com 0)

    Métodos:

        depositar(valor) → adiciona o valor ao saldo

        sacar(valor) → subtrai o valor do saldo, se houver saldo suficiente; caso contrário, retorna uma mensagem de saldo insuficiente

        extrato() → retorna uma string com o nome do titular e o saldo atual formatado

'''
class ContaBancaria:
    # Definição da classe ContaBancaria
    def __init__(self, titular: str, saldo: float):
        # Construtor: define os atributos iniciais do objeto
        # 'self' representa o próprio objeto
        self.titular = titular
        self.saldo = saldo

    def depositar(self) -> None:
        # Método para adicionar valor ao saldo
        # Aqui usamos while True + try/except para garantir que
        # o usuário digite um número válido
        while True:
            try:
                deposito = float(input('\ndigite o valor a ser depositado:\n'))
                self.saldo += deposito  # atualiza o saldo do objeto
                break  # sai do laço quando o valor for válido
            except ValueError:
                print('digite apenas números')

    def sacar(self) -> None:
        # Método para retirar valor do saldo
        while True:
            try:
                saque = float(input('\ndigite o valor de saque:\n'))
                if saque > self.saldo:
                    print('\nsaldo insuficiente.\n')
                    continue  # volta pro início do laço
                self.saldo -= saque  # atualiza o saldo
                break
            except ValueError:
                print('\ndigite apenas números\n')

    def extrato(self) -> str:
        # Retorna uma string com o titular e o saldo atual
        return f'\nOlá {self.titular}, seu saldo é de: {self.saldo}$\n'


# Criamos um objeto da classe ContaBancaria
pessoa1 = ContaBancaria('Marcelo', 0)

# Chamamos o método extrato para ver o saldo inicial
print(pessoa1.extrato())

# Chamamos depositar() para adicionar dinheiro
pessoa1.depositar()

# Chamamos sacar() para retirar dinheiro
pessoa1.sacar()

# Chamamos extrato() novamente para ver o saldo final
print(pessoa1.extrato())


# -----------------------------
# Dicas de boas práticas
# -----------------------------
# - Métodos que alteram estado (depositar, sacar) geralmente retornam None
# - Validação de entrada é importante, mesmo que o frontend exista
# - OOP é sobre modelar objetos e suas responsabilidades
# - Ler a documentação oficial ajuda a consolidar o entendimento:
#   https://docs.python.org/3/tutorial/classes.html
