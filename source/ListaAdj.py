from Vertice import Vertice
from Aresta import Aresta

# Definição do nosso "INFINITO"
INF = 1E8

# Classe Grafo - Matriz de Adjacências
class ListaAdj(object):
    # Construtor da classe
    def __init__(self, direcionado):
        # Lista de adjacencia de vertices (Membro privado da classe)
        self.__lista = [] 
        # Numero de vertices (Membro privado da classe)
        self.__nVertices = 0 
        '''
        Dicionario que contem o nome do vertice como chave e 
        como valor, sua posicao na lista
        '''
        self.__posicoes = {}
        self._direcionado = direcionado

    # Destrutor da classe
    def __del__(self):  
        for v in self.__lista:
            del v 

    # Impressão da lista
    def __str__(self):
        saida = "V = { "
        for v in self.__lista:
            saida += v._obtemNome() + " "
        saida += "}\n"

        # Impressão da lista de arestas
        saida += "Vizinhanca dos vertices \n"
        for v in self.__lista:
            saida += v._obtemNome() + ": "
            aux = v._obtemProximo()
            if aux is not None:
                while(aux._obtemProximo() != None):
                    saida += aux._obtemNome() + "(" + str(aux._obtemPeso()) + ") "
                    aux = aux._obtemProximo()
                saida += aux._obtemNome() + "(" + str(aux._obtemPeso()) + ") "
            saida += "\n"
            saida += "\n"
        return saida    
  
    # Dada uma posição na lista, retorna o vértice correspondente
    def _obtemVertice(self, pos):
        return self.__lista[pos]
        
    # Dado um vértice, retorna sua posição relativa na lista
    def _obtemPosicao(self, v):
        try:
            return self.__posicoes[str(v)]
        except:
            return -1

    # Retorna a lista de vizinhos do vertice u
    def _obtemVizinhos(self, u):
        lista = [] # Lista dos nomes dos vértices

        # Obtendo a posicao do vertice u
        pos = self._obtemPosicao(u)

        # Já partindo do próximo vértice que u aponta
        aux = self.__lista[pos]._obtemProximo()

        # Enquanto pudermos avançar na lista
        while(aux != None):
            tmp = self._obtemPosicao(aux._obtemNome())
            lista.append(self.__lista[tmp]._obtemNome())
            aux = aux._obtemProximo()
        return lista
 
    # Retorna True se os vertices u e v sao vizinhos
    def _ehVizinho(self, u, v):
        vertice_u = str(u)
        vertice_v = str(v)

        # Busca o vértice de nome 'u'
        pos_u = self._obtemPosicao(vertice_u)
        aux = self.__lista[pos_u]
        while(aux != None): # Buscamos na lista do vértice 'u'
            # Se encontramos 'v' nesta lista
            if(aux._obtemNome() == vertice_v): 
                return True # Conclusão: 'u' e 'v' são vizinhos
            aux = aux._obtemProximo() # Senão, vamos para o próximo da lista
        '''
        Por fim, caso não encontremos 'v' na lista de 'u', 
        retornamos False
        '''
        return False 
  
    # Remove o vértice u do grafo
    def _removeVertice(self, u):
        return False # Ainda não implementado
    
    # Remove a aresta (u,v) do grafo
    def _deletaAresta(self, u, v):
        return False # Ainda não implementado
    
    '''
    Recebe dois vértices u e v como parâmetros 
    e retorna true se v é predecessor de u (v aponta pra u)
    Apenas para grafos direcionados.
    '''
    def _ehPredecessor(self,u,v):
        return False # Ainda não implementado

    '''
    Recebe dois vértices u e v como parâmetros 
    e retorna true se v é sucessor de u (u aponta pra v)
    Apenas para grafos direcionados.
    '''
    def _ehSucessor(self,u,v):
        return self._ehVizinho(u,v)

    '''
    Recebe um vértice u como parâmetro e retorna
    o conjunto de sucessores desse vértice
    (Todos os vértices dos quais u aponta)
    Apenas para grafos direcionados.
    '''
    def _obtemSucessores(self, u):
        listaDeSucessores = []

        for v in self.__lista:
            for v2 in self.__lista:
                if (u == v._obtemNome() and self._ehSucessor(u, v2._obtemNome())):
                    # Só tá adicionando o primeiro sucessor
                    listaDeSucessores.append(v2._obtemNome())

        return listaDeSucessores
    
    '''
    Recebe um vértice u como parâmetro e retorna
    o conjunto de predecessores desse vértice
    (Todos os vértices que apontam para u)
    Apenas para grafos direcionados.
    '''
    def _obtemPredecessores(self,u):
        return [] # Ainda não implementado
    
    '''
    Deleta um vértice do grafo e as arestas 
    indicentes a ele (por consequência)
    '''
    def _deletaVertice(self,u):
        return False # Ainda não implementado

    # Esta funcao retorna a lista de arestas do grafo
    def _obtemArestas(self):
        # Lista de arestas
        listaArestas = []
        
        # Percorrendo as posicoes da lista de vertices
        for pos_u in self.__posicoes.values():
            u = self.__lista[pos_u]
            v = self.__lista[pos_u]._obtemProximo()
            # Enquanto pudermos avançar na lista
            while(v != None):
                aresta = Aresta(u._obtemNome(), v._obtemNome(), v._obtemPeso())
                listaArestas.append(aresta)
                v = v._obtemProximo()
                
        return listaArestas
      
    '''
    Nesta função, adicionamos um novo elemento ao grafo, que pode ser:
    (a) Um único vértice
    (b) Uma aresta (ou arco), valorada ao não
    '''
    def _add(self, u, v = None, peso = 1):
        if(u == None):
            return # Nem  vértice de origem é válido
        
        vertice_u = str(u)
    
        # Se v for None, então verificamos a inserção de um vértice
        if(v == None):
            # Se u não foi inserido, vamos inserí-lo
            if(not (u in self.__lista)):
                self.__criaVertice(u)
                self.__nVertices += 1

        else:
            vertice_v = str(v)
            pos_u = self._obtemPosicao(u)
            pos_v = self._obtemPosicao(v)

            # Se u e v não são vizinhos, cria a ligação entre eles
            if(pos_u >= 0 and pos_v >= 0 and not(self._ehVizinho(u, v))):
                self.__criaAresta(u, v, peso)

                if(not self._direcionado):
                    self.__criaAresta(v, u, peso)
    
    '''
    Cria uma aresta de ligação entre os vértices u e v, dado um 
    peso (1, por default)
    '''
    def __criaAresta(self, u, v, peso = 1):
        pos1 = self._obtemPosicao(u)
        pos2 = self._obtemPosicao(v)
        
        if(pos1 >= 0 and pos2 >= 0):
            aux = self.__lista[pos1] # Vértice auxiliar
            # Encontra o próximo elemento do vetor
            while(aux != None and aux._obtemProximo() != None):                
                aux = aux._obtemProximo()
            # Cria um nó na lista de u contendo o vértice v
            aux._criaProximo(Vertice(self.__lista[pos2]._obtemNome(), peso))    

            # Modifica o último para apontar para nulo
            prox = aux._obtemProximo()
            prox._modificaProximo(None)

    # Criacao de um vertice para a lista
    def __criaVertice(self, u):
        '''
        Testa se o vértice u eh novo (ou seja: nao foi encontrado 
        no grafo)
        '''
        if(self._obtemPosicao(u) == -1):
            vertice = Vertice(u)
            self.__lista.append(vertice)
            self.__posicoes[str(u)] = self.__lista.index(vertice)