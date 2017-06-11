import numpy as np 

class sandpile(object):
    
#***Threshold hardcoded as 4***
    
    def __init__(self, numEdgePoints, simSteps):
        self.numEdgePoints = numEdgePoints
        self.sandpileArray = np.zeros((self.numEdgePoints, self.numEdgePoints))
        self.avalancheHistory = np.zeros(simSteps)
        self.avalancheTime = np.zeros(simSteps)
        self.simSteps = simSteps
        
    def addSand(self, sandQty, locX, locY):
        self.sandpileArray[locX, locY] += sandQty
    
    
    def anyHigherThanThreshold(self):
        return (np.any(self.sandpileArray > 4))
        
            
    def findHighestPoint(self):
        row = int((np.argmax(self.sandpileArray)/np.size(self.sandpileArray,0)))
        col = np.argmax(self.sandpileArray) % np.size(self.sandpileArray,0)
        return row, col
    
    
    def redistributeSand(self, row, col):
        if self.sandpileArray[row, col] > 4:
            self.sandpileArray[row, col] -= 4
            self.sandpileArray[row + 1, col] += 1
            self.sandpileArray[row - 1, col] += 1
            self.sandpileArray[row, col + 1] += 1
            self.sandpileArray[row, col - 1] += 1
        
    
    def clearEdges(self):
        self.sandpileArray[:,0] = 0
        self.sandpileArray[:,-1] = 0
        self.sandpileArray[0,:] = 0
        self.sandpileArray[-1,:] = 0
        
        
    
        
