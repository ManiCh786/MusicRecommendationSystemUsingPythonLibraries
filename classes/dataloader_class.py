import pandas as pd #pandas library to load and extract csv
class DataLoader: #Data Loader Class including method to load data which will load csv file and read
    def __init__(self, file_path):#constructor of the class
        self.file_path = file_path #variable to set file path
        self.data = None # declaring empty variable to store data when file is read

    def load_data(self): #method to load data
        try: #try catch to avoid program to crash in case of file loading error
            self.data = pd.read_csv(self.file_path) #reading csv of the given file path 
            print(f"Data loaded successfully from {self.file_path}") #printing success message
        except Exception as e:
            print(f"Error loading data: {e}") #in case of Exception
