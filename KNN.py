
"""KNN implemantation using Euclidean distance"""

import math
import numpy as np

def Euclidean_distance(point,dataset):
  
  distance=[]
  o_index=0
  for data in dataset:
    index=0
    cost=0;
    for dimension in point:
      
      cost=cost+math.sqrt(((data[index]-dimension)**2))
      index=index+1;
      
    distance.append(cost)
    
  return distance
    
'''data=[[5,2],[3,2],[2,2],[1,2],[3,2],[5,2]]
associate=[5,3,2,2,3,5]'''

dist=Euclidean_distance([5,2],data)

dist.sort()

prediction=0
for value in range(0,3):
  """You can code here as par your requirements"""