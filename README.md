# Welcome to my repository!
<b>Owner</b>: Joren Libunao, USF MSDS '23, UCSD '16 <br>
<b>Previous role</b>: Data Scientist Intern at Alaska Airlines, Inc.

## Table of Contents
- [Introduction](#introduction)
- [Reddit Data Pipeline](#reddit-data-pipeline)
- [Waste Classifier App](#waste-classifier-app)
- [Algorithm Reports](#algorithm-reports)
- [Evolution Simulator](#evolution-simulator)
- [Stroke Prediction](#stroke-prediction)
- [Spotify Recommendation App](#spotify-recommendation-app)
- [MLOps Project and Slide Deck](#mlops-project)

## Introduction <a name="introduction"></a>
This is my personal repository for projects I worked on during my time as a USF MSDS student that were allowed to be published or just projects I worked on in my own spare time. Please feel free to ask me about other projects I worked on in the program that were not allowed to be published, as I have many more that I would like to share, but due to plagiarism concerns for future cohorts I am not allowed to share them here. I would be happy to share sample code in those instances upon request. 

## Reddit Data Pipeline <a name="reddit-data-pipeline"></a>
#### Related class: Distributed Data Systems
In a topic involving topic clustering and sentiment analysis of Reddit posts and comments, I had to build a ETL data pipeline using Apache Airflow to automatically scrape data from Reddit, load it into Google Cloud platform, then transfer it into MongoDB Atlas, and finally load it into Databricks where the topic clustering and sentiment analysis took place. The code in this folder focuses on the entire data pipeline from scraping Reddit to MongoDB Atlas. The code for the topic clustering and sentiment analysis is available upon request, but I wanted to highlight the data pipeline as that was the main focus of this project. 

In case you are wondering, the MongoDB Atlas step was only there so I could practice using NoSQL and MongoDB. Typically, I would just load the data into Databricks directly using Google Cloud.

## Waste Classifier App <a name="waste-classifier-app"></a>
#### Related class: Entrepreneurship in Data Science
Using PyTorch's torchvision image classification models, Amazon Web Services (AWS), and Flask, my group of 6 including myself built a waste classifier app that would take a photo of waste and determine which bin the item should go into: compost, recycling, or landfill. The app was momentarily deployed on a public link, but has since been removed due to running out of AWS credits. You can find detailed instructions for the app in a markdown file in this folder.

## Algorithm Reports <a name="algorithm-reports"></a>
#### Related class: Data Structures and Algorithms
In my Data Structures and Algorithms course, we were tasked with writing two in-depth reports on some of the algorithms used for clustering and for feature importance. Both of those reports can be found here, with code used to implement each algorithm and visualizations as well to demonstrate the algorithms. 

## Evolution Simulator <a name="evolution-simulator"></a>
#### Related class: Deep Learning
In a team of 5, we developed an evolution simulator game that uses a PyTorch algorithm similar to NEAT to find the optimal neural network weights for a creature to survive in the environment. The creatures must eat the plants in order to gain energy, and they learn how to best navigate the environment using weights which control their turning and direction. 

## Stroke Prediction <a name="stroke-prediction"></a>
This was a personal project I did in my spare time to practice with different classification models (Logistic Regression, Linear Support Vector Machines, Decision Tree Classifier, Random Forest Classifier, Gradient Boosting Classifier). Using a medical dataset containing patient data, the goal was to predict whether a patient was likely to have a stroke or not.

## Spotify Recommendation App <a name="spotify-recommendation-app"></a>
I created a basic Spotify recommender app using the Spotify API and Streamlit. The app asks you for a song and it will output 10 related songs. I am in the process of trying to add a button to add it as a playlist to your library. 

## MLOps Pipeline Project
#### Related class: Machine Learning Operations
In a team of 4, we researched and used many different ML tools for experiment and artifact tracking, data versioning, data quality, model orchestration, model deployment, app development, model monitoring, and CI/CD. After working with all of the tools, we chose one tool for each stage to build an overall MLOps pipeline for the business case of predicting e-commerce sales of summer clothes, and then presented it to our professor who was acting as the CTO of the company.
