import random
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re

# Read the CSV file into a DataFrame
csv_file_path = 'updated_file.csv'
df = pd.read_csv(csv_file_path)
greetings = ["hi", "Hi", "Hello", "hello", "hey", "helloo", "hellooo", "g morning", "g morning", "good morning", "morning", "good day", "good afternoon", "good evening", "greetings", "greeting", "good to see you", "its good seeing you", "how are you", "how're you", "how are you doing", "how ya doin'", "how ya doin", "how is everything", "how is everything going", "how's everything going", "how is you", "how's you", "how are things", "how're things", "how is it going", "how's it going", "how's it goin'", "how's it goin", "how is life been treating you", "how's life been treating you", "how have you been", "how've you been", "what is up", "what's up", "what is cracking", "what's cracking", "what is good", "what's good", "what is happening", "what's happening", "what is new", "what's new", "what is neww", "gday", "howdy", 'assalamualaikum', 'salam', "what's up", "whats up!"]
bad_words_list = ["Oh no","Bollocks","Bad","bad man","Poor","bure","Gande","bad","poor","bad man","kute","bure","worse","doremon","Cheese"  ,"crackers","Shit","Bastard","besharam"]
# Function to clean and tokenize user queries
def get_device_info(device_name):
    device_name = preprocess_query(device_name)
    matching_device = df[df['Name'].str.lower().isin(device_name)]

    if not matching_device.empty:
        return f"Here is information about {device_name}:\n{get_top_products_table(matching_device)}"
    else:
        return f"Sorry, no information found for {device_name}."

def get_top_products_table(products):
    if not products.empty:
        table_html = '<table class="table table-bordered" style="max-width: 80%;"><thead><tr><th>ID</th><th>Name</th><th>Cleaned_Price</th><th>Clean_Rating</th><th>Total Ratings</th><th>URL</th></tr></thead><tbody>'
        for _, row in products.iterrows():
            table_html += f'<tr><td>{row["ID"]}</td><td>{row["Name"]}</td><td>{row["Cleaned_Price"]}</td><td>{row["Clean_Rating"]}</td><td>{row["Total Ratings"]}</td>'
            
            # Use the actual URL from the "URL" column
            product_url = row["URL"]
            
            # Include a clickable URL (replace 'product_url' with the actual variable)
            table_html += f'<td><a href="{product_url}" target="_blank">Link</a></td></tr>'

        table_html += '</tbody></table>'
        return table_html
    else:
        return "No top products available."

def preprocess_query(query):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(query.lower())
    tokens = [token for token in tokens if token.isalnum() and token not in stop_words]
    return tokens

# Function to filter devices based on user query
def get_best_devices_within_price_range(target_price, num_devices=2):
    # Calculate the absolute difference between device price and target price
    df['Price_Difference'] = abs(df['Cleaned_Price'] - target_price)

    # Filter devices based on the target price
    filtered_df = df[df['Cleaned_Price'] <= target_price]

    # Sort by price difference and cleanliness rating
    sorted_df = filtered_df.sort_values(by=['Price_Difference', 'Clean_Rating'], ascending=[True, False])

    # Drop the temporary column used for sorting
    sorted_df = sorted_df.drop(columns=['Price_Difference'])

    # Return the top N devices
    return sorted_df[['ID', 'Name', 'Cleaned_Price', 'Clean_Rating', 'Total Ratings']].head(num_devices)

# Function to calculate statistics

def calculate_statistics():
    total_listings = len(df)
    average_price = df['Cleaned_Price'].mean()
    average_rating = df['Clean_Rating'].mean()
    average_review_count = df['Total Ratings'].mean()

    # Generate a random number for total_questions_asked (for demonstration purposes)
    total_questions_asked = random.randint(35, 45)
    
    return total_listings, average_price, average_rating, average_review_count, total_questions_asked


def get_device_details(query):
    try:
        # Tokenize the query
        query_tokens = preprocess_query(query.lower())  # Convert to lowercase for case-insensitive matching

        # Find the index of 'device' in the query
        device_index = next((i for i, token in enumerate(query_tokens) if token == 'device'), None)

        if device_index is not None and device_index + 1 < len(query_tokens):
            # Extract the device name
            device_name = ' '.join(query_tokens[device_index + 2:])
            # Filter devices based on the device name
            matching_devices = df[df['Name'].str.lower().str.contains(device_name)]

            if not matching_devices.empty:
                # Generate HTML table with reduced width
                table_html = '<table class="table table-bordered" style="max-width: 80%;"><thead><tr><th>ID</th><th>Name</th><th>Cleaned_Price</th><th>Clean_Rating</th><th>Total Ratings</th>'
                
                # Check if 'URL' column exists
                if 'URL' in matching_devices.columns:
                    table_html += '<th>URL</th>'

                table_html += '</tr></thead><tbody>'

                for _, row in matching_devices.iterrows():
                    table_html += f'<tr><td>{row["ID"]}</td><td>{row["Name"]}</td><td>{row["Cleaned_Price"]}</td><td>{row["Clean_Rating"]}</td><td>{row["Total Ratings"]}</td>'
                    
                    # Check if 'URL' column exists
                    if 'URL' in matching_devices.columns:
                        table_html += f'<td><a href="{row["URL"]}" target="_blank">Link</a></td>'

                    table_html += '</tr>'

                table_html += '</tbody></table>'

                return table_html
            else:
                return "No devices found for the query."

        else:
            return "Device name not found in the query."
    except Exception as e:
        return f"An error occurred: {e}"



