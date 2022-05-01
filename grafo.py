import networkx as nx
from networkx.drawing.nx_agraph import write_dot, graphviz_layout
import matplotlib.pyplot as plt

G = nx.DiGraph()

class Grafica:
    def __init__(self):
        self.G = nx.DiGraph()

    def Graficar(self,nodo,tamaño):
        contador=self.Grafica_arbol(nodo,0)
        if contador==tamaño:
            print('funciona')
            plt.title('Arbol')
            pos =graphviz_layout(self.G, prog='dot')
            nx.draw(self.G, pos, with_labels=True, arrows=True)
            plt.show()
        else:
            print('pailas')

    def Grafica_arbol(self,nodo,contador):
        if nodo.nododerecho==None and nodo.nodoizquierdo==None:
            contador+=1
            return contador
        else:
            if not self.G.has_node(nodo.valor):
                self.G.add_node(nodo.valor)
            self.G.add_node(nodo.nodoizquierdo.valor)
            self.G.add_node(nodo.nododerecho.valor)
            self.G.add_edge(nodo.valor,nodo.nodoizquierdo.valor)
            self.G.add_edge(nodo.valor,nodo.nododerecho.valor)
            contador=self.Grafica_arbol(nodo.nodoizquierdo,contador)
            contador=self.Grafica_arbol(nodo.nododerecho,contador)
            return contador




# write dot file to use with graphviz
# run "dot -Tpng test.dot >test.png"

# same layout using matplotlib with no labels

