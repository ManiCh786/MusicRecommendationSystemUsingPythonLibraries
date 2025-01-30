from classes.data_preprocessor_class import DataPreprocessor
from classes.eda import EDA
from classes.recommendation_class import RecommendationSystem
def main():
    file_path = "dataset/data1.csv" #dataset file path
    preprocessor = DataPreprocessor(file_path) #calling DataPreprocessor Class
    preprocessor.load_data() #calling the method 

    if preprocessor.data is not None:
        # Inspect and Clean Data
        preprocessor.inspect_data()
        preprocessor.check_missing_values()
        preprocessor.fill_missing_values()  # Fills missing values

    
        eda = EDA(preprocessor.data)
        eda.compute_statistics()  # This includes skewness, kurtosis, variance, and median
        #visualization
       


        # eda.plot_distributions('popularity')  
        # eda.plot_relationships('danceability', 'energy')  

        # eda.plot_grouped_bar('energy', 'popularity')  
        

        # eda.plot_grouped_bar('year', 'popularity')

        # eda.plot_pie_chart('mode')
        # eda.plot_pie_chart('popularity_level')
        # # Correlation Heatmap
        eda.plot_correlation_heatmap()

        recommendation_system = RecommendationSystem(preprocessor.data)
        features = preprocessor.data.select_dtypes(include=['float64', 'int64']).values
        similarity_matrix = recommendation_system.compute_similarity(features,metric='cosine')
        recommendations = recommendation_system.recommend(similarity_matrix, item_index=0, top_n=5)
        print("Recommendations:\n", recommendations)

main()
