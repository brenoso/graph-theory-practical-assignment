from ListaAdj import ListaAdj

# Definição do nosso "INFINITO"
INF = 1E8

# Classe que obtem os dados de entrada para a montagem do grafo
class Instancia(object):
    def __init__(self, arquivo = None):
        # Objeto que realiza a leitura dos arquivos de entrada
        self.__arquivo = arquivo 
  
    def _leArquivo(self, nomeArq):
        # Objeto que realiza a leitura dos arquivos de entrada
        self.__arquivo = open(nomeArq, 'r') 

        linhas = self.__arquivo.readlines()
        
        direcionado = True
        # Retirando o '\n' da string
        if(linhas[0].rstrip('\n') == "UNDIRECTED"): 
            direcionado = False
        
        # Estrutura de lista de adjacencia 
        g = ListaAdj()
        
        # Estrutura de matriz de adjacencia
        #g = MatrizAdj()
        
        # Estrutura de matriz de incidencia
        #g = MatrizInc()
        
        print (linhas[1])
        nVertices = int(linhas[1])
        
        # Conjunto de labels dos vertices (faço por conveniência)
        setLabels = set([])
        for i in range(2, len(linhas)):
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
        for i in range(2, len(linhas)):
            linha = linhas[i].split()
            if(len(linha) == 2): # Se for nao-valorado
                g._adiciona(linha[0], linha[1], 1, direcionado)
                
            else: # Se for valorado
                g._adiciona(linha[0], linha[1], float(linha[2]), 
                            direcionado)
                
        return g