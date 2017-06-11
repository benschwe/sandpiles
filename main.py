import sandpileClass
import numpy as np
from matplotlib import pyplot as plt
import time

#%%
# Set up piles
sandpiles = {}
simSteps = 50000
sandpiles['small'] = sandpileClass.sandpile(50, simSteps)
sandpiles['med'] = sandpileClass.sandpile(100, simSteps)
#sandpiles['large'] = sandpileClass.sandpile(300, simSteps)

#%%
# Main loop

for size in sandpiles.keys():
    step = 0
    print 'Working on {} pile'.format(size)
    
    while step < sandpiles[size].simSteps:
        
        sandpiles[size].addSand(1, sandpiles[size].numEdgePoints/2, 
                                sandpiles[size].numEdgePoints/2)
    
        start = time.time()
        if sandpiles[size].anyHigherThanThreshold(): 
            
            avalancheLength = 0
            
            while sandpiles[size].anyHigherThanThreshold():
                row, col = sandpiles[size].findHighestPoint()
                sandpiles[size].redistributeSand(row, col)
                sandpiles[size].clearEdges()
                avalancheLength += 1
                
            sandpiles[size].avalancheHistory[step] = avalancheLength
        end = time.time()
        
        sandpiles[size].avalancheTime[step] = end - start
        step += 1  
        
        if step % 500 == 0:
            print '{}% complete'.format(100.0*(step/float(sandpiles[size].simSteps)))
            print 'Elapsed time for last 500 steps: {}'.format(np.sum(sandpiles[size].avalancheTime
                                                               [step - 500:step]))
            
    sandpiles[size].hist = (np.histogram(sandpiles[size].avalancheHistory
                            [sandpiles[size].avalancheHistory > 0], 50))

#%%
# Plotting
for size in sandpiles.keys():
    plt.figure(1)
    plt.loglog(sandpiles[size].hist[0], sandpiles[size].hist[1][1:], 
               linestyle = 'None', marker = '.', markersize = 10, label = size)
    plt.grid(which = 'both')
    plt.xlabel('Size of avalanche')
    plt.ylabel('# of avalanches')
    plt.legend()
    
    plt.figure(2)
    plt.plot(np.arange(0,sandpiles[size].simSteps, 1), 
             sandpiles[size].avalancheHistory, label = size)
    plt.legend()
    
    



    