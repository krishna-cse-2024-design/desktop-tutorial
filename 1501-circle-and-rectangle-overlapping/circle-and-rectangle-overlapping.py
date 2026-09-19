class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        #lets bring the circle's centre to 0,0
        x1, y1, x2, y2  = x1 - xCenter,y1-yCenter, x2 - xCenter, y2-yCenter
        xCenter, yCenter = 0, 0
        
        #finding nearest point of rectangle from 0,0
        #if ract lies in any quadrant then it will be on vertex/corner
        #if rect lies in two quadrant i.e. it instersects X or Y axis them the nearest point will be on the edges
        nearest_X = float("inf")
        nearest_Y = float("inf")
        if x1<0 and x2>0:
            if y1<0 and y2>0:
                return True
            nearest_X = 0
            nearest_Y=y2 if abs(y1)>abs(y2) else y1
        elif y1<0 and y2>0:
            nearest_X = x1 if abs(x1)<abs(x2) else x2
            nearest_Y= 0
        else:
            nearest_X = x1 if abs(x1)<abs(x2) else x2
            nearest_Y = y1 if abs(y1)<abs(y2) else y2
        
        #finding dist from centre
        dist = ((nearest_X*nearest_X)+(nearest_Y*nearest_Y))**0.5

        return dist<=radius