# -*- coding: utf-8 -*-

class Aresta (object):

    '''
    Construtor da classe
    '''
    def __init__(self, u, v, peso = 1):
        self.__u = str(u)
        self.__v = str(v)
        self.__peso = peso

    '''   
    Imprime a aresta
    '''
    def __str__(self):
        return " (" + str(self.__u) + ", " + str(self.__v) + ")(" + str(self.__peso) + ") "
    
    '''
    Retorna uma lista com o par ordenado de vértices que compõem a aresta
    '''
    def _obtemAresta(self):
        return [self.__u, self.__v]

    def _obtemVerticeU(self):
        return self.__u
    
    def _obtemVerticeV(self):
        return self.__v

    def _obtemPeso(self):
        return self.__peso