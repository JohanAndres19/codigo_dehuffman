import sys
from PyQt5.QtGui import QTextOption 
from  PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize, Qt
from qt_for_python.uic.ventanaH import *
from qt_for_python.uic.ventanav import *
import execjs
import logica;
from grafo import *
#-------------------------------------
#------------- Interfaz---------------

class Ventana_principal(QMainWindow):
    def __init__(self,modelo):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.modelo=modelo
        self.controlador=Controlador(self)
        #----------------------------
        self.setWindowTitle("HUFFMAN")
        self.ui.textEdit.setReadOnly(True)
        self.ui.textEdit.setWordWrapMode(QTextOption.NoWrap)
        #--------------------------------
        self.ui.text_ingresar.setClearButtonEnabled(True)
        self.ui.tableWidget.setVisible(False)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def Get_modelo(self):
        return self.modelo

#--------------------------------------
#--------------------------------------

class Controlador():
    def __init__(self,ventana):
        self.ventana =ventana
        self.Eventos()

    def Eventos(self):
        self.ventana.ui.boton_encriptar.clicked.connect(lambda: self.ventana.Get_modelo().Encriptar())
        self.ventana.ui.boton_mostrar.clicked.connect(lambda: self.ventana.Get_modelo().Mostrar_arbol())
        self.ventana.ui.pushButton.clicked.connect(lambda:self.ventana.Get_modelo().Mostrar_simbolos())
#---------------------------------------
#---------------------------------------
class Modelo ():
    def __init__(self) :
        self.ventana = Ventana_principal(self)
        self.matriz =None
        self.valores_in=[]

    def Encriptar(self):
        texto=self.ventana.ui.text_ingresar.text()
        if texto!='':
            js=  execjs.compile(open(r'Huffman_codigo.js').read())
            dicc= js.call('codificar',texto)
            self.matriz=dicc['matriz']
            self.textoencri=dicc['txtoincriptado']
            aux=self.textoencri.split(' ')
            self.valor_sim=dicc['simbolosencri']
            self.palabra=''
            for i in range(len(aux)):
                j=texto[i].center((len(aux[i])+2))
                self.palabra+=j
            print(self.palabra)
            print(list(self.valor_sim.keys()))
            self.Mostrar_tabla()    
 
    def Mostrar_arbol(self):
        arbol =logica.construirarbol(self.matriz,len(self.matriz[0])-1,list(self.valor_sim.keys()))
        Grafica().Graficar(arbol,len(list(self.valor_sim.keys())))
    
    def Mostrar_simbolos(self):
        self.ventanav =QtWidgets.QMainWindow()
        self.ui =Ui_MainWindow2()
        self.ui.setupUi(self.ventanav)
        self.ui.textEdit.setReadOnly(True)
        palabras=' Diccionario de simbolos : \n' 
        for i in self.valor_sim:
            palabras+=' '+i+' : '+self.valor_sim[i]+'\n'
        self.ui.textEdit.setText(palabras)   
        self.ui.label_2.setWordWrap(True)
        cantidad=0
        for i in self.textoencri.split(' '):
            cantidad+=len(i)
        texto='cantidad de bits cadena original :\n'+ str(8*len(self.ventana.ui.text_ingresar.text()))+'\ncantidad de bits cadena codificada : \n'+ str(cantidad)+'\nahorro :\n'+"{:.3f}".format(100-((cantidad*100)/(8*len(self.ventana.ui.text_ingresar.text()))))+'%'
        self.ui.label_2.setText(texto)
        self.ventanav.show()
    
    def Mostrar_tabla(self): 
        labels_en_x=[]
        if self.ventana.ui.tableWidget.rowCount()!=0:
            self.ventana.ui.tableWidget.clearContents()
            self.ventana.ui.tableWidget.setRowCount(0)
            self.ventana.ui.tableWidget.setColumnCount(0)
        for i in range(len(self.matriz[0])):
            self.ventana.ui.tableWidget.insertColumn(i)
            self.ventana.ui.tableWidget.setColumnWidth(i,41)
        if self.ventana.ui.tableWidget.columnCount()>21:
             self.ventana.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        else:
             self.ventana.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        for i in range(len(self.matriz)):
            self.ventana.ui.tableWidget.insertRow(i)
            self.ventana.ui.tableWidget.setRowHeight(i,41)    
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])) :
                celda= QTableWidgetItem(str(self.matriz[i][j]))
                celda.setTextAlignment(Qt.AlignHCenter)
                self.ventana.ui.tableWidget.setItem(i,j,celda)
        for i in range(len(self.matriz[0])):
            labels_en_x.append(str(i))
        self.ventana.ui.tableWidget.setHorizontalHeaderLabels(labels_en_x)    
        self.ventana.ui.tableWidget.setVerticalHeaderLabels(["SIMBOLO","FRECUENCIA","PADRE","TIPO","IZQ","DER"])
        self.ventana.ui.tableWidget.setVisible(True) 
        self.ventana.ui.textEdit.setText(self.palabra+'\n'+self.textoencri)

    def Get_ventana(self):
        return self.ventana    

#--------------------------------------
#---------------Main------------------- 
if __name__ =="__main__":
    app =QApplication(sys.argv)
    gui = Modelo().Get_ventana()
    gui.show()
    sys.exit(app.exec_())
