from Aresta import Aresta

# Definição do nosso "INFINITO"
INF = 1E8

class MatrizAdj(object): 
    # Construtor da classe
    def __init__(self):
        self.__M = [] # Cria, inicialmente, uma matriz sem elementos
        # Numero de vertices (Membro privado da classe)
        self.__nVertices = 0 
        '''
        Dicionario que contem o nome do vertice como chave e como 
        valor, sua posicao na lista
        '''
        self.__posicoes = {} 
        '''
        Dicionario que contem a posicao do vertice na matriz como 
        chave e como valor, o nome do vertice
        '''
        self.__vertices = {}
    
    # Destrutor da classe
    def __del__(self):  
        del self.__M

    # Impressão da matriz de adjacência
    def __str__(self):
        saida = "V = { "
        for v in self.__posicoes:
            saida += v + " "
        saida += "}\n"

        saida += "Matriz de adjacencia\n"
        for i in range(self.__nVertices):
            for j in range(self.__nVertices):
                saida += str(self.__M[i][j]) + " "
            saida += "\n"
        saida += "\n"
        return saida

    '''
    Dada uma posição da matriz, retorna um vertice (neste caso, 
    optei pelo nome)
    '''
    def _obtemVertice(self, pos):
        return self.__vertices[pos]

    # Dado um vértice, retorna sua posição relativa na matriz
    def _obtemPosicao(self, u):
        try:
            return self.__posicoes[str(u)]
        except:
            return -1

    '''
    Retorna os vizinhos do vertice u (retorna sua posicao 
    relativa na matriz)
    '''
    def _obtemVizinhos(self, u):
        lista = []
        pos_u = self._obtemPosicao(str(u))
        for i in range(self.__nVertices):
            if(self.__M[pos_u][i] != 0 and self.__M[pos_u][i] != INF):
                lista.append(self.__vertices[i])
        return lista

    # Verifica se o vertice u eh vizinho de v
    def _ehVizinho(self, u, v):
        # Obtenção da posição relativa do vértice u
        pos_u = self._obtemPosicao(u) 
        # Obtenção da posição relativa do vértice v
        pos_v = self._obtemPosicao(v) 

        if(pos_u >= 0 and pos_v >= 0):
            return (self.__M[pos_u][pos_v] != 0 and 
                    self.__M[pos_u][pos_v] != INF)

        # Caso pos_u == -1 ou pos_v == -1
        return False

    # Remove o vertice u do grafo
    def _removeVertice(self, u):
        print("Exercicio")

    # Remove a aresta (u,v) do grafo
    def _removeAresta(self, e, u, v):
        print("Exercicio")
        
    # Esta funcao retorna a lista de arestas do grafo
    def _obtemArestas(self):
        listaArestas = []
        for pos_u in range(self.__nVertices):
            u = self.__vertices[pos_u]
            for pos_v in range(self.__nVertices):
                v = self.__vertices[pos_v]
                if(self.__M[pos_u][pos_v] != 0 and self.__M[pos_u][pos_v] != INF):
                    aresta = Aresta(u, v, self.__M[pos_u][pos_v])
                    listaArestas.append(aresta)
        
        return listaArestas
      
    '''
    Nesta função, adicionamos um novo elemento ao grafo, que pode ser:
    (a) Um único vértice
    (b) Uma aresta (ou arco), valorada ao não
    '''
    def _adiciona(self, u, v = None, peso = 1, direcionado = True):
        if(u == None):
            return

        vertice_u = str(u)
        # Se v for None, então verificamos a inserção de um vértice
        if(v == None):
            # Se u não foi inserido, vamos inserí-lo
            if(not (vertice_u in self.__posicoes)):
                self.__criaVertice(u)

        else:
            vertice_v = str(v)
            # Se u e v não são vizinhos, cria a ligação entre eles
            if(not(self._ehVizinho(u, v))):
                self.__criaAresta(u, v, peso)

                if(not direcionado):
                    self.__criaAresta(v, u, peso)
    
    '''
    Cria uma aresta de ligação entre os vértices u e v, 
    dado um peso (1, por default)
    '''
    def __criaAresta(self, u, v, peso = 1):
        # Obtenção da posição relativa do vértice u
        pos_u = self._obtemPosicao(u) 
        # Obtenção da posição relativa do vértice v
        pos_v = self._obtemPosicao(v) 
        # Ligação dos vértices u e v
        if(pos_u >= 0 and pos_v >= 0):
            self.__M[pos_u][pos_v] = peso
    
    # Criacao de um vertice para a matriz
    def __criaVertice(self, u):
        self.__nVertices += 1
        self.__M.append([0])

        self.__posicoes[str(u)] = self.__nVertices - 1
        self.__vertices[self.__nVertices - 1] = str(u)

        # Se tamanho é igual a 1, teremos apenas um vértice isolado
        if(self.__nVertices == 1):
            return

        '''
        Para cada vértice do grafo, adicionamos sua ligação 
        ao novo vértice
        '''
        for i in range(self.__nVertices - 1):        
            self.__M[i].append(0)

        # Criamos as arestas do novo grafo
        for i in range(self.__nVertices - 1):
            self.__M[self.__nVertices - 1].append(0)