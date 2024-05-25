from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from qpoint3df import *
from edge import *
from random import *
from triangle import *
from math import *
import shapefile
import sys



class Draw(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.features = []
        self.points = []
        self.dt = []
        self.contours = []
        self.dtm_slope = []
        self.dtm_exposition = []
        self.viewDT = True
        self.viewContourLines = True
        self.viewSlope = True
        self.viewExposition = True

    def _get_exposition_angle(self, exposition_class):
        angles = {
            "N": 0, "NE": pi/4, "E": pi/2, "SE": 3*pi/4, 
            "S": pi, "SW": 5*pi/4, "W": 3*pi/2, "NW": 7*pi/4
        }
        return angles[exposition_class]
    
    def mousePressEvent(self, e:QMouseEvent):
        #Get cursor position
        x = e.position().x()
        y = e.position().y()
        
        #Generate random height
        zmin = 150
        zmax = 400
        z = random() * (zmax - zmin) + zmin
        
        #Create new point
        p = QPoint3DF(x, y, z)

        #Add point to the point cloud
        self.points.append(p)

        #Repaint screen
        self.repaint()
        

    def paintEvent(self,  e:QPaintEvent):
        #Draw situation
        
        #Create new object
        qp = QPainter(self)

        #Start drawing
        qp.begin(self)
        
        if self.viewSlope:
            #Set graphic attributes
            qp.setPen(Qt.GlobalColor.gray)
      
            #Draw slope
            for t in self.dtm_slope:
                #Get slope
                slope = t.getSlope()
            
                #Convert slope to color
                mju = 2*255/pi
                col = int(255 - mju*slope)
                color = QColor(col, col, col)
                qp.setBrush(color)
            
                #Draw triangle
                qp.drawPolygon(t.getVertices())

        if self.viewExposition:
            exposition_classes = { 
                "N": QColor(0, 0, 255),   # North (Blue)
                "NE": QColor(0, 128, 255),  # Northeast (Light Blue)
                "E": QColor(0, 255, 0),    # East (Green)
                "SE": QColor(128, 255, 0),  # Southeast (Light Green)
                "S": QColor(255, 0, 0),    # South (Red)
                "SW": QColor(255, 128, 0),  # Southwest (Orange)
                "W": QColor(255, 255, 0),  # West (Yellow)
                "NW": QColor(128, 128, 128) # Northwest (Gray)
            }
            
            for t in self.dtm_exposition: 
                exposition = t.getExposition()  # Get the exposition of the triangle
                
                # Determine the closest exposition class (e.g., "N", "NE", etc.)
                exposition_class = min(exposition_classes.keys(), key=lambda x: abs(exposition - self._get_exposition_angle(x)))
                
                # Set the brush color to the corresponding exposition class color
                qp.setBrush(exposition_classes[exposition_class]) 

                # Draw the triangle
                qp.drawPolygon(t.getVertices())

            
        #DRAW DT
        if self.viewDT:     
            #Set graphic attributes
            qp.setPen(Qt.GlobalColor.green)
            qp.setBrush(Qt.GlobalColor.transparent)
            
            #Draw triangulation
            for e in self.dt:
                qp.drawLine(int(e.getStart().x()), int(e.getStart().y()), int(e.getEnd().x()), int(e.getEnd().y()))

        if self.viewContourLines:
            #Set graphic attributes
            qp.setPen(Qt.GlobalColor.gray)
            qp.setBrush(Qt.GlobalColor.yellow)
        
            #Draw contour lines
            for e in self.contours:
               qp.drawLine(int(e.getStart().x()), int(e.getStart().y()), int(e.getEnd().x()), int(e.getEnd().y()))
                 
            #Set graphic attributes
            qp.setPen(Qt.GlobalColor.black)
            qp.setBrush(Qt.GlobalColor.yellow)

        #Draw points
        r = 3
        for p in self.points:
            qp.drawEllipse(int(p.x()-r), int(p.y()-r), 2*r, 2*r)
       
    

        #End drawing
        qp.end()


    def loadData(self):
        """Loads data from a shapefile."""
        filename, _ = QFileDialog.getOpenFileName(self, "Open file", "", "Shapefile (*.shp)")
        if filename:
            shp = shapefile.Reader(filename)
            self.features = []
            self.min_max = [float('inf'), float('inf'), -float('inf'), -float('inf')]
            # calculate minimum and maximum coordinates
            min_x, min_y, max_x, max_y = float('inf'), float('inf'), -float('inf'), -float('inf')
            for feature in shp.shapes():
                print(feature)
                if feature.shapeType == shapefile.POINTZ:
                    x, y, z = feature.points[0][0], feature.points[0][1], feature.z[0]
                    x_min, y_min, x_max, y_max = self.min_max
                    # Update min/max for x and y
                    self.min_max[0] = min(x_min, x)
                    self.min_max[1] = min(y_min, y)
                    self.min_max[2] = max(x_max, x)
                    self.min_max[3] = max(y_max, y)
                    point = QPoint3DF(x, y, z)
                else:
                    print('feature is not a point!')
                # store not resized point in features   
                self.features.append(point)


    def resizeData(self):
        """Resizes data to fit imnto window size."""
        width = self.frameGeometry().width()
        height = self.frameGeometry().height()
        self.points = []  # List to store points
        for feature in self.features:
            x = int(((feature.x() - self.min_max[0]) / (self.min_max[2] - self.min_max[0]) * width))
            y = int((height - (feature.y() - self.min_max[1]) / (self.min_max[3] - self.min_max[1]) * height))
            z = feature.getZ()
            point = QPoint3DF(x, y, z)
            # Add point to the list
            self.points.append(point)


    def getPoints(self):
        # Return points
        return self.points
    
    def getDT(self):
        #Return DT
        return self.dt
    
    def clearAll(self):
        #Clear points
        self.points.clear()
        
        #Clear results
        self.clearResults()
        
        #Repaint screen
        self.repaint()
        
        
    def clearResults(self):
        #Clear DT
        self.dt.clear()
        
        #Clear contours
        self.contours.clear()

        #Clear slope
        self.dtm_slope.clear()
        
        #Clear aspect
        self.dtm_exposition.clear()
        
        #Repaint screen
        self.repaint()      
    
    
    def setDT(self, dt: list[Edge]):
        self.dt = dt
        
        
    def setContours(self, contours: list[Edge]):
        self.contours = contours


    def setDTMExposition(self, dtm_exposition: list[Triangle]):
        self.dtm_exposition = dtm_exposition    
        
    
    def setDTMSlope(self, dtm_slope: list[Triangle]):
        self.dtm_slope = dtm_slope
    
    
    def setViewDT(self, viewDT):
        self.viewDT = viewDT
        
        
    def setViewContourLines(self, viewContourLines):
        self.viewContourLines = viewContourLines
        
        
    def setViewSlope(self, viewSlope):
        self.viewSlope = viewSlope
        
        
    def setViewExposition(self, viewExposition):
        self.viewExposition = viewExposition