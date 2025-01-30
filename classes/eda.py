

import matplotlib.pyplot as plt #using this library to show plots,graph etc
import pandas as pd
import seaborn as sns
class EDA: #exploratory Data analysis class
    def __init__(self, data):
        self.data = data

    def compute_statistics(self): #compute Statistics function to compute skew,kurt etc
        if self.data is not None:
            
            numeric_data = self.data.select_dtypes(include=['float64', 'int64'])# Filter out non numeric columns 
            if not numeric_data.empty: #if it is nor empty
                print("\nDescriptive Statistics (Numeric Data Only):")
                print(numeric_data.describe()) # details about the data after removing non-numeric vlaues
                
               #calculating stats using python libraries builtin functions
                skewness = numeric_data.skew()
                kurtosis = numeric_data.kurt()
                variance = numeric_data.var()
                median = numeric_data.median()

                # DPrinting the results
                print("\nAdditional Statistics (Numeric Data Only):")
                print(f"Skewness:\n{skewness}")
                print(f"Kurtosis:\n{kurtosis}")
                print(f"Variance:\n{variance}")
                print(f"Median:\n{median}")
            else:
                print("No numeric data available for statistical analysis.") #in case the data numeric data is empty
        else:
            print("Error! Data not loaded.")#exception

    def plot_distributions(self, column_name): #visualizing the column given using a histogram
        if column_name in self.data.columns:  #check of the column exits 
            plt.figure(figsize=(8, 6))# create a fig or 8*6 in
            sns.histplot(self.data[column_name], kde=True) #create a histogram of te column with a kernel density estimate (KDE)
            plt.title(f'Distribution of {column_name}') #title of the histogram
            plt.show() #display the histogram

    def plot_relationships(self, x_col, y_col): #visualizing relationship between two columns
        if x_col in self.data.columns and y_col in self.data.columns: #check if the columns exits 
            plt.figure(figsize=(8, 6)) #create a fig of 8 * 6 in
            sns.scatterplot(x=self.data[x_col], y=self.data[y_col]) #create a scatter plot with x and y axis 
            plt.title(f'Relationship between {x_col} and {y_col}') #title of the diagram
            plt.show() #show the diagram


    def plot_grouped_bar(self, categorical_column, numerical_column, max_categories=10): #create a grouped bar plot with categorical(x-axis) and numeric(y-axis) column 
    
        if categorical_column in self.data.columns and numerical_column in self.data.columns: #check if both columns exits 
            # Aggregate categories
            grouped_data = self.data.groupby(categorical_column)[numerical_column].mean().sort_values(ascending=False)#Group by the categorical column and calculate the mean of the numerical column, then sort in descending order
            
            top_categories = grouped_data.head(max_categories) #Select the top 10 categories based on the mean value
            others = grouped_data.iloc[max_categories:].mean() # Calculate the mean for all remaining categories
            
            # Add "Others" category if no of categories are more than 10
            if len(grouped_data) > max_categories:
                top_categories["Others"] = others
            
            # Convert to a DataFrame for plotting
            plot_data = top_categories.reset_index()
            plot_data.columns = [categorical_column, numerical_column]#column names

            # Plot
            plt.figure(figsize=(10, 6))  # create a fig 
            sns.barplot(data=plot_data, x=numerical_column, y=categorical_column, palette="viridis",hue=categorical_column, dodge=False, legend=False)  #creating a bar plot  
            plt.title(f'Top {max_categories} Categories: {numerical_column} by {categorical_column}') #title of the graph
            plt.xlabel(numerical_column.capitalize()) #label of the x-axis
            plt.ylabel(categorical_column.capitalize()) #label of the y-axis
            plt.tight_layout() # Adjust layout to prevent overlapping
            plt.show()
        else:
            print(f"Columns '{categorical_column}' or '{numerical_column}' are not present in the dataset.")

    # Pie Chart
    def plot_pie_chart(self, categorical_column): #generating Pie Chart
        if categorical_column in self.data.columns: #check if column is present in the data
            data_counts = self.data[categorical_column].value_counts()
            plt.figure(figsize=(8, 6)) #create a fig of 8,6 in
            data_counts.plot.pie(autopct='%1.1f%%', startangle=90, cmap='Set3') #genreate pie chart,autopct shows the percentage of each cateory with one value after decimal point ,cmap is the colour pallete
            plt.title(f'Pie Chart of {categorical_column}') #title
            #Remove the label for the y-axis  because pie charts don't have a y-axis
            plt.ylabel('')
            plt.show()#show
        elif categorical_column == 'popularity_level':
            if self.data['popularity'].isnull().any():
                raise ValueError("The popularity column contains null values.")

            data_counts = pd.cut(
                self.data['popularity'],
                bins=[0, 30, 60, 100],  # Define bins for Low, Medium, High
                labels=['Low(0-30)', 'Medium(30-60)', 'High(60-100)'],  # Assign labels for the bins
                include_lowest=True  # Include the lowest value in the first bin
            )

            # Check if any values fall outside the bins
            if data_counts.isnull().any():
                raise ValueError("Some values in the 'popularity' column are outside the defined bins. Adjust the bins as needed.")

            # Create a pie chart
            plt.figure(figsize=(8, 6))  # Create a figure with size 8x6 inches
            data_counts.value_counts().plot.pie(
                autopct='%1.1f%%',  # Show percentage with one decimal point
                startangle=90,  # Start the chart at 90 degrees
                cmap='Set3'  # Use a color palette
            )
            plt.title(f'Pie Chart of {categorical_column}')  # Add a title
            plt.ylabel('')  # Remove y-axis label
            plt.show()  # Display the chart
                
    def plot_box_plot(self, categorical_column, numerical_column):
        if categorical_column in self.data.columns and numerical_column in self.data.columns: #check if bpth columns exits
            plt.figure(figsize=(8, 6))
            sns.boxplot(x=self.data[categorical_column], y=self.data[numerical_column])# Generate a box plot to visualize the distribution of the numerical column
                                                                                        # with respect to the categories in the categorical column
            plt.title(f'Box Plot: {numerical_column} by {categorical_column}')
            plt.xticks(rotation=45) #rotate by 45 degree for better readability
            plt.show()
        else: #exception
            print(f"Columns '{categorical_column}' or '{numerical_column}' are not present in the dataset.")

    def plot_correlation_heatmap(self):
        if self.data is not None: #if the dataset is not empty 
            numeric_data = self.data.select_dtypes(include=['float64', 'int64']) #select only the numeric
            plt.figure(figsize=(10, 8)) 
            sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm', fmt='.2f')#generate a heatmap,corr() computes pairwise correlation,cmap is the colour pallete, and fmt is value format upto 2 decimals
            plt.title('Correlation Heatmap') #title
            plt.show()
        else:#exception
            print("Error! Data not loaded.")
