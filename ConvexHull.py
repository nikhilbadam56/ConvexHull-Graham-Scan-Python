
# CONVEX HULL IMPLEMENTATION USING GRAHAM SCAN ALGORITHM.
# APPLICATION :
# SELF DRIVING CARS(COLLISION AVOIDANCE),OBJECT TRACKING , EPIDEMIC SPREAD EXTENT , CALCULATING THE AREA OF CONTAINMENT ZONE TO MITIGATE PANDEMICS 
# , IMAGE PROCESSING , PACKAGING ETC.
#
 
import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib
class Hull:
    def __init__(self):
        self.points = [] #GRAPH POINTS
        self.stack = [] #MAINTING A STACK OF EXPLORED POINTS SATISFYING THE CCW CONDITION 
    
    def insert(self,point):
        #INSERTING THE POINTS 
        if not point is None:
            self.points.append(point)

    def sort(self):
        #THIS FUNCTION SORTS THE POINTS FIRST , BASED ON THE Y COORDINATE OF POINTS AND THEN BASED ON THE POLAR ANGLE MADE BY EVERY OTHER POINT
        #WITH THE POINT WITH LOWEST Y COORDINATE .
        def fun(x): 
            return x[1]
        ar = sorted(self.points,key=fun)
        start = ar[0] #POINT WITH LOWEST Y COORDINATE POINT
        def fun2(x):
            return self.slope(start,x) #CALCULATING THE POLAR ANGLE OF REST OF POINT WITH RESPECT TO THE POINT WITH LOWEST Y COORDINATE
        return sorted(ar[1:],key=fun2),start

    def slope(self,point1,point2):
        return math.atan2((point2[1] - point1[1]),(point2[0] - point1[0])) #POLAR SLOPE OF THE POINTS
    def calc_slope_btw_last_three_points(self):

        #CALCULATING THE RELATIVE CCW ROTATION EXTENT
        length = len(self.stack)-1
        p = self.stack[length-2]
        q = self.stack[length-1]
        r = self.stack[length]
        return (q[1] - p[1])*(r[0] - q[0]) - (r[1] - q[1])*(q[0] - p[0])
        # return self.slope(self.stack[length-2],self.stack[length-1]) - self.slope(self.stack[length-1],self.stack[length])
    
    def hull(self):
        #MAIN FUNCTION
        sorted_array,start =self.sort() 
        self.stack.append(start) #APPENDING THE START POINT INTO STACK
        for i in range(0,len(sorted_array)): #ITERATING OVER THE POINTS 
            self.stack.append(sorted_array[i])
            # print(self.stack)
            while len(self.stack)>2 and not self.calc_slope_btw_last_three_points()<0: #CONTINUOUSLY ASSESING THE STACK POINTS FOR THE CCW ROTATION IF NOT DROPPING THE POINTS
                del self.stack[-2]
            yield self.stack #USED FOR ANIMATING DISPLAY USING MATPLOTLIB

    def animate(self,i):
        #FUNCTION FOR PLOTTING THE AS ALGORITHM INPUTS POINTS INTO STACK.

        plt.cla() #CLEARING THE PLOT EACH TIME SO AS TO CREATE A ANIMATING APPEAL

        plt.plot(np.array(self.points)[:,0],np.array(self.points)[:,1],'o') #PLOTTING THE GRAPH POINTS

        plt.plot(np.array(self.stack)[:,0],np.array(self.stack)[:,1],'k-') #PLOTTING THE LINE THROUGH THE POINTS IN THE STACK

        plt.title("Grapham Scan Algorithm , For Convex Hull") #TITLE

    def __str__(self):
        string = ""
        for i in self.stack:
            string+=str('('+str(i[0])+' '+str(i[1])+')')
        return string

hull = Hull()
points = np.random.rand(50, 2) #GENERATING SOME RANDOM DATA POINTS TO SURROUND THEM WITH CONVEX HULL

#INITIAL DATA USED FOR TESTING THE ALGORITHM PERFORMANCE

# points = [[0, 3], [1, 1], [2, 2], [4, 4], [0, 0], [1, 2], [3, 1], [3, 3]]

for i in points:
    hull.insert(i)#INSERTING THE DATA INTO CLASS'S POINTS LIST

ani = matplotlib.animation.FuncAnimation(plt.gcf(),hull.animate,hull.hull) #MATPLOTLIB FUNCTION USED FOR ANIMATING THE PLOTS.

plt.show()