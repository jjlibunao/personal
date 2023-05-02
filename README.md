# Welcome to my repository!
Joren Libunao

This is my personal repository for projects I worked on during my time as a USF MSDS student that were allowed to be published or just projects I worked on in my own spare time. Please feel free to ask me about other projects I worked on in the program that were not allowed to be published, as I have many more that I would like to share, but due to plagiarism concerns for future cohorts I am not allowed to share them here. I would be happy to share sample code in those instances upon request. 

## Reddit Data Pipeline
In a topic involving topic clustering and sentiment analysis of Reddit posts and comments, I had to build a ETL data pipeline using Apache Airflow to automatically scrape data from Reddit, load it into Google Cloud platform, then transfer it into MongoDB Atlas, and finally load it into Databricks where the topic clustering and sentiment analysis took place. The code in this folder focuses on the entire data pipeline from scraping Reddit to MongoDB Atlas. The code for the topic clustering and sentiment analysis is available upon request, but I wanted to highlight the data pipeline as that was the main focus of this project. 

In case you are wondering, the MongoDB Atlas step was only there so I could practice using NoSQL and MongoDB. Typically, I would just load the data into Databricks directly using Google Cloud.

## Algorithm Reports
In my Data Structures and Algorithms course, we were tasked with writing two in-depth reports on some of the algorithms used for clustering and for feature importance. Both of those reports can be found here, with code used to implement each algorithm and visualizations as well to demonstrate the algorithms. 

## Stroke Prediction
This was a personal project I did in my spare time to practice with different classification models (Logistic Regression, Linear Support Vector Machines, Decision Tree Classifier, Random Forest Classifier, Gradient Boosting Classifier). Using a medical dataset containing patient data, the goal was to predict whether a patient was likely to have a stroke or not.

## Spotify Recommender App
I created a basic Spotify recommender app using the Spotify API and Streamlit. The app asks you for a song and it will output 10 related songs. I am in the process of trying to add a button to add it as a playlist to your library. 
