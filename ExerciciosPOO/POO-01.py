'''
🎯 Desafio:

✅ Crie uma classe chamada Cachorro.
✅ Ela deve ter:

    atributo nome

    atributo idade
   
     ✅ Deve ter um método apresentar() que imprima:
    "Oi! Eu sou [nome] e tenho [idade] anos caninos."


'''
class Cachorro:
    """Classe que utilizamos para criar instâncias/objetos que irão seguir o mesmo padrão de regras e comportamento"""

    especie: str = "Canis familiaris"  # atributo da classe, diferente de um atributo inicializado em um método __init__
    # atributos de classe são informações guardadas dentro de toda a classe, ou seja, todo objeto/instância dessa classe
    # vai ter este atributo, pois ele foi atribuído primariamente antes de qualquer método que manipule um objeto

    # dentro de uma classe nós temos os métodos
    # o método nada mais é que uma função, porém dentro de uma classe

    # usualmente, dentro de uma classe, antes de qualquer método
    # teremos um método __init__
    # esse método é muito importante pois sua sintaxe nos dá substrato argumentativo para o Python
    # e assim podemos manipular individualmente objetos/instâncias
    def __init__(self, nome: str, idade: int):  # dentro de métodos nós temos parâmetros que podem ser passados neles
        # parâmetros nada mais são do que variáveis utilizadas para armazenar valores nos atributos
        # sendo o 'self' a variável obrigatória utilizada para interagir especificamente com aquele objeto/instância
        # que está sendo referenciado

        # estes são os atributos; os atributos nada mais são que os campos específicos de informação
        # que um objeto/instância pode ter
        # sendo o atributo self o que referencia individualmente o objeto
        self.nome = nome  # esta sintaxe diz que o objeto tem um atributo nome igual ao valor passado no parâmetro nome
        # ou objeto.nome = (valor passado no parâmetro do método)
        self.idade = idade  # o mesmo conceito se aplica para este atributo

    def apresentar(self) -> str:  # neste exemplo temos um método que recebe como parâmetro o próprio objeto para referência
        """Retorna a frase de apresentação do cachorro."""
        return f"Oi! Eu sou {self.nome} e tenho {self.idade} anos caninos."
        # retornamos os valores específicos salvos nos atributos daquele objeto individual

    def aniversario(self) -> None:  # neste método também temos como parâmetro o próprio objeto em si
        """Aumenta a idade em 1 (simula um aniversário)."""
        self.idade += 1  # ele pega o objeto referenciado no parâmetro do método e soma 1 ao seu atributo idade

    def __repr__(self) -> str:  # método que retorna uma string representando o objeto
        """Representação oficial — útil para depuração."""
        return f"Cachorro(nome={self.nome!r}, idade={self.idade})"
        # aqui basicamente pedimos: "deste objeto, traga os atributos nome e idade"

# utilizaremos os conceitos vistos anteriormente

# primeiro criamos um objeto
# como pode ser observado, para criarmos um objeto de uma classe
# basta criar uma variável, dizer que ela pertence a essa classe
# e passar nos parâmetros do método inicializador da classe os valores que queremos salvar nos atributos
dog = Cachorro('pulguento', 12)  # é importante passar os parâmetros na mesma ordem que o método __init__ espera receber

# exemplo no def __init__(self, nome: str, idade: int):
# nesta variável que utiliza a classe, o self recebe o 'dog', pois assim que declaramos dog
# já indicamos que ele é igual à classe Cachorro
# em seguida, passamos nos parâmetros ('pulguento', 12), que seguem a mesma ordem do método

# agora essa variável é da classe Cachorro e possui:
# atributo nome = 'pulguento'
# atributo idade = 12
print(dog)  # saída:

# como essa variável já tem esses valores armazenados,
# se chamarmos outro método da classe que utilize esses atributos,
# ele conseguirá acessá-los normalmente
print(Cachorro.apresentar(dog))  # saída: Oi! Eu sou pulguento e tenho 12 anos caninos.

# outro exemplo:
print(Cachorro.__repr__(dog))  # saída: Cachorro(nome='pulguento', idade=12)

# além de imprimir valores, também podemos manipular o objeto utilizando métodos
Cachorro.aniversario(dog)  # este método soma +1 ao atributo idade do objeto
print(dog)  # ao consultar o objeto após a execução do método, observamos a alteração

# e obviamente não podemos esquecer do nosso atributo de classe
print(dog.especie) # saída:Canis familiaris
# mesmo com tudo que fizémos o atributo de classe espécie não é alterado (pelo o motivo explicado a cima)

# ---------------------------
# Dicas importantes sobre OOP
# ---------------------------

# 1️⃣ Classe vs Instância
# Classe é o "molde" (Cachorro).
# Instância (ou objeto) é o que nasce desse molde (dog = Cachorro(...)).
# Cada instância tem seus próprios atributos de instância (nome, idade),
# mas compartilha os atributos de classe (especie).

# 2️⃣ Atributos de classe vs atributos de instância
# - Atributo de classe: pertence à classe inteira (Cachorro.especie).
# - Atributo de instância: pertence a um objeto específico (self.nome, self.idade).
# Alterar um atributo de instância NÃO altera o atributo de classe.

# 3️⃣ Métodos
# Métodos são funções que pertencem a uma classe.
# O primeiro parâmetro (self) sempre recebe a instância que está chamando o método.
# Quando fazemos dog.apresentar(), o Python faz por baixo:
# Cachorro.apresentar(dog)

# 4️⃣ Por que existe o 'self'?
# 'self' é a referência ao objeto atual.
# Ele permite acessar e modificar os atributos daquela instância específica.
# Sem o self, o método não saberia "de qual cachorro" estamos falando.

# 5️⃣ Type hints (anotações de tipo)
# Exemplo:
# def apresentar(self) -> str:
# O '-> str' indica que este método RETORNA uma string.
# Isso NÃO muda o comportamento do Python em tempo de execução,
# mas ajuda:
# - quem está lendo o código
# - ferramentas de análise (linters, IDEs)
# - documentação automática
# - evitar erros lógicos

# Outro exemplo:
# def aniversario(self) -> None:
# '-> None' indica que o método NÃO retorna valor nenhum.
# Ele apenas executa uma ação (efeito colateral),
# no caso, alterar o estado interno do objeto (self.idade).

# Regra prática:
# - Métodos que PRODUZEM um valor → usam return → geralmente -> str, -> int, etc.
# - Métodos que SÓ ALTERAM estado → não retornam nada → -> None

# 6️⃣ __repr__
# __repr__ define como o objeto aparece quando é impresso ou inspecionado.
# Ele é muito usado para:
# - debug
# - logs
# - inspeção rápida de estado do objeto
# Boas práticas: retornar algo que mostre claramente os atributos principais.

# 7️⃣ Encapsulamento (conceito-chave de OOP)
# Os dados (atributos) e os comportamentos (métodos)
# estão agrupados dentro da mesma estrutura (a classe).
# Isso deixa o código:
# - mais organizado
# - mais reutilizável
# - mais fácil de manter e evoluir

# 8️⃣ Leitura obrigatória (OOP em Python)
# Documentação oficial sobre classes:
# https://docs.python.org/3/tutorial/classes.html
# Não existe dev bom que não leia documentação, jovem gafanhoto ;)
# Ler a documentação NÃO é opcional para quem quer dominar OOP de verdade.


