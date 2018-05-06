from Aresta import Aresta

# Definição do nosso "INFINITO"
INF = 1E8

class MatrizAdj(object): 
    # Construtor da classe
    def __init__(self, direcionado):

        # Representa a matriz
        self.__M = []
        self.__nVertices = 0 
        '''
        Representa o nome do vertice como chave, e como 
        valor, a sua posicao na lista
        '''
        self.__posicoes = {} 
        '''
        Representa a posicao do vertice na matriz como 
        chave, e como valor, o seu nome
        '''
        self.__vertices = {}
        self._direcionado = direcionado
    
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


    # Retorna o vértice de determinada posição da matriz
    def _obtemVertice(self, pos):
        return self.__vertices[pos]

    # Dado um vértice, retorna sua posição relativa na matriz
    def _getPosicao(self, u):
        try:
            return self.__posicoes[str(u)]
        except:
            return -1

    '''
    Retorna os vizinhos do vertice u (retorna sua posicao 
    relativa na matriz)
    '''
    def _obtemVizinhos(self, u):
        vizinhos = []
        pos_u = self._getPosicao(str(u))
        for i in range(self.__nVertices):
            if(self.__M[pos_u][i] != 0 and self.__M[pos_u][i] != INF):
                vizinhos.append(self.__vertices[i])
        return vizinhos

    # Verifica se o vertice u é vizinho de v
    def _ehVizinho(self, u, v):
        # Obtenção da posição relativa do vértice u
        pos_u = self._getPosicao(u) 
        # Obtenção da posição relativa do vértice v
        pos_v = self._getPosicao(v) 

        if(pos_u >= 0 and pos_v >= 0):
            return (self.__M[pos_u][pos_v] != 0 and 
                    self.__M[pos_u][pos_v] != INF)

        # Caso pos_u == -1 ou pos_v == -1
        return False

    # Remove o vertice u do grafo
    def _removeVertice(self, u):
        print("Ainda nao implementado")

    # Deleta a aresta (u,v) do grafo
    def _deletaAresta(self, u, v):
        u = int(u)
        v = int(v)

        # Tenta acessar a posicao da possível aresta na matriz
        try:
            self.__M[u][v]
        except:
            return False

        if self.__M[u][v] != 0 and self.__M[u][v] != INF: # Checa a existencia da aresta
            self.__M[u][v] = 0 # Remove a aresta            
        else:
            return False # Aresta não removida pois já não existia.

        ''' 
        Verifica se o grafo é direcionado. Caso não seja
        deve remover a (u,v) e a (v,u) na matriz
        '''
        if self._direcionado == True:
            return True # Retorna que a aresta (u,v) foi removida com sucesso
        else:
            self.__M[v][u] = 0
            return True # Remove também a (v,u) e retorna sucesso

    '''
    Recebe dois vértices u e v como parâmetros 
    e retorna true se v é predecessor de u (v aponta pra u)
    Apenas para grafos direcionados.
    '''
    def _ehPredecessor(self,u,v):

        u = int(u)
        v = int(v)

        # Tenta acessar a posicao da aresta na matriz
        try:
            self.__M[v][u]
        except:
            return False
            
        if self.__M[v][u] != 0 and self.__M[v][u] != INF: # Se v aponta para u retorna True
            return True
        else:
            return False

    '''
    Recebe dois vértices u e v como parâmetros 
    e retorna true se v é sucessor de u (u aponta pra v)
    Apenas para grafos direcionados.
    '''
    def _ehSucessor(self,u,v):

        u = int(u)
        v = int(v)

        # Tenta acessar a posicao da aresta na matriz
        try:
            self.__M[u][v]
        except:
            return False
            
        if self.__M[u][v] != 0 and self.__M[u][v] != INF: # Se u aponta para v retorna True
            return True
        else:
            return False
    
    '''
    Recebe um vértice u como parâmetro e retorna
    o conjunto de sucessores desse vértice
    (Todos os vértices dos quais u aponta)
    Apenas para grafos direcionados.
    '''
    def _obtemSucessores(self,u):
        
        u = int(u)

        # Tenta acessar a posicao da aresta na matriz
        try:
            self.__M[u][0]
        except:
            return []

        return self._obtemVizinhos(u)

    '''
    Recebe um vértice u como parâmetro e retorna
    o conjunto de predecessores desse vértice
    (Todos os vértices que apontam para u)
    Apenas para grafos direcionados.
    '''
    def _obtemPredecessores(self,u):
        
        u = int(u)
        predecessores = []

        # Verifica a existencia do vértice
        try:
            self.__M[u][0]
        except:
            return []

        # Verifica para cada vértice, se ele é predecessor do vértice u
        for i in range(self.__nVertices):
            if self.__M[i][u] != 0 and self.__M[i][u] != INF:
                predecessores.append(self.__vertices[i])

        return predecessores

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
    def _add(self, u, v = None, peso = 1):
     
        if(u == None):
            return

        u = str(u)

        # Se não for passado o argumento v, será considerado apenas o vértice u
        if(v == None):
            # Verifica se o vértice u já consta no grafo, caso contrário o insere
            if(not (u in self.__posicoes)):
                self.__criaVertice(u)
        else:
            v = str(v)
            # Se u e v ainda não são vizinhos, cria a ligação (aresta) entre eles
            if(not(self._ehVizinho(u, v))):
                self.__criaAresta(u, v, peso)

                # Se não for direcionado, cria uma aresta fazendo a ligação inversa da
                # anterior (u->v e u<-v)
                if(not self._direcionado):
                    self.__criaAresta(v, u, peso)
    
    '''
    Cria uma aresta de ligação entre os vértices u e v, 
    dado um peso (1, por default)
    '''
    def __criaAresta(self, u, v, peso = 1):
        # Obtenção da posição relativa do vértice u
        pos_u = self._getPosicao(u) 
        # Obtenção da posição relativa do vértice v
        pos_v = self._getPosicao(v) 
        # Ligação dos vértices u e v
        if(pos_u >= 0 and pos_v >= 0):
            self.__M[pos_u][pos_v] = peso
    
    # Criacao de um vertice para a matriz
    def __criaVertice(self, u):
        self.__nVertices += 1

        self.__M.append([0])

        self.__posicoes[str(u)] = self.__nVertices - 1 # Adiciona o vértice na lista de posicões
        
        self.__vertices[self.__nVertices - 1] = str(u)

        '''
        Retorna caso o número de vértices no grafo seja 1
        pois não terá nenhuma ligação com outro vértice
        '''
        if(self.__nVertices == 1):
            return

        '''
        Varre toda a matriz adicionando a cada linha (vértice do grafo)
        mais uma coluna (que representa a ligação com o novo vértice)
        inicialmente com o valor 0
        '''
        for i in range(self.__nVertices - 1):
            self.__M[i].append(0)


        '''
        Cria as conexões (arestas) do novo vértice
        preenchendo todas as suas colunas com o valor 0
        '''
        for i in range(self.__nVertices - 1):
            self.__M[self.__nVertices - 1].append(0)