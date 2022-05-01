var matriz = [];
var frecuencia=[]
var txtoincriptado=''
function codificar(texto) {   
    var simbolosfre = obtener_simbolo_frecuencia(texto);
    // rellenar la matriz
    matriz=rellenar_matriz(simbolosfre);
    frecuencia=JSON.parse(JSON.stringify(matriz[1]))
    operar_matriz(simbolosfre.length);
    // ---------------------------
    for(let i=0; i<matriz[0].length;i++){
        if(matriz[0][i]==0){
            matriz[0][i]='-'
        }
    }
    var simbolosencri=encriptar(simbolosfre.length);
    txtoincriptado =encriptar_texto(texto,simbolosencri);
    txtoincriptado=txtoincriptado.trim();
    return {matriz,txtoincriptado,simbolosencri};
}
function encriptar_texto(texto,simbolosencri){
    let palabra=''
    for(let value of texto){
        palabra+=simbolosencri[value]+' ';
    }
    return palabra;
}
function operar_matriz(tamaño){
    var columna=tamaño;
    var izq=[];
    var der=[];
    do {
        izq = getNodo();
        der = getNodo();
        matriz[1][columna] = izq[0]+der[0];
        matriz[4][columna] = izq[1];
        matriz[5][columna] = der[1];
        matriz[2][izq[1]] = columna;
        matriz[2][der[1]] = columna;
        matriz[3][izq[1]] = 1;
        matriz[3][der[1]] = 2;
        frecuencia[columna] = izq[0]+der[0];
        columna++;
    } while (columna<matriz[0].length);
        
}

function getNodo(){
    var subarreglo = JSON.parse(JSON.stringify(frecuencia));
    subarreglo.sort(function(a,b){return a - b;});
    var valor=[0,0];
    let i=0;
    while(valor[0]==0  && i<subarreglo.length){
        valor[0]=subarreglo[i];
        i++;
    }
    valor[1]=frecuencia.indexOf(valor[0])
    frecuencia[valor[1]]=0;
    return valor
}

function rellenar_matriz(simbolosfre){
    for (let i = 0; i < 6; i++) {
        matriz.push([])
    }
    // agregar primeros valores
    for (let value of simbolosfre) {
        matriz[0].push(value[0])
        matriz[1].push(value[1])
    }
    var tamaño = matriz[0].length;
    for (let value of matriz) {
        let rowtamaño= value.length;
        for (let j = 0; j < ((tamaño * 2) - 1); j++) {
            if (rowtamaño!== 0) {
                if (j >((tamaño * 2) - 1 - rowtamaño)) {
                    value.push(0);
                }
            } else {
                value.push(0);
            }
        }
    }
    return matriz;
}
function obtener_simbolo_frecuencia(texto) {
    var simbolos = [];
    var frecu = [];
    var simbo_fre = [];
    for (let value of texto) {
        let contador = 0;
        if (!simbolos.includes(value)) {
            simbolos.push(value);
            contador++;
            frecu.push(contador);
        } else {
            frecu[simbolos.indexOf(value)]+=1;
        }
    }
    for (let i = 0; i < simbolos.length; i++) {
        simbo_fre.push([simbolos[i], frecu[i]]);
    }
    return simbo_fre.sort();
}


function encriptar(size){
    let encryptedSymbols={};
    for(let i = 0; i < size; i++){
        encryptedSymbols[matriz[0][i]]=encodeSymbol(i);
    }
    return encryptedSymbols;
}

function encodeSymbol(i){
    if(matriz[2][i] == matriz[0].length-1){
        if(matriz[3][i] == 1){
            return "0";
        }else{
            return "1";
        }
    }else{
        if(matriz[3][i] == 1){
            return encodeSymbol(matriz[2][i])+"0";
        }else{
            return encodeSymbol(matriz[2][i])+"1";
        }
    }
}



