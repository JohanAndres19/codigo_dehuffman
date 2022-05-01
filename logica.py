class Nodo :
    def __init__(self,valor = None, nododerecho = None, nodoizquierdo = None):
        self.valor = valor
        self.nododerecho = nododerecho
        self.nodoizquierdo = nodoizquierdo
    



def construirarbol(matriz, pos, simbolos): 
    nodo = None
    if matriz[0][pos] in simbolos :
        nodo= Nodo(matriz[0][pos])
        print(nodo.valor)
        return nodo  
    else: 
        nodo =Nodo(pos)
        nodo.nodoizquierdo=construirarbol(matriz,matriz[4][pos],simbolos)
        nodo.nododerecho=construirarbol(matriz,matriz[5][pos],simbolos)
        print(nodo.valor)
        return nodo
    
