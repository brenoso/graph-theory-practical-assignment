from Instancia import Instancia

instancia = Instancia()
grafo = instancia._leArquivo("../instances/Padrao_Txt/n5_dir_wgt_comb0.txt")
print(grafo)
print(grafo._ehVizinho(1,2)) # True
print(grafo._ehVizinho(1,10)) # False
# Vizinhos do vertice 2
vizinhos = grafo._obtemVizinhos(1)
for v in vizinhos:
    print(v)

arestas = grafo._obtemArestas()
for e in arestas:
    print(e)