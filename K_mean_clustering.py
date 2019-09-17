import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets.samples_generator import make_blobs

class K_Means:
    
    def __init__(self, k=3, max_iterations = 500):
        self.k = k
        self.max_iterations = max_iterations
    
    def euclidean_distance(self, point1, point2):
        #return math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)   #sqrt((x1-x2)^2 + (y1-y2)^2)
        return np.linalg.norm(point1-point2, axis=0)
        
    def fit(self, data):
        
        #let the first K points from the dataset be the initial centroids
        self.centroids = {}
        for i in range(self.k):
            self.centroids[i] = data[i]
        
        #start K-Mean clustering
        for i in range(self.max_iterations):
            #create classifications the size of K
            self.classes = {}
            for j in range(self.k):
                self.classes[j] = []#empty them
                
            #find the distance between the points and the centroids
            for point in data:
                distances = []
                for index in self.centroids:
                    distances.append(self.euclidean_distance(point,self.centroids[index]))
                
                #find which cluster the datapoint belongs to by finding the minimum
                #ex: if distances are 2.03,1.04,5.6,1.05 then point belongs to cluster 1 (zero index)
                cluster_index = distances.index(min(distances))
                self.classes[cluster_index].append(point)
                
            #now that we have classified the datapoints into clusters, we need to again 
            #find new centroid by taking the centroid of the points in the cluster class
            for cluster_index in self.classes:
                self.centroids[cluster_index] = np.average(self.classes[cluster_index], axis = 0)
                

def main():
    
    #generate dummy cluster datasets
    K = 4
    X, y_true = make_blobs(n_samples=300, centers=K,
                           cluster_std=0.60, random_state=0)
    
    k_means = K_Means(K)
    k_means.fit(X)
    
    
    print(k_means.centroids)
    
    # Plotting starts here
    colors = 10*["r", "g", "c", "b", "k"]

    for centroid in k_means.centroids:
        plt.scatter(k_means.centroids[centroid][0], k_means.centroids[centroid][1], s = 130, marker = "x")

    for cluster_index in k_means.classes:
        color = colors[cluster_index]
        for features in k_means.classes[cluster_index]:
            plt.scatter(features[0], features[1], color = color,s = 30)
    
if __name__ == "__main__":
    main()