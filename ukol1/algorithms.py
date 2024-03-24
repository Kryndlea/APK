from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from math import sqrt, acos, pi


#processing data
class Algorithms:
    
    def __init__(self):
        pass
    
    # Ray crossing algorithm for multiple polygons
    def rayCrossingPols(self, q : QPointF, polygons):
        results = []
        for pol in polygons:
            res = self.rayCrossing(q, pol)
            results.append(res)
        return results
    
    # Winding number algorithm for multiple polygons
    def windingNumberPols(self, q : QPointF, polygons):
        results = []
        for pol in polygons:
            res = self.windingNumber(q, pol)
            results.append(res)
        return results
                
    # Ray crossing algorithm for one polygon
    def rayCrossing(self, q:QPoint, pol:QPolygonF):
        
        # initialize the number of left and right intersections and number of vertices
        kl = 0
        kr = 0
        n = len(pol)
        
        # process all vertices
        for i in range(n):
            
            # reduce coordinates
            xir = pol[i].x() - q.x()
            yir = pol[i].y() - q.y()
            
            # reduce coordinates of the next vertex
            xi1r = pol[(i+1)%n].x() - q.x()
            yi1r = pol[(i+1)%n].y() - q.y()
            
            # check if the point is located on a vertex
            if (xir == 0) and (yir == 0):
                return -1

            # check for horizontal edge
            if (yi1r - yir) == 0:
                continue
            # compute intersection of ray and edge
            xm = (xi1r * yir - xir * yi1r) / (yi1r - yir)
               
            # process lower segment  
            if (yi1r < 0) != (yir < 0): 
               
                # if the point is suitable, intersection is on the left side
                if xm < 0:
                    kl += 1
            # process upper segment
            if (yi1r > 0) != (yir > 0):
                # if the point is suitable, intersection is on the right side
                if xm > 0:
                    kr += 1
                        
        # check if point is on the edge
        if (kl % 2) != (kr % 2):
            return -1
                    
        # check if the point is inside the polygon
        elif (kr % 2 == 1):
            return 1

        # point is outside the polygon
        return 0
    
           
    # Winding number algorithm for one polygon
    def windingNumber(self, q:QPoint, pol:QPolygonF):
        
       # initialize the winding number, the number of vertices and tolerance
        wn_total = 0
        n = len(pol)
        epsilon = 1.0e-10
        
        # process all vertices
        for i in range(n):
            # check if the point is located on a vertex
            if (pol[i].x() == q.x()) and (pol[i].y() == q.y()):
                return -1
            
            # compute vectors
            v1 = pol[i].x() - q.x(), pol[i].y() - q.y()
            v2 = pol[(i+1)%n].x() - q.x(), pol[(i+1)%n].y() - q.y()
        
            # compute the determinant and scalar product
            det = v1[0] * v2[1] - v1[1] * v2[0]
            scalar = v1[0] * v2[0] + v1[1] * v2[1]
            
            # compute the distance between the point and the vertices of the edge
            dis = sqrt((v1[0]**2 + v1[1]**2) * (v2[0]**2 + v2[1]**2))
            # if distance is zero, the point is on the edge
            if dis == 0:
                return -1
            
            # compute the angle between the point and the vertices of the edge
            wn = scalar / dis
            wn = acos(wn)
            
            # Determine wheter to add or subtract the angle
            if det > 0:
                wn_total += wn
            elif det < 0:
                wn_total -= wn
            
            # check if the point is on the edge
            if det == 0 and abs(wn - pi) < epsilon:
                return -1
                
        # check if the point is inside the polygon
        if abs(abs(wn_total) - 2 * pi) < epsilon:
            return 1
        # point is outside the polygon
        else:
            return 0
        
        
            
               