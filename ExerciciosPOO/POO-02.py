'''
Exercício:

Crie uma classe Pessoa que:

    Receba no construtor (__init__) o nome e a idade da pessoa.

    Tenha um método chamado falar que retorne a frase:
    "Olá, meu nome é [nome] e eu tenho [idade] anos."

Depois, crie um objeto da classe Pessoa com nome e idade, e chame o método falar para imprimir a frase.

'''
class Pessoa:  # Primeiro definimos uma classe (por convenção, classes começam com letra maiúscula)
    def __init__(self, nome: str, idade: int):  # Definimos os parâmetros que o método inicializador recebe
        # 'self' representa o próprio objeto que está sendo criado/manipulado
        # Os atributos abaixo recebem os valores vindos dos parâmetros
        self.idade = idade
        self.nome = nome

    def falar(self):  # Definimos um método que espera receber um objeto dessa classe
        return f'Olá, meu nome é {self.nome} e eu tenho {self.idade} anos'
        # O método retorna uma string usando os valores armazenados nos atributos do objeto


# Aqui a variável recebe a classe Pessoa, OBS sempre passar os valores
# na mesma ordem dos parâmetros da classe inicializadora
p1 = Pessoa('joãozinho', 8)

print(Pessoa.falar(p1))  # Forma explícita de chamar o método

print(p1.falar())
# Forma mais simples/fácil: chamamos o método diretamente a partir do objeto


# Type hints (anotações de tipo)
# Exemplo:
# def apresentar(self) -> str:
# O '-> str' indica que este método RETORNA uma string.
# Isso NÃO muda o comportamento do Python em tempo de execução,
# mas ajuda:
# - quem está lendo o código
# - ferramentas de análise (linters, IDEs)
# - documentação automática
# - evitar erros lógicos


# Leitura obrigatória (OOP em Python)
# Documentação oficial sobre classes:
# https://docs.python.org/3/tutorial/classes.html
# Não existe dev bom que não leia documentação, jovem gafanhoto ;)
# Ler a documentação NÃO é opcional para quem quer dominar OOP de verdade.
