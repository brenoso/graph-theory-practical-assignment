# -*- coding: utf-8 -*-

'''
Classe que representa um vértice do grafo e armazena o próximo
vértice na lista
'''
class Vertice(object):

    '''
    Construtor da classe
    '''
    def __init__(self, nome, peso = 1):
        self.__nome = str(nome)
        self.__peso = peso
        self.__proximo = None

    '''
    Destrutor da classe
    '''
    def __del__(self): 
        aux = self
        tmp = self.__proximo
        if(aux.__proximo != None):
            del tmp
        del aux

    '''    
    Personaliza a impressao do vértice
    '''
    def __str__(self):
        return " {" + str(self.__nome) + ", " + str(self.__peso) + "} "

    '''
    Cria o próximo vértice a ser inserido na lista
    '''
    def _criaProximo(self, v):      
        if(v != None):
            # Alocando um novo vértice
            self.__proximo = Vertice(v._obtemNome(), v._obtemPeso())
            return
        self.proximo = v
    
    '''            
    Modifica o próximo vértice da lista
    '''
    def _modificaProximo(self, v):
        self.__proximo = v

    '''    
    Retorna o nome do vértice
    '''
    def _obtemNome(self):
        return self.__nome
    
    '''
    Retorna o peso do vértice
    '''
    def _obtemPeso(self):
        return self.__peso
    
    '''
    Retorna o próximo vértice da lista
    '''
    def _obtemProximo(self):
        return self.__proximo