## Project Overview: Daraz Chat Bot for Mobile Recommendation

This project focuses on the development of a sophisticated chat bot tailored for mobile recommendations on the Daraz platform. The methodology employed in creating this chat bot involves meticulous data retrieval, cleaning, and storage processes, providing users with a seamless experience when seeking information about mobile devices.

Key Steps in the Implementation:

### 1. Data Retrieval:
The details of mobile devices are sourced from the Daraz website through a targeted search using the keyword "mobile." Selenium is utilized to extract comprehensive information, including price, specifications, ratings, and reviews, from the first 160 mobiles listed.

### 2. Data Processing: 
The acquired data undergoes a rigorous cleaning process to ensure accuracy and reliability. Essential information such as device name, brand, rating, reviews, and specifications is extracted and organized.

### 3. Data Storage:
   The cleaned data is stored efficiently in both CSV files and an SQL database, facilitating easy retrieval and analysis.

### 4. Chat Bot Development: 
Leveraging Natural Language Toolkit (NLTK), a chat bot is created to handle user queries seamlessly. The chat bot efficiently responds to user inquiries related to device pricing, specifications, ratings, and combinations thereof.

### 5. User Queries Handling:

Price-based queries: Users can inquire about devices within specific price ranges (e.g., Samsung devices over 35,000 and under 60,000).
Specification-based queries: Users can search for devices based on specifications (e.g., Redmi phone with 8 GB RAM and 32 MP camera).
Rating-based queries: Users can explore devices with a specified rating threshold (e.g., devices with a rating over 4 stars).
Combined queries: Users can perform searches based on a combination of ratings, specifications, and device names (e.g., Show me Redmi mobiles with a 4-star rating, 4 to 8 GB RAM).

### 6. Frontend Development: 
A responsive and visually appealing frontend is crafted using HTML, CSS, and JavaScript to enhance user interaction and experience.

### 7. Backend Integration: 
The frontend is seamlessly connected to the backend using the Flask framework, ensuring a robust and dynamic interaction between users and the chat bot.

This project amalgamates advanced web scraping techniques, natural language processing, and web development to provide users with an intuitive and effective mobile recommendation system on the Daraz platform.
