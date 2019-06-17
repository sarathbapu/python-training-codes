# -*- coding: utf-8 -*-
'''
Defines a new class point which can be used to find the distance between two points.

A square is characterised by the following properties
1. All sides are equal
2. All diagonals are equal
3. 2 sides are at right angle. (Checked using Pythagoras theorem)

'''
import math 

'''
Class point
'''
class Point :
    ''' 
    Initialising an instance of point
    '''
    def __init__(self, x, y) :
        self.x = x
        self.y = y
    '''
    Shortest distance between this point and new point
    '''
    def distance(self, point1) :
        return math.sqrt(((self.x - point1.x) ** 2 )+((self.y - point1.y) ** 2))
    '''
    Returns square of shortest distance between points
    '''
    def distanceSquare(self, point) :
        return ((self.x - point.x)**2) + ((self.y - point.y)**2)

def checkSquare(p1, p2, p3, p4):
    
    return (checkSides(p1, p2, p3, p4) and checkDiagonals(p1, p2, p3, p4) 
            and checkRightAngles(p1, p2, p3, p4))

def checkSides(p1, p2, p3, p4) :
    side = p1.distance(p2)
    return side == p2.distance(p3) and side == p3.distance(p4) and side == p4.distance(p1)
    
def checkDiagonals(p1, p2, p3, p4) :
    return p1.distance(p3) == p2.distance(p4)
    
def checkRightAngles(p1, p2, p3, p4):
    return (p1.distanceSquare(p3) == 2 * p1.distanceSquare(p2) 
            and p2.distanceSquare(p4) == 2 * p1.distanceSquare(p2))
    
# Driver program
print("Yes" if checkSquare(Point(20, 10), Point(20, 20), Point(10, 20), 
                           Point(10, 10)) else "No")