def get_two_best_devices(query):
    # Tokenize the query
    query_tokens = preprocess_query(query.lower())

    # Filter devices based on the device name in the query
    matching_devices = df[df['Name'].str.lower().str.contains('|'.join(query_tokens))]

    if not matching_devices.empty:
        # Sort the matching devices by 'Clean_Rating' column in descending order
        sorted_devices = matching_devices.sort_values(by='Clean_Rating', ascending=False)

        # Take the top two devices
        best_two_devices = sorted_devices.head(2)

        # Generate HTML table with reduced width for URL column
        table_html = '<table class="table table-bordered" style="max-width: 80%;"><thead><tr><th>ID</th><th>Name</th><th>Cleaned_Price</th><th>Clean_Rating</th><th>Total Ratings</th><th style="max-width: 150px;">URL</th></tr></thead><tbody>'

        for _, row in best_two_devices.iterrows():
            table_html += f'<tr><td>{row["ID"]}</td><td>{row["Name"]}</td><td>{row["Cleaned_Price"]}</td><td>{row["Clean_Rating"]}</td><td>{row["Total Ratings"]}</td><td style="max-width: 150px;"><a href="{row["URL"]}" target="_blank">Link</a></td></tr>'

        table_html += '</tbody></table>'

        return table_html
    else:
        return "No devices found for the query."


# Function to get top 5 products based on defined criteria
def get_top_products(criteria='highest_ratings'):
    if criteria == 'highest_ratings':
        top_products = df.sort_values(by='Clean_Rating', ascending=False).head(5)
    elif criteria == 'most_reviews':
        top_products = df.sort_values(by='Total Ratings', ascending=False).head(5)
    else:
        top_products = pd.DataFrame()

    return top_products

