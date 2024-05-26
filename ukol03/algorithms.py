from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from math import *
from numpy import *
from scipy.linalg import *
from qpoint3df import *
from edge import *
from triangle import *

#Processing data
class Algorithms:
    
    def __init__(self):
        pass
        
    def get2LineAngle(self, p1:QPointF, p2:QPointF, p3:QPointF, p4:QPointF):
                
        #Get 2 line angle
        ux = p2.x() - p1.x()
        uy = p2.y() - p1.y() 
        
        vx = p4.x() - p3.x()
        vy = p4.y() - p3.y()         
        
        #Dot product
        dot = ux * vx + uy * vy  
        
        #Vector norms
        nu = (ux**2 + uy**2)**(1/2)
        nv = (vx**2 + vy**2)**(1/2)
        
        #Correct interval
        arg = dot/(nu*nv)
        
        return acos(max(min(arg, 1), -1))
        
   
    def getPointAndLinePosition(self, p: QPoint3DF, p1: QPoint3DF, p2: QPoint3DF): 
        # Analyze point and line position
        ux = p2.x() - p1.x()
        uy = p2.y() - p1.y()
        
        vx = p.x() - p1.x()
        vy = p.y() - p1.y()
        
        #Compute test
        t = ux*vy - uy*vx
        
        #Point in the left half plane
        if t > 0:
            return 1
        
        #Point in the right half plane
        if t < 0:
            return 0
        
        #Point on the line
        return -1
    
        
    def getNearestPoint(self, q:QPoint3DF, points:list[QPoint3DF]):
        #Find point nearest to q
        p_nearest = None
        dist_nearest = inf
        
        #Process all points
        for p in points:
            #Point p differente from q
            if p!=q:
                #Compute distance
                dx = p.x() - q.x()
                dy = p.y() - q.y()
                
                dist = sqrt(dx**2 + dy**2)
                
                #Update nearest point
                if dist < dist_nearest:
                    p_nearest = p
                    dist_nearest = dist
        
        return p_nearest
        
                
    def getDelaunayPoint(self, start:QPoint3DF,end:QPoint3DF, points:list[QPoint3DF]):
        #Find Delaunay point to an edge
        p_dt = None
        angle_max = 0   
             
        #Process all points
        for p in points:
            
            #Point p differente from q
            if start != p and end != p:
                
                #Point in the left halfplane
                if self.getPointAndLinePosition(p, start, end) == 1:
                    
                    #Compute angle
                    angle = self.get2LineAngle(p, start, p, end)
                
                    # Update maximum
                    if angle > angle_max:
                        angle_max = angle
                        p_dt = p
                
        return p_dt
    
    
    def updateAEL (self, e: Edge, ael: list[Edge]):
        #Update active edges list
        e_op = e.changeOrientation()
        
        #Is edge in ael?
        if e_op in ael:
            #Remove edge
            ael.remove(e_op)
            
        #Add edge to ael    
        else:
            ael.append(e)
                
                
    def createDT(self, points: list[QPoint3DF]):
        #Create Delaunay triangulation with incremental method
        dt = []
        ael = []

        #Sort points by x
        p1 = min(points, key = lambda k: k.x() )
        
        #Find nearest point
        p2 = self.getNearestPoint(p1, points)
        
        #Create edges
        e = Edge(p1, p2)
        e_op = Edge(p2, p1)
        
        #Add both edges to ael
        ael.append(e)
        ael.append(e_op)
        
        # Repeat until ael is empty
        while ael:
            # Take first edge
            e1 = ael.pop()
            
            #Change orientation
            e1_op = e1.changeOrientation()
            
            #Find optimal Delaunay point
            p_dt = self.getDelaunayPoint(e1_op.getStart(), e1_op.getEnd(), points)

            #Did we find a suitable point?
            if p_dt != None:
                #create remaining edges
                e2 = Edge(e1_op.getEnd(), p_dt)
                e3 = Edge(p_dt, e1_op.getStart())
                
                #Create Delaunay triangle
                dt.append(e1_op)
                dt.append(e2)
                dt.append(e3)
                
                #Update AEL
                self.updateAEL(e2, ael)
                self.updateAEL(e3, ael)
                
        return dt
    
    
    def getContourPoint(self, p1:QPoint3DF, p2:QPoint3DF, z:float):
        #Intersection of triangle and horizontal plane
        xb = (p2.x() - p1.x())/(p2.getZ()-p1.getZ()) * (z-p1.getZ()) + p1.x()
        yb = (p2.y() - p1.y())/(p2.getZ()-p1.getZ()) * (z-p1.getZ()) + p1.y()
        
        return QPoint3DF(xb, yb, z)
    
    
    def createContourLines(self, dt, zmin, zmax, dz):
        #Create contour lines defined by interval and step
        contours = []
                
        #Process all triangles
        for i in range(0, len(dt), 3):
            #Get vertices of triangle
            p1 = dt[i].getStart()
            p2 = dt[i].getEnd()
            p3 = dt[i + 1].getEnd()
            
            #Get z coordiantes
            z1 = p1.getZ()
            z2 = p2.getZ()
            z3 = p3.getZ()
            
            #Create all contour lines
            for z in arange(zmin, zmax, dz):
                
                #Compute edge height differences
                dz1 = z - z1
                dz2 = z - z2
                dz3 = z - z3
                
                #skip coplanar triangle
                if dz1 == 0 and dz2 == 0 and dz3 == 0:
                    continue
                
                #Edge p1 and p2 is colinear
                elif dz1 ==0 and dz2 ==0:
                    contours.append(dt[i])
                
                #Edge p2 and p3 is colinear
                elif dz2 ==0 and dz3==0:
                    contours.append(dt[i+1]) 
                
                #Edge p3 and p1 is colinear
                elif dz3 ==0 and dz1==0:
                    contours.append(dt[i+2]) 
                    
                
                #Edges p1, p2 and p2, p3 intersected by plane
                elif dz1 * dz2 <= 0 and dz2 * dz3 <= 0:
                    
                    #Compute intersections
                    a = self.getContourPoint(p1, p2, z)
                    b = self.getContourPoint(p2, p3, z)
                    
                    #Create edge
                    e1 = Edge(a, b)
                    
                    #Add edge to contour lines
                    contours.append(e1)
                
                #Edges p2, p3 and p3, p1 intersected by plane
                elif dz2 * dz3 <= 0 and dz3 * dz1 <= 0:
                    
                    #Compute intersections
                    a = self.getContourPoint(p2, p3, z)
                    b = self.getContourPoint(p3, p1, z)
                    
                    #Create edge
                    e1 = Edge(a, b)
                    
                    #Add edge to contour lines
                    contours.append(e1)
                
                #Edges p3, p1 and p1, p2 intersected by plane
                elif dz3 * dz1 <= 0 and dz1 * dz2 <= 0:
                    
                    #Compute intersections
                    a = self.getContourPoint(p3, p1, z)
                    b = self.getContourPoint(p1, p2, z)
                    
                    #Create edge
                    e1 = Edge(a, b)
                    
                    #Add edge to contour lines
                    contours.append(e1)
                
        return contours
    
    
    def computeSlope(self, p1:QPoint3DF, p2:QPoint3DF, p3:QPoint3DF):
        #Compute triangle slope
        
        #Directions
        ux = p1.x() - p2.x() 
        uy = p1.y() - p2.y() 
        uz = p1.getZ() - p2.getZ()        
        
        vx = p3.x() - p2.x() 
        vy = p3.y() - p2.y() 
        vz = p3.getZ() - p2.getZ()        
        
        #Normal vector     
        nx = uy * vz - vy * uz
        ny = - (ux*vz - vx * uz)
        nz = ux * vy - vx * uy
        
        #Norm
        norm = (nx**2 +ny**2 + nz**2)**(1/2)

        return acos(abs(nz)/norm)        
        
        
    def computeExposition(self, p1:QPoint3DF, p2:QPoint3DF, p3:QPoint3DF):
        #Compute triangle exposition
        
        #Directions
        ux = p1.x() - p2.x() 
        uy = p1.y() - p2.y() 
        uz = p1.getZ() - p2.getZ()        
        
        vx = p3.x() - p2.x() 
        vy = p3.y() - p2.y() 
        vz = p3.getZ() - p2.getZ()        
        
        #Normal vector     
        nx = uy * vz - vy * uz
        ny = - (ux*vz - vx * uz)

        # exposition
        exposition = atan2(nx, ny)
        if exposition < 0:
            return exposition + 2*pi
        return exposition     
                
                
    
    def analyzeDTMSlope(self, dt:list [Edge]):
        #analyze dtm slope 
        dtm_slope: list [Triangle] = []    
        
        #Process all triangles
        for i in range(0, len(dt), 3):
            #Get vertices of triangle
            p1 = dt[i].getStart()
            p2 = dt[i].getEnd()
            p3 = dt[i + 1].getEnd()
            
            #Get slope
            slope = self.computeSlope(p1, p2, p3)
            
            #Create triangle
            triangle = Triangle(p1, p2, p3, slope, 0)
            
            #Add triangle to the list
            dtm_slope.append(triangle)
            
        return dtm_slope
    
    
    def analyzeDTMExposition(self, dt:list [Edge]):
        #analyze dtm exposition 
        dtm_exposition: list [Triangle] = []    
        
        #Process all triangles
        for i in range(0, len(dt), 3):
            #Get vertices of triangle
            p1 = dt[i].getStart()
            p2 = dt[i].getEnd()
            p3 = dt[i + 1].getEnd()
            
            #Get exposition
            exposition = self.computeExposition(p1, p2, p3)
            
            #Create triangle
            triangle = Triangle(p1, p2, p3, 0, exposition)
            
            #Add triangle to the list
            dtm_exposition.append(triangle)
            
        return dtm_exposition
                