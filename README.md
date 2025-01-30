
Sheffield Hallam University

Music Data Analytics

An intelligent service recommendation engine

Abdur Rehman
  34039009


 
Introduction:
The goal of this project is to conduct exploratory data analysis (EDA) on online content streaming company’s dataset to uncover insights into song characteristics such as popularity, energy, danceability, and more. The dataset consists of various musical features such as energy, danceability, causticness, loudness, and popularity, which can be used to examine patterns and relationships between these attributes.
In this report, I will explain the methods used to process and analyze the data, present the results of various visualizations, and provide reflections on the challenges and learnings from the project. The analysis was carried out using Python, leveraging libraries such as pandas, matplotlib, seaborn, and plotly for data manipulation and visualization. This report covers the steps taken in processing the dataset, the visualizations created, and the insights gained.
________________________________________
Implementation Decisions and Justifications
1.	Data Cleaning and Preprocessing:
o	Handling Missing Values: It was crucial to ensure the dataset had no missing values, as missing values could skew results. I used pandas to check for missing data and remove or replace the missing values accordingly.
•	Column Selection: Given the available features in the dataset, I decided to focus on the following key columns: popularity, energy, danceability, acousticness, valence, and explicit. These features were chosen due to their direct relevance to understanding a song's appeal and their compatibility for statistical analysis, and they are all numerical or categorical in nature, suitable for various statistical analyses.
2. Feature Extraction and Justification
The key features chosen for analysis in this report include:
1.	Popularity:
o	Justification: Popularity is the most direct indicator of a song's success. It's essential for understanding the success of a song on platforms like Spotify, and it's often the target variable when analyzing trends in music.
2.	Energy:
o	Justification: Energy reflects the intensity of a song, which can directly impact listener engagement, especially for songs that are meant for dancing or high-energy activities. It's a crucial feature for predicting a song's popularity, as higher energy songs tend to perform better.
3.	Danceability:
o	Justification: Danceability describes how suitable a song is for dancing, and it often correlates with higher engagement levels. More danceable songs typically have more listeners in specific demographics.
4.	Acousticness:
o	Justification: Acousticness reflects the level of natural sounds in a song. High acousticness could appeal to different listener bases, such as those who prefer folk or classical music, and may influence its popularity within these subgenres.
5.	Valence:
o	Justification: Valence indicates the emotional tone of a song, whether it's positive or negative. Since people tend to prefer more positive music, valence is an important feature for understanding the emotional impact of a song and its potential popularity.
These features were chosen because they offer insights into the song’s mood, energy, listener engagement, and overall appeal, making them ideal candidates for analysis.
________________________________________
2.	Exploratory Data Analysis and Visualization:
o	Distribution Plots: I used distribution plots for the popularity column to understand the effect of popularity scores among songs. This helped identify whether most songs have a high or low popularity.
o	Scatter Plots for Relationships: I used Scatter Plots to explore relationships between variables such as energy and danceability, as both attributes are likely to influence how listeners perceive the song's overall vibe.
o	Grouped Bar Plots: To understand the relationship between energy and popularity, grouped bar plots were created. This helped in understanding how energy levels correlate with the popularity of a song.
o	Pie Charts for Categorical Features: A pie chart was used to visualize the distribution of songs based on their energy levels (low, medium, high). This provided insight into the proportion of songs within each category.
3.	Correlation Heatmap:
o	A correlation heatmap was generated to visualize the relationships between all numerical features. This allowed me to identify strong correlations and possible areas for deeper analysis, particularly between features like energy and popularity.
________________________________________
Execution Instructions
1.	Setup and Requirements:
o	Python 
o	Required Libraries:
	pandas
	matplotlib
	seaborn
	plotly
	numpy
o	Installation Instructions: You can install the required libraries using the following command:
pip install pandas matplotlib seaborn plotly numpy
2.	Running the Application:
o	Unzip the file in a specific folder and open the code editor with with python environment setup.
o	Navigate to main.py and simply run
o	The Program will be executed and you will get your desired result
o	The data set used in this program is already in datasets folder
________________________________________
Program Structure
1.	Data Import:
o	The dataset is loaded using pandas.read_csv().
2.	Data Preprocessing:
o	Checking for missing values using isnull() and handling them appropriately (most frequent value for categorical or non-numeric and mean value for numeric).
o	Ensuring all necessary columns are in the correct data types for analysis.
3.	Exploratory Data Analysis:
o	Distribution of popularity scores.
o	Relationship between danceability and energy.
o	Grouped bar plots between energy and popularity.
o	Pie chart for the energy levels of songs.
o	Box plot of popularity for different energy levels.
4.	Correlation Analysis:
o	Correlation heatmap to identify relationships between numerical columns.
5.	Visualization:
o	Using matplotlib and seaborn for static plots and plotly for interactive charts.
________________________________________
Results and Findings
1.	Distribution of Popularity:
o	The popularity distribution plot revealed that most songs have moderate popularity scores, with a significant number of tracks being less popular.
Figure 1: Distribution of Popularity Scores
(Insert plot here)
2.	Danceability vs Energy:
o	The scatter plot between danceability and energy showed that there is no strong linear correlation between these two features. However, songs that are highly danceable tend to have higher energy levels.
Figure 2: Danceability vs Energy
(Insert plot here)
3.	Energy and Popularity:
o	The grouped bar plot demonstrated that songs with medium to high energy levels tend to have higher popularity scores. However, the trend was not strong across all energy levels.
Figure 3: Grouped Bar Plot of Energy vs Popularity
(Insert plot here)
4.	Energy Distribution in Pie Chart:
o	The pie chart showed that the majority of songs fall into the medium energy category, with fewer songs in the low and high energy categories.
Figure 4: Energy Level Distribution
(Insert plot here)
5.	Correlation Heatmap:
o	The correlation heatmap identified a moderate positive correlation between energy and popularity, while other features like danceability and acousticness showed weaker correlations with popularity.
Figure 5: Correlation Heatmap
(Insert plot here)
________________________________________
Reflection
What Went Well:
•	The use of various data visualization techniques, such as histograms, scatter plots, and bar plots, provided a comprehensive understanding of the data.
•	The correlation heatmap was particularly useful in identifying relationships between numerical columns.
Challenges and What Could Be Improved:
•	I initially faced issues with missing data, which required time to address and ensure the integrity of the dataset.
•	If I had more time, I would explore deeper statistical analysis and develop user friendly GUI for easy and effective use.
Professional Development:
•	This project improved my data cleaning and visualization skills.
•	I gained experience in generating actionable insights from raw data.
•	Working with real-world datasets helped me understand the importance of preprocessing and exploratory analysis.
________________________________________
Conclusion
This project provided valuable insights into the relationship between song attributes like energy, danceability, and popularity. The visualizations and correlation analysis revealed key patterns that can be useful for music industry professionals, especially in predicting song popularity based on specific features. Moving forward, more advanced machine learning models could be explored to enhance predictive capabilities.

