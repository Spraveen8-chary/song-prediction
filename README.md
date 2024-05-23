# Song Predictions Based on Text Analysis
## Overview
This project involves the prediction of song themes based on text analysis using TextBlob within a Flask web application. It utilizes various components and scripts to extract data from Spotify playlists, build a predictive model, and play songs based on the predicted themes.

# Project Structure

- `static`: This directory contains CSS files, images, and other static assets for your web application.

- `templates`: Here, you'll find HTML files that are used to render the web pages for your Flask app.

- `app.py `: This is the main Flask application file, where your web application is defined and run.

- `extract_playlist.py`: This script is used to create a dataset by extracting data from Spotify playlists using their IDs.

- `model.pkl`: This is a serialized pickle model that you've built for predicting song themes based on text analysis.

- `model.py`: In this file, you've developed your model using TextBlob for predicting themes of songs.

- `playlist_data.csv`: This CSV file contains the data extracted from Spotify playlists, converted into a structured format.

- `song_extraction.py`: This script is used to predict themes for songs based on text analysis and play songs associated with the predicted themes.

# Getting Started
These instructions will help you get started with the song prediction feature of your project.

# Prerequisites
List any prerequisites that need to be installed before getting started. For example:

- Python 3.x
- Flask
- TextBlob
- Other dependencies...

# Note 
Get your ClientID and Secret code from spotify developers dashboard 

# Usage
Explain how to use the song prediction feature within your Flask-based project, including any configuration or setup required.

- To run the Flask web application, execute the following command:

```bash
  python app.py
```

Your web application will be accessible at `http://localhost:5000`.

- To predict themes for songs and play them, navigate to the appropriate section of your web application and follow the on-screen instructions.

# Output

- ``Home``
![image](https://github.com/Spraveen8-chary/song-prediction/assets/108536707/183830ad-fdbe-4046-9ff3-543506a2729e)

- ``text analysis``
  ![image](https://github.com/Spraveen8-chary/song-prediction/assets/108536707/81a3b0e3-d5bb-4cf4-bec1-ed9d52c73a9f)
- similar songs
    ![image](https://github.com/Spraveen8-chary/song-prediction/assets/108536707/d19840c9-83d9-48bd-ad45-93bf11a6df80)



