from ListaAdj import ListaAdj
from MatrizAdj import MatrizAdj
from MatrizInc import MatrizInc

# Definição do nosso "INFINITO"
INF = 1E8

# Classe que obtem os dados de entrada para a montagem do grafo
class Instancia(object):
    def __init__(self, tipo_estrutura, arquivo = None):
        # Objeto que realiza a leitura dos arquivos de entrada
        self.__arquivo = arquivo
        self.__tipo_estrutura = tipo_estrutura
  
    def _leArquivo(self, path):
        # Objeto que realiza a leitura dos arquivos de entrada
        self.__arquivo = open(path, 'r') 

        linhas = self.__arquivo.readlines()
        
        direcionado = True
        # Retirando o '\n' da string
        if(linhas[0].rstrip('\n') == "UNDIRECTED"): 
            direcionado = False
        
        if self.__tipo_estrutura == 1:
            g = MatrizAdj()
        elif self.__tipo_estrutura == 2:
            g = MatrizInc()
        elif self.__tipo_estrutura == 3:
            g = ListaAdj()

        # nVertices = int(linhas[1])
        nVertices = len(linhas) - 1
        
        # Conjunto de labels dos vertices (faço por conveniência)
        setLabels = set([])
        for i in range(1, len(linhas)):
            linha = linhas[i].split()
            setLabels.add(linha[0])
            setLabels.add(linha[1])
        setLabels = set(map(int, setLabels))

        '''
        Adicao dos primeiros vertices no grafo (no momento, o grafo 
        esta vazio)
        '''
        for i in setLabels:
            g._adiciona(str(i))
        
        # Criacao do grafo
        for i in range(1, len(linhas)):
            linha = linhas[i].split()
            if(len(linha) == 2): # Se for nao-valorado
                g._adiciona(linha[0], linha[1], 1, direcionado)
                
            else: # Se for valorado
                g._adiciona(linha[0], linha[1], float(linha[2]), 
                            direcionado)
                
        return g