# Classe Livro
class Livro:
    def __init__(self, titulo, autor, ano_publicacao, num_copias):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.num_copias = num_copias

    def emprestar(self):
        if self.num_copias > 0:
            self.num_copias -= 1
            print(f"O livro '{self.titulo}' foi emprestado com sucesso.")
        else:
            print("Desculpe, este livro não está disponível no momento.")

    def devolver(self):
        self.num_copias += 1
        print(f"O livro '{self.titulo}' foi devolvido com sucesso.")

#Classe Usuário
class Usuario:
    def __init__(self, nome, identificacao, contato):
        self.nome = nome
        self.identificacao = identificacao
        self.contato = contato

    def __str__(self):
        return f"Nome: {self.nome}, Identificação: {self.identificacao}, Contato: {self.contato}"

# Classe biblioteca com todas as funções
class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []
        self.livros_emprestados = []

    # Cadastro de livros
    def cadastrar_livro(self, livro):
        self.livros.append(livro)
        print(f"O livro '{livro.titulo}' foi cadastrado com sucesso.")
        
    # Cadastro de usuários
    def cadastrar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"O usuário '{usuario.nome}' foi cadastrado com sucesso.")
        
    # Buscar livro por título
    def buscar_livro_por_titulo(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                return livro
        return None

    # função pegar livro emprestado
    def pegar_livro_emprestado(self, titulo_livro, nome_usuario):
        livro_encontrado = self.buscar_livro_por_titulo(titulo_livro)
        if livro_encontrado:
            usuario_encontrado = None
            for usuario in self.usuarios:
                if usuario.nome == nome_usuario:
                    usuario_encontrado = usuario
                    break

            if usuario_encontrado:
                if livro_encontrado.num_copias > 0:
                    livro_encontrado.num_copias -= 1
                    print(f"O livro '{livro_encontrado.titulo}' foi pego emprestado por '{nome_usuario}'.")
                    self.livros_emprestados.append((livro_encontrado, nome_usuario))
                else:
                    print("Desculpe, este livro não está disponível no momento.")
            else:
                cadastrar_novo_usuario = input(f"O usuário '{nome_usuario}' não está cadastrado. Deseja cadastrá-lo agora? (s/n): ")
                if cadastrar_novo_usuario.lower() == 's':
                    identificacao = input("Digite o número de identificação do usuário: ")
                    contato = input("Digite o contato do usuário: ")
                    novo_usuario = Usuario(nome_usuario, identificacao, contato)
                    self.cadastrar_usuario(novo_usuario)
                    self.pegar_livro_emprestado(titulo_livro, nome_usuario)
                else:
                    print("Operação cancelada.")
        else:
            print("Livro não encontrado.")

    # função devolver livro emprestado
    def devolver_livro(self, titulo_livro):
        livro_encontrado = self.buscar_livro_por_titulo(titulo_livro)
        if livro_encontrado:
            livro_emprestado = None
            for livro, usuario in self.livros_emprestados:
                if livro.titulo == titulo_livro:
                    livro_emprestado = livro
                    usuario_emprestou = usuario
                    break

            if livro_emprestado:
                nome_usuario = input(f"Digite o nome do usuário que pegou emprestado o livro '{titulo_livro}': ")
                if nome_usuario == usuario_emprestou:
                    livro_encontrado.devolver()
                    self.remover_livro_emprestado(titulo_livro)
                else:
                    print("Este livro foi emprestado por outro usuário.")
            else:
                print("Este livro não está emprestado no momento.")
        else:
            print("Livro não encontrado.")

    # função consultar livros
    def consultar_livros(self, termo):
        livros_encontrados = []
        for livro in self.livros:
            if termo.lower() in livro.titulo.lower() or termo.lower() in livro.autor.lower():
                livros_encontrados.append(livro)

        if livros_encontrados:
            print("Livros encontrados:")
            for livro in livros_encontrados:
                print(f"Título: {livro.titulo}, Autor: {livro.autor}, Ano de Publicação: {livro.ano_publicacao}, Cópias Disponíveis: {livro.num_copias}")
        else:
            print("Nenhum livro encontrado.")

    # função gerar relatório
    def gerar_relatorio(self):
        print("\nRelatório de Livros Disponíveis:")
        if self.livros:
            for livro in self.livros:
                print(f"Título: {livro.titulo}, Autor: {livro.autor}, Ano de Publicação: {livro.ano_publicacao}, Cópias Disponíveis: {livro.num_copias}")
        else:
            print("Não há livros disponíveis.")

        print("\nRelatório de Livros Emprestados:")
        if self.livros_emprestados:
            for livro_emprestado, usuario in self.livros_emprestados:
                print(f"Título: {livro_emprestado.titulo}, Autor: {livro_emprestado.autor}, Ano de Publicação: {livro_emprestado.ano_publicacao}, Nome do Usuário: {usuario}")
        else:
            print("Não há livros emprestados no momento.")

        print("\nRelatório de Usuários Cadastrados:")
        if self.usuarios:
            for usuario in self.usuarios:
                print(f"Nome: {usuario.nome}, Identificação: {usuario.identificacao}, Contato: {usuario.contato}")
        else:
            print("Não há usuários cadastrados.")

    # função buscar livros
    def consultar_livros(self, termo):
        livros_encontrados = []

        for livro in self.livros:
            if termo.lower() in livro.titulo.lower() or termo.lower() in livro.autor.lower() or termo.lower() == str(livro.ano_publicacao):
                livros_encontrados.append(livro)

        if livros_encontrados:
            print("Livros encontrados:")
            for livro in livros_encontrados:
                print(f"Título: {livro.titulo}, Autor: {livro.autor}, Ano de Publicação: {livro.ano_publicacao}, Cópias Disponíveis: {livro.num_copias}")
        else:
            print("Nenhum livro encontrado.")
    
    # função de remover livro emprestado
    def remover_livro_emprestado(self, titulo_livro):
        for i, (livro, _) in enumerate(self.livros_emprestados):
            if livro.titulo == titulo_livro:
                del self.livros_emprestados[i]
                break

# Menu de interação com o usuário
def exibir_menu():
    print("\n=== MENU ===")
    print("1. Cadastrar Livro")
    print("2. Cadastrar Usuário")
    print("3. Pegar Livro Emprestado")
    print("4. Devolver Livro")
    print("5. Consultar Livros")
    print("6. Gerar Relatório")
    print("0. Sair")

def main():
    biblioteca = Biblioteca()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            ano = input("Digite o ano de publicação do livro: ")
            num_copias = input("Digite o número de cópias disponíveis: ")
            livro = Livro(titulo, autor, int(ano), int(num_copias))
            biblioteca.cadastrar_livro(livro)
        elif opcao == "2":
            nome = input("Digite o nome do usuário: ")
            identificacao = input("Digite o número de identificação do usuário: ")
            contato = input("Digite o contato do usuário: ")
            usuario = Usuario(nome, identificacao, contato)
            biblioteca.cadastrar_usuario(usuario)
        elif opcao == "3":
            titulo_livro = input("Digite o título do livro a ser pego emprestado: ")
            nome_usuario = input("Digite o nome do usuário que está pegando emprestado o livro: ")
            biblioteca.pegar_livro_emprestado(titulo_livro, nome_usuario)
        elif opcao == "4":
            titulo_livro = input("Digite o título do livro a ser devolvido: ")
            biblioteca.devolver_livro(titulo_livro)
        elif opcao == "5":
            termo = input("Digite o título ou autor do livro a ser consultado: ")
            biblioteca.consultar_livros(termo)
        elif opcao == "6":
            biblioteca.gerar_relatorio()
        elif opcao == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

"""
# Criando uma instância da biblioteca
biblioteca = Biblioteca()

# Cadastrando alguns livros e um usuário
livro1 = Livro("Python Programming", "John Doe", 2020, 5)
livro2 = Livro("Data Science Handbook", "Jane Smith", 2018, 3)
usuario1 = Usuario("João", "123456", "joao@email.com")

biblioteca.cadastrar_livro(livro1)
biblioteca.cadastrar_livro(livro2)
biblioteca.cadastrar_usuario(usuario1)

# Pegando um livro emprestado e devolvendo-o em seguida
biblioteca.pegar_livro_emprestado("Python Programming", "João")
biblioteca.devolver_livro("Python Programming")

# Consultando livros pelo título
biblioteca.consultar_livros("Python")

# Gerando relatório
biblioteca.gerar_relatorio()
"""