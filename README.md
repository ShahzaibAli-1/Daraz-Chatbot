
# Daraz Chat Bot for Mobile Recommendation

This project presents a sophisticated chat bot designed for mobile recommendations on the Daraz platform. The implementation involves meticulous data retrieval, cleaning, and storage processes to offer users a seamless experience when seeking information about mobile devices.

## Table of Contents
- [Project Overview](#project-overview)
    - [Data Retrieval](#1-data-retrieval)
    - [Data Processing](#2-data-processing)
    - [Data Storage](#3-data-storage)
    - [Chat Bot Development](#4-chat-bot-development)
    - [User Queries Handling](#5-user-queries-handling)
    - [Frontend Development](#6-frontend-development)
    - [Backend Integration](#7-backend-integration)
- [Video Demo](#video-demo)

## Project Overview

### 1. Data Retrieval
Mobile device details are sourced from the Daraz website using Selenium, with a targeted search for the keyword "mobile." The first 160 mobiles listed are scraped, extracting comprehensive information such as price, specifications, ratings, and reviews.

### 2. Data Processing
The acquired data undergoes a rigorous cleaning process to ensure accuracy and reliability. Essential information, including device name, brand, rating, reviews, and specifications, is extracted and organized.

### 3. Data Storage
Cleaned data is efficiently stored in both CSV files and an SQL database, facilitating easy retrieval and analysis.

### 4. Chat Bot Development
Utilizing the Natural Language Toolkit (NLTK), a chat bot is created to handle user queries seamlessly. The bot efficiently responds to inquiries related to device pricing, specifications, ratings, and combinations thereof.

### 5. User Queries Handling

- **Price-based queries:** Users can inquire about devices within specific price ranges (e.g., Samsung devices over 35,000 and under 60,000).
- **Specification-based queries:** Users can search for devices based on specifications (e.g., Redmi phone with 8 GB RAM and 32 MP camera).
- **Rating-based queries:** Users can explore devices with a specified rating threshold (e.g., devices with a rating over 4 stars).
- **Combined queries:** Users can perform searches based on a combination of ratings, specifications, and device names (e.g., Show me Redmi mobiles with a 4-star rating, 4 to 8 GB RAM).

### 6. Frontend Development
A responsive and visually appealing frontend is crafted using HTML, CSS, and JavaScript to enhance user interaction and experience.

### 7. Backend Integration
The frontend is seamlessly connected to the backend using the Flask framework, ensuring a robust and dynamic interaction between users and the chat bot.

This project amalgamates advanced web scraping techniques, natural language processing, and web development to provide users with an intuitive and effective mobile recommendation system on the Daraz platform.

## Video Demo
Check out the video demo of the Daraz Chat Bot in action: [Daraz Chat Bot Video Demo](https://github.com/Gamer997/Daraz-Chatbot/assets/98121819/b7ce727d-45c1-40e7-af84-e45ebdcf9532)

Feel free to explore the code and contribute to the enhancement of this mobile recommendation system!
