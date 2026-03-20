# Amazon Customer Review Sentiment Analysis

## Description

This project performs sentiment analysis on Amazon customer reviews to classify them as Positive, Negative, or Neutral. The analysis helps in understanding customer opinions and overall product feedback.

## Features

- Performs sentiment analysis using TextBlob

- Classifies reviews into Positive, Negative, and Neutral

- Calculates sentiment polarity

- Visualizes results using charts and graphs

- Generates insights from customer feedback

## Technologies Used

- Python
- Pandas
- TextBlob
- Matplotlib
- Seaborn
- WorldCloud

## Dataset
- Amazon Product Reviews
- Source: Public GitHub repository (imsreecharan/datasets_)

## Business Insights

- Product Strategy: Focus on "quality" and "fast delivery" to improve customer satisfaction  
- Marketing: High percentage of positive reviews can be used for testimonials  
- Customer Support: Negative reviews highlight issues like "broken" or "slow delivery" that need attention  

## How It Works

The dataset containing Amazon customer reviews is first cleaned and preprocessed. Each review is analyzed using TextBlob to calculate sentiment polarity:

Polarity > 0 → Positive
Polarity < 0 → Negative
Polarity = 0 → Neutral

The results are then visualized using graphs for better understanding.

## How to Run

1. Clone the repository
2. Install required libraries:
   pip install pandas textblob matplotlib seaborn
3. Run the script:
   python sentiment.py

## Output

The project provides:
- Sentiment classification (Positive, Negative, Neutral)
- Polarity scores for each review
- Visualizations like bar charts and word clouds

## Note
This project is created for educational purposes only.

## Author

Samruddhi Bhowood
B.Sc IT Student | Data Analytics Enthusiast