# Function to handle user queries
def handle_query(query):
    if any(bad_word in query for bad_word in bad_words_list):
        return "Sorry for frustrating you. I apologize if my response was inappropriate. Let's continue with your query."
    
    elif any(greet_word in query for greet_word in greetings):
        return "Hello! I'm your mobile phone recommendation chatbot. Feel free to ask anything."
    elif any(keyword in query for keyword in ('show me', 'display', 'list', 'mobiles', 'phones', 'devices')) and 'star rating' in query and any(keyword in query for keyword in ('GB RAM', 'GB ram')) and 'MP camera' in query:
    # Handle devices with specified criteria
        preprocessed_query = preprocess_query(query)
        
        rating_tokens = [token for token in preprocessed_query if token.replace('.', '', 1).isdigit()]
        ram_tokens = [token for token in preprocessed_query if token.isdigit()]

        try:
            min_rating = float(rating_tokens[0]) if rating_tokens else None
            min_ram, max_ram = int(ram_tokens[0]), int(ram_tokens[1]) if len(ram_tokens) > 1 else int(ram_tokens[0])
            
            if not matching_devices.empty:
                return f"The mobiles with a {min_rating}-star rating, {min_ram} to {max_ram} GB RAM, and above a 48 MP camera are:\n{get_top_products_table(matching_devices)}"
            else:
                return f"No mobiles found with a {min_rating}-star rating, {min_ram} to {max_ram} GB RAM, and above a 48 MP camera."
        except ValueError as ve:
            return f"An error occurred: {ve}"

    elif 'statistics' in query:
        total_listings, average_price, average_rating, average_review_count, total_questions_asked = calculate_statistics()

        # Increment total_questions_asked for each question encountered
        total_questions_asked += query.lower().count('how')  # You can customize this logic based on your specific requirements

        return f"Total Listings: {total_listings}\nAverage Product Price: {average_price}                                                      Average Ratings of Products: {average_rating}\n                                                                                     Average Review Count per Product: {average_review_count}\n                                                                             Average Questions Asked per product: {total_questions_asked}"

    elif 'device under' in query and 'rating over' in query:
        # Handle combination of price and rating criteria
        price_tokens = [token for token in preprocess_query(query) if token.isdigit()]
        rating_tokens = [token for token in preprocess_query(query) if token.replace('.', '', 1).isdigit()]
        print(price_tokens,rating_tokens)
        if len(price_tokens) > 1 or len(rating_tokens) == 1:
            max_price = float(price_tokens[0])
            min_rating = float(rating_tokens[1])
            print(max_price,min_rating)
            matching_devices = df[(df['Cleaned_Price'] <= max_price) & (df['Clean_Rating'] > min_rating)]
            print(df)
            if not matching_devices.empty:
                return f"The phones under {max_price} PKR with a rating over {min_rating} are:\n{get_top_products_table(matching_devices)}"
            else:
                return f"No devices found under {max_price} PKR with a rating over {min_rating}."

        else:
            return "Invalid combination. Please specify a valid price and rating."
    

    elif ('mobiles with a' in query or 'phone with' in query or 'device with' or 'phones with'in query) and 'star rating' in query and ('GB RAM' in query or 'GB ram' or 'GB Ram' in query):
        # Handle combination of brand, star rating, and RAM criteria
        preprocessed_query = preprocess_query(query)
        print("Preprocessed Query:", preprocessed_query)  # Add this line for debugging

        rating_tokens = [token for token in preprocessed_query if token.replace('.', '', 1).isdigit()]
        ram_tokens = [token for token in preprocessed_query if token.isdigit()]

        print("Rating Tokens:", rating_tokens)  # Add this line for debugging
        print("RAM Tokens:", ram_tokens)  # Add this line for debugging

        try:
            min_rating = float(rating_tokens[0]) if rating_tokens else None
            min_ram, max_ram = int(ram_tokens[0]), int(ram_tokens[1]) if len(ram_tokens) > 1 else int(ram_tokens[0])

            print("Min Rating:", min_rating)  # Add this line for debugging
            print("Min RAM:", min_ram)  # Add this line for debugging
            print("Max RAM:", max_ram)  # Add this line for debugging

            # Extract brand names from the query
            brand_names = [brand for brand in df['Brand'].str.lower().unique() if brand in preprocessed_query]

            print("Matching Brands:", brand_names)  # Add this line for debugging

            matching_devices = df[(df['Brand Name'].str.lower().isin(brand_names)) &
                                (df['Clean_Rating'] > min_rating) &  # Change this line to filter ratings higher than min_rating
                                (df['RAM'].between(min_ram, max_ram))]

            if not matching_devices.empty:
                return f"The mobiles with a {min_rating}-star rating and {min_ram} to {max_ram} GB RAM from {', '.join(brand_names)} are:\n{get_top_products_table(matching_devices)}"
            else:
                return f"No mobiles found with a {min_rating}-star rating and {min_ram} to {max_ram} GB RAM from {', '.join(brand_names)}."
        except ValueError as ve:
            return f"An error occurred: {ve}"
    elif 'phone with' in query and 'GB RAM' in query and 'MP Camera' in query:
        # Handle questions like "best phone with 8 GB RAM and 64 MP Camera"
        ram_tokens = [token for token in preprocess_query(query) if token.isdigit() and 'GB' in query]
        camera_tokens = [token for token in preprocess_query(query) if token.isdigit() and 'MP' in query]

        if len(ram_tokens) == 1 and len(camera_tokens) == 1:
            desired_ram = int(ram_tokens[0])
            desired_camera = int(camera_tokens[0])

            # Search for devices with the specified RAM and Camera specifications in the product descriptions
            matching_devices = df[df['Product_Description'].str.contains(f'{desired_ram}GB.*{desired_camera}MP', case=False, regex=True)]

            if not matching_devices.empty:
                return f"The best phones with {desired_ram} GB RAM and {desired_camera} MP Camera are:\n{get_top_products_table(matching_devices)}"
            else:
                return f"No devices found with {desired_ram} GB RAM and {desired_camera} MP Camera."
        else:
            return "Invalid RAM or camera specification. Please specify valid values."

    elif 'phone with' in query and 'GB RAM' in query:
        # Handle questions like "best phone with 64 GB RAM"
        ram_tokens = [token for token in preprocess_query(query) if token.isdigit()]
        print(ram_tokens)
        if len(ram_tokens) == 1:
            desired_ram = int(ram_tokens[0])
            print(desired_ram)
            best_spec_devices = df[df['RAM'] == desired_ram].sort_values(by='Clean_Rating', ascending=False).head(5)

            if not best_spec_devices.empty:
                return f"The best phones with {desired_ram} GB RAM are:\n{get_top_products_table(best_spec_devices)}"
            else:
                return f"No devices found with {desired_ram} GB RAM."
        else:
            return "Invalid RAM specification. Please specify a valid RAM value."

    
    elif ('device under' in query or 'device over' in query) or ('mobile under' in query or 'mobile over' in query):
        # Handle queries for devices under or over a specified price
        try:
            # Extract the target price from the query, considering 'k' (thousands)
            price_tokens = [token.lower() for token in preprocess_query(query) if token.isdigit() or (token.endswith('k') and token[:-1].isdigit())]
            
            if 'k' in price_tokens[-1]:
                # If the last token ends with 'k', treat it as thousands
                target_price = float(price_tokens[-1][:-1]) * 1000
            else:
                target_price = float(price_tokens[-1])

            # If brand_name is not needed, consider all brands
            if 'devices under' in query:
                # Get devices under the specified price for all brands
                devices_under_price = df[df['Cleaned_Price'] <= target_price].head(5)
                return get_top_products_table(devices_under_price)
            elif 'devices over' in query:
                # Get devices over the specified price for all brands
                devices_over_price = df[df['Cleaned_Price'] > target_price].head(5)
                return get_top_products_table(devices_over_price)
        except ValueError:
            return "Invalid price value. Please specify a valid numeric price."


    elif 'under' in query or ' over' in query :
        # Handle queries for devices under or over a specified price
        try:
            # Extract the target price from the query, considering 'k' (thousands)
            price_tokens = [token.lower() for token in preprocess_query(query) if token.isdigit() or (token.endswith('k') and token[:-1].isdigit())]

            if 'k' in price_tokens[-1]:
                # If the last token ends with 'k', treat it as thousands
                target_price = float(price_tokens[-1][:-1]) * 1000
            else:
                target_price = float(price_tokens[-1])

            # Extract brand name from the "Brand Name" column
            brand_name = next((token for token in preprocess_query(query) if token.lower() in df['Brand Name'].str.lower().unique()), None)

            # If brand_name is None, consider all brands
            if brand_name is None:
                if 'under' in query:
                    # Get devices under the specified price for all brands
                    devices_under_price = df[df['Cleaned_Price'] <= target_price].head(5)
                    return get_top_products_table(devices_under_price)
                elif 'over' in query:
                    # Get devices over the specified price for all brands
                    devices_over_price = df[df['Cleaned_Price'] > target_price].head(5)
                    return get_top_products_table(devices_over_price)
            else:
                # Filter devices based on the specified brand and price
                if 'under' in query:
                    devices_under_price = df[(df['Cleaned_Price'] <= target_price) & (df['Brand Name'].str.lower() == brand_name)].head(5)
                    return get_top_products_table(devices_under_price)
                elif 'over' in query:
                    devices_over_price = df[(df['Cleaned_Price'] > target_price) & (df['Brand Name'].str.lower() == brand_name)].head(5)
                    return get_top_products_table(devices_over_price)
        except ValueError:
            return "Invalid price value. Please specify a valid numeric price."
    elif any(word in query for word in ['between', 'price range', 'in range']) and any(keyword in query for keyword in ['price range', 'between']):
        try:
            # Extract the target price range from the query, considering 'k' (thousands)
            price_tokens = [token.lower() for token in preprocess_query(query) if token.isdigit() or (token.endswith('k') and token[:-1].isdigit())]
            if 'k' in price_tokens[0] or 'k' in price_tokens[1]:
                # If either token ends with 'k', treat it as thousands
                min_price = float(price_tokens[0][:-1]) * 1000 if 'k' in price_tokens[0] else float(price_tokens[0])
                max_price = float(price_tokens[1][:-1]) * 1000 if 'k' in price_tokens[1] else float(price_tokens[1])
            else:
                min_price = float(price_tokens[0])
                max_price = float(price_tokens[1])

            # Filter devices based on the specified price range
            filtered_devices = df[(df['Cleaned_Price'] >= min_price) & (df['Cleaned_Price'] <= max_price)]

            if not filtered_devices.empty:
                # Sort devices by Clean_Rating in descending order to get the best-rated devices
                sorted_devices = filtered_devices.sort_values(by='Clean_Rating', ascending=False).head(5)
                return get_top_products_table(sorted_devices)
            else:
                return f"No devices found in the range {min_price} to {max_price}."
        except ValueError:
            return "Invalid price range. Please specify valid numeric price values."


    elif 'device details' in query:
        response = get_device_details(query)
        print("Response to 'device details' query:", response)  
        return response
    elif 'top products' in query or 'best products' in query or 'top chart' or 'Top products'in query:
        top_products = get_top_products()
        return get_top_products_table(top_products)
    elif 'devices' or 'Devices' in query:
        response = get_two_best_devices(query)
        return response
    elif 'davice details' in query:
        response = get_device_details(query)
        print("Response to 'device details' query:", response)  
        return response
    else:
        return "I'm sorry, I didn't understand that. Feel free to ask me about the best devices under a specific price range, inquire about device details, or ask for the price of a specific device."

if __name__ == "__main__":
    # Example interaction loop
    exit_chat = False
    while not exit_chat:
        user_query = input("You: ")
        response = handle_query(user_query)
        print(response)
