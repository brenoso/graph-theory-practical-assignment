from Instancia import Instancia
import os

# ---------------------- Definição dos Menus ---------------------- #
def print_menu_arquivo():
    print ("\nDigite o nome do arquivo a ser lido:")

def print_menu_estrutura_dados():
    print (67 * "-")
    print ("Escolha uma Estrutura de Dados para representar o grafo")
    print ("1. M.A.")
    print ("2. M.I.")
    print ("3. L.A.")
    print ("4. Sair\n")

def print_menu_geral():
    print (67 * "-")
    print ("\nSelecione a operacao para executar no grafo:")
    print("1. Imprimir")
    print ("2. ehVizinho")
    print ("3. obtemVizinho")
    print ("10. Sair\n")

# Variáveis auxiliares para os menus
sair = False
loop = False

# ---------------------- Menu de leitura do arquivo ---------------------- #

loop=True      
  
while loop:
    print_menu_arquivo()
    arquivo = input()
    path = None

    # Navega pela pasta a procura do arquivo
    for root, dirs, files in os.walk("../instances"):
        for file in files:
            if arquivo in file:
                print("\nArquivo encontrado!")
                path = os.path.join(root, file)
                print("Caminho: " + path +"\n")
                loop = False
                break # Evita encontrar dois arquivos com o mesmo nome
    
    if path is None:
        print("\nArquivo nao encontrado!\n")

# ---------------------- Menu de Estrutura de Dados ---------------------- #

loop=True

while loop: 

    print_menu_estrutura_dados()
    tipo_estrutura = input("Digite sua escolha [1-4]: ")
    tipo_estrutura = int(tipo_estrutura)

    def cria_grafo():
        global grafo # Torna o grafo acessível fora desse contexto
        grafo = Instancia(tipo_estrutura)
        grafo = grafo._leArquivo(path)
        print(grafo)

    if tipo_estrutura == 1:     
        print ("\nMatriz de Adjacencia selecionada!\n")
        cria_grafo()
        loop = False

    elif tipo_estrutura == 2:
        print ("\nMatriz de Incidencia selecionada!\n")
        cria_grafo()
        loop = False

    elif tipo_estrutura == 3:
        print ("\nLista de Adjacencia selecionada!\n")
        cria_grafo()
        loop = False

    elif tipo_estrutura == 4:
        print ("Saindo...")
        sair = True
        loop = False

    else:
        print ("\nOpcao escolhida invalida!\n")

# ------------------------------ Menu Geral ------------------------------ #

loop=True

while loop and not sair:
    print_menu_geral()
    escolha = input("Digite sua escolha [1-X]: ") # Editar o X para o número final de opções
    escolha = int(escolha)

    if escolha == 1:     
        print (grafo)
        print("\n")

    elif escolha == 2:     
        print ("\nDigite dois vertices para verificar se eles sao vizinhos")
        parVertices = input("u,v: ")
        parVertices = parVertices.split(",")
        u = parVertices[0]
        v = parVertices[1]
        print(grafo._ehVizinho(u,v))
        print("\n")

    elif escolha == 3:
        print ("\nDigite um vertice para verificar seus vizinhos")
        vertice = input("u: ")
        print(grafo._obtemVizinhos(vertice))
        print("\n")

    elif escolha == 10: # Opção temporária
        print ("Saindo...")
        sair = True
        loop = False

    else:
        print ("\nOpcao escolhida invalida!\n")


# ---------------------- Operações Temporárias ---------------------- #
# ----------- Serão removidas após o término de todos os menus ------ #

if not sair :
    print (67 * "-")
    # for v in vizinhos:
    #     print(v)
    # arestas = grafo._obtemArestas()
    # for e in arestas:
    #     print(e)