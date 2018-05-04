from Instancia import Instancia
import os

# ---------------------- Menus Definition---------------------- #
def print_menu_arquivo():
    print ("Digite o nome do arquivo a ser lido:")


def print_menu_estrutura_dados():       ## Your menu design here
    print ("Escolha uma Estrutura de Dados para representar o grafo")
    print ("1. M.A.")
    print ("2. M.I.")
    print ("3. L.A.")
    print ("4. Sair")
    print (67 * "-")
# ---------------------- End Menus Definition ---------------------- #

# Menu de leitura do arquivo
loop=True      
  
while loop:
    print_menu_arquivo()
    arquivo = input()
    path = None

    # Navega pela pasta a procura do arquivo
    for root, dirs, files in os.walk("../instances"):
        for file in files:
            if file == arquivo:
                print("\nArquivo encontrado!\n")
                path = os.path.join(root, file)
                loop = False
    
    if path is None:
        print("\nArquivo nao encontrado!\n")

# Menu de leitura do arquivo
loop=True

while loop: 

    print_menu_estrutura_dados()
    tipo_estrutura = input("Enter your choice [1-4]: ")
    tipo_estrutura = int(tipo_estrutura)

    if tipo_estrutura==1:     
        print ("Matriz de Adjacencia selecionada")
        loop=False

    elif tipo_estrutura==2:
        print ("Matriz de Incidencia selecionada")
        loop=False

    elif tipo_estrutura==3:
        print ("Lista de Adjacencia selecionada")
        loop=False

    elif tipo_estrutura==4:
        print ("Menu 4 has been selected")
        # loop = False

    else:
        # Any integer inputs other than values 1-5 we print an error message
        print ("Wrong option selection. Enter any key to try again..")


instancia = Instancia(tipo_estrutura)
grafo = instancia._leArquivo(path)
print(grafo)
# print(grafo._ehVizinho(1,2)) # True
# print(grafo._ehVizinho(1,10)) # False
# # Vizinhos do vertice 2
# vizinhos = grafo._obtemVizinhos(1)
# for v in vizinhos:
#     print(v)

# arestas = grafo._obtemArestas()
# for e in arestas:
#     print(e)