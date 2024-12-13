# Threads Review Analysis

This project is a sentiment analysis tool built using Flask, machine learning, and natural language processing (NLP). It is designed to analyze user reviews of the Threads app, determine whether the review is positive or negative, and display additional information such as the platform (Google Play or App Store), rating, and review description.

## Features
- Sentiment analysis of user reviews (Positive/Negative).
- Supports both Google Play and App Store reviews.
- Displays the review platform, rating (1 to 5 stars), and review description.
- Provides a simple web interface to submit and analyze reviews.

## Technologies Used
- **Flask**: A lightweight web framework for Python to serve the application.
- **Scikit-learn**: For machine learning, used to create the sentiment analysis model.
- **NLP (Natural Language Processing)**: Utilized to process and analyze review text.
- **Joblib**: For loading pre-trained models and vectorizers.
- **HTML/CSS/JavaScript**: For the frontend interface and user experience.

## Model Information
The sentiment analysis model used in this project was built using machine learning techniques. Here are some key details about the model:

- **Model Type**: The model are classification model that trained to predict whether a review is **Positive** or **Negative**.
- **Algorithm Used**: The model uses a Logistic Regression, 
- **Data**: The model was trained on a dataset of user reviews, which includes both Google Play and App Store reviews. The training data was preprocessed to remove noise, such as special characters, and tokenize the text.
- **Text Vectorization**: The `vectorizer.pkl` file contains the text vectorizer, used to transform the text data into numerical features for machine learning.
- **Performance**: The model achieved an accuracy of 85% on the test set, making it reliable for predicting sentiment in new reviews.
- **Model File**: The trained model is saved as `Threads_review.pkl` and loaded into the application for making predictions.
- 
- ## Model Performance

Below is a visual representation of the model's performance:

![Model Performance](<img width="551" alt="image" src="https://github.com/user-attachments/assets/702932c7-8cd5-4e18-8b25-84619f0696e0" />)
![Model Performance](<img width="317" alt="image" src="https://github.com/user-attachments/assets/38ff3dd8-24f9-4f52-bb1f-c88c57eafb9e" />)




## Usage
- On the homepage, you'll find a form where you can select the platform (Google Play or App Store), provide a review description, and rate the app (1-5 stars).
- After submitting the form, the app will display the sentiment of the review (Positive or Negative), along with the source (platform), rating, and review description.
- Visit the web application: Open a browser and go to `http://127.0.0.1:5000/` to start using the review analysis tool.


##UI
(<img width="908" alt="image" src="https://github.com/user-attachments/assets/f3bf1f78-2e2a-46d4-952f-9f20eabd252b" />)

