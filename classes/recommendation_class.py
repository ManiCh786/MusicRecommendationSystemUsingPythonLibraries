
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances

import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
import numpy as np
class RecommendationSystem:
    def __init__(self, data):
        self.data = data

    def compute_similarity(self, features, metric='cosine'):  #computing similarity using cosine and euclidean 
        if metric == 'cosine':
            #higher similarity means more similar
            return cosine_similarity(features) #using cosine similarity function from sklearn library
        #higher similarity means less similar
        elif metric == 'euclidean':
            return -euclidean_distances(features)  # Inversing it to make it high value more similar
        else:
            raise ValueError("Unsupported similarity metric.") #exception

    def recommend(self, similarity_matrix, item_index, top_n=5):
        similar_items = np.argsort(-similarity_matrix[item_index])[:top_n + 1] #returns the indices of the sorted array,the negative sign means that higher similarity values come first
        similar_items = similar_items[1:]  # Exclude the item itself
        return self.data.iloc[similar_items] #return the data of the most similar

    def evaluate_metrics(self, X, y, metrics=['cosine', 'euclidean']):
        results = {} #initialize the empty dictionary to store results later 
        for metric in metrics: #looping through each metric
            similarity_matrix = self.compute_similarity(X, metric) #computing similarity using each metric
            y_pred = np.argmax(similarity_matrix, axis=1)#calculating prediction
            accuracy = accuracy_score(y, y_pred)
            results[metric] = accuracy
            print(f"Accuracy for {metric}: {accuracy}")
        return results

    def plot_metrics_comparison(self, results):
        plt.figure(figsize=(8, 6))
        plt.bar(results.keys(), results.values())
        plt.title("Accuracy Comparison of Similarity Metrics")
        plt.xlabel("Similarity Metric")
        plt.ylabel("Accuracy")
        plt.show()
