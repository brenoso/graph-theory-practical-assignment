class Aresta (object):
    # Construtor da classe (Membros privados)
    def __init__(self, u, v, peso = 1):
        self.__u = str(u)
        self.__v = str(v)
        self.__peso = peso
        
    # Personaliza a impressao da aresta
    def __str__(self):
        return " (" + str(self.__u) + ", " + str(self.__v) + ")(" + str(self.__peso) + ") "
    
    # Obtem vertices da aresta (retorna uma lista com dois elementos)
    def _obtemAresta(self):
        return [self.__u, self.__v]
    
    # Retorna o peso da aresta
    def _obtemPeso(self):
        return self.__peso