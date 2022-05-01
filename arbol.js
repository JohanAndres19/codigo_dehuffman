class Nodo {
    constructor(valor = null, nododerecho = null, nodoizquierdo = null) {
        this.valor = valor;
        this.nododerecho = nododerecho;
        this.nodoizquierdo = nodoizquierdo;
    }
}


function construirarbol(matriz, pos, simbolos) {
    var nodo = null;
    if (matriz[0][pos] in simbolos) {
        nodo= new Nodo(matriz[0][pos])
        return nodo  
    } else {
        nodo = new Nodo(pos);
        nodo.nodoizquierdo=construirarbol(matriz,matriz[4][pos],simbolos);
        nodo.nododerecho=construirarbol(matriz,matriz[5][pos],simbolos);
        return nodo
    }
}


