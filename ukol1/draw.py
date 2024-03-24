from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtGui import QMouseEvent, QPaintEvent
from PyQt6.QtWidgets import *
import shapefile
import algorithms


class Draw(QWidget):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Inicialize features
        self.q = QPointF(-100, -100)
        self.add_vertex = False
        self.pol = QPolygonF()
        self.polygons = []
        self.features = None
        self.min_max = [0,0,10,10]
        self.result = []

    # function for loading input data
    def loadData(self, filename):   
        # load objects from shapefile
        filename, _ = QFileDialog.getOpenFileName(self, "Open file", "", "Shapefile (*.shp)")
        if filename:
            shp = shapefile.Reader(filename)
            self.features = shp.shapes()

            # calculate minimum and maximum coordinates
            min_x, min_y, max_x, max_y = float('inf'), float('inf'), -float('inf'), -float('inf')
            for feature in self.features:
                for point in feature.points:
                    min_x = min(min_x, point[0])
                    min_y = min(min_y, point[1])
                    max_x = max(max_x, point[0])
                    max_y = max(max_y, point[1])
            # store minimum and maximum coordinates
            self.min_max = [min_x, min_y, max_x, max_y]
        
    # function for rescaling data to fit Canvas  
    def resizeData(self):
        # get width and height of the widget
        width = self.frameGeometry().width()
        height = self.frameGeometry().height()
        
        # initialize list for storing polygons
        self.polygons = [None] * len(self.features)

        # rescale data and create polygons
        for k, feature in enumerate(self.features):
            self.polygons[k] = QPolygonF()
            for point in feature.points:
                x = int(((point[0] - self.min_max[0]) / (self.min_max[2] - self.min_max[0]) * width))
                y = int((height - (point[1] - self.min_max[1]) / (self.min_max[3] - self.min_max[1]) * height))
                p = QPointF(x, y)
                self.polygons[k].append(p)        

    # function to draw point 
    def mousePressEvent(self, e: QMouseEvent):
        # get cursor position
        x = e.position().x()
        y = e.position().y()
        
        # add vertex
        self.q.setX(x)
        self.q.setY(y) 
            
        # repaint
        self.repaint()
    
    #  function that sets colors
    def paintEvent(self, e: QPaintEvent):
        # create new object
        qp = QPainter(self)
        # start drawing
        qp.begin(self)
        # set graphical attributes
               
        for index, polygon in enumerate(self.polygons):
            # set graphical attributes
            qp.setPen(QPen(Qt.GlobalColor.black))
            qp.setBrush(Qt.GlobalColor.lightGray)
            
            if self.result and (self.result[index] == 1) or self.result and (self.result[index] == -1):
                qp.setBrush(Qt.GlobalColor.cyan)
                
            # draw polygon
            qp.drawPolygon(polygon)
            
        self.result = []
        
        qp.setPen(QPen(Qt.GlobalColor.black))
        qp.setBrush(Qt.GlobalColor.red)
        
        if self.add_vertex == True:
            # draw vertex
            r = 5
            qp.drawEllipse(int(self.q.x()-r), int(self.q.y()-r), 2*r, 2*r)
                
        qp.end()
    
    # function that sets the result
    def setResult(self, results):
        self.result = results
        self.repaint()

    # function that adds a point or removes a point
    def switchDrawing(self):
        self.add_vertex = not(self.add_vertex)
        self.repaint()
        
    # function that returns analyzed point
    def getQ(self):
        # return analyzed point
        return self.q
    
    # function that returns analyzed polygon
    def getPol(self):
        # return analyzed polygon
        return self.pol
    
    # function that returns analyzed polygons
    def getPols(self):
        return self.polygons
    
    # function to clear the screen
    def clearData(self):
        # clear data
        self.pol.clear()
        self.polygons.clear()
        self.q.setX(-100)
        self.q.setY(-100)
        self.repaint()
        
#chceme vice polygonu, ale nechceme message box ale zvyraznit polygon- 
# vysledek zadny polygon, jeden polygon, dva nebo vice nez dva
#misto self polygonu budu mit list polygonů [],
# analyzační funkce bude opakovane volat funkci analyzepointandpolygon na vsechny polygony
#for pol in pols : 
#   res = anayzePointPolygonPosition(q, pol)
#results []bude obsahovta vsechny polygony, ktere jsou true (jejich id)
#pred vykreslenim polygonu se zeptame jestli je v tom seznamu a pokud ano, tak ho zvyraznime


        
        
        