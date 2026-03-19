1. Project Overview
   
This project, Spotify Focus Predictor, is a Machine Learning application designed to classify music into "Focus" (study-friendly) and "Distraction" categories. By analyzing audio signatures, the model helps students automate the creation of deep-work playlists.

2. Features
   
Audio Analysis: Evaluates tracks based on Energy, Instrumentalness, and Acousticness.

Automated Labeling: Uses logic-based filtering to categorize 114,000+ tracks.

Focus Prediction: Identifies songs with low "Speechiness" to minimize cognitive load.

Data Visualization: Generates charts to show the difference between "Focus" and "Distraction" music.

3. Technologies Used

Python: The core programming language.

Pandas: For high-speed data manipulation and CSV handling.

Scikit-Learn: To implement the Machine Learning (K-Means/Classification) models.

Matplotlib: For rendering data insights and graphs.

4. Installation and SetuP
   
Clone the Repository:
git clone https://github.com/prerita25bce10141-ops/spotify-focus-predictor.git

Install Dependencies:
pip install pandas scikit-learn matplotlib

Prepare Data:
Place the dataset.csv (from Kaggle) into the root folder.

Run the Project:
python main.py
