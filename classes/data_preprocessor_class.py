from classes.dataloader_class import DataLoader
import pandas as pd

class DataPreprocessor(DataLoader): # a DataPreprocessor class that extends DataLoader Class
    def inspect_data(self):#inspect data method to get overview of the loaded data
        if self.data is not None: #checking if the data is empty 
            print("\nData Overview:")
            print(self.data.info()) # if not empty display information about the data using builtin function info()
           
        else:
            print("Error! Data not loaded.")#in case data is not loaded

    def check_missing_values(self): #method to check if data has some missing values
        if self.data is not None:
            missing_values = self.data.isnull().sum() #calculating sum of missing values
            print("\nMissing Values:\n", missing_values)
            return missing_values #returning the sum of missing values
        else:
            print("Error! Data not loaded.")
            return pd.Series() #returns empty pandas series in case data is not loaded to avoid program tp crash

    def fill_missing_values(self): #method to apply data cleaning technique
        if self.data is not None:
            for column in self.data.columns: #looping through columns in the data
                if self.data[column].isnull().sum() > 0: #if the current column has some missing value 
                    if self.data[column].dtype == 'object': # check if the column type is text or categorical
                        mode_value = self.data[column].mode()[0]  #find the Mode i.e most frequent value
                        self.data[column] = self.data[column].fillna(mode_value) #fill that value in the missing column
                        print(f"Filled missing values in '{column}' with mode: {mode_value}") #display the message
                    else: #if the column type is numeric
                        mean_value = self.data[column].mean() #find mean of that column
                        self.data[column] = self.data[column].fillna(mean_value) #fill withh that mean value
                        print(f"Filled missing values in '{column}' with mean: {mean_value}") #display the message
        else:
            print("Error! Data not loaded.") #in case of failure
