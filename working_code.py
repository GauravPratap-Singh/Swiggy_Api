import json
import pandas as pd
import os


# Function to fetch dish information from json file
def fetch_dish_info(data):
    dishes_li = []
    cards = data['data']['cards']
    for card in cards:
        grouped_card = card.get("groupedCard", {})
        card_group_map = grouped_card.get("cardGroupMap", {})
        regular_cards = card_group_map.get("REGULAR", {})
        for regular_card in regular_cards.get("cards", []):
            categories = regular_card.get("categories", [])
            data = regular_card['card']['card']
            if 'itemCards' in data:
                for item in data['itemCards']:
                    dish_info = item['card']['info']
                    if dish_info:
                        dish = {
                            'Dish Name': dish_info['name'],
                            'Category': dish_info['category'],
                            'Price': dish_info['price'] / 100,
                            'Description': dish_info.get('description', 'N/A'),
                            'Rating': dish_info['ratings']['aggregatedRating'].get('rating', 'N/A'),
                            'Rating Count': dish_info['ratings']['aggregatedRating'].get('ratingCount', 'N/A')
                        }
                    dishes_li.append(dish)
    return dishes_li

# Function to convert extracted menu to pandas csv file
def save_to_csv(dishes_li):
    # Convert the extracted data into a Pandas DataFrame
    df = pd.DataFrame(dishes_li)

    # Save the DataFrame to a CSV file
    df.to_csv('menu_data.csv', index=False)
    print("Menu data saved to menu_data.csv")

# Function to load data from json file
def load_json(json_path):
    with open(json_path, 'r') as json_file:
    # Load JSON data from the file
        data = json.load(json_file)
    return data


if __name__ == "__main__":

    # Loading the json file containg swiggy api content in json
    json_path = 'res3.json'
    if os.path.exists(json_path):
        json_data = load_json('res3.json')
        # Extracting the menu detail from the json file
        if json_data:
            menu_data = fetch_dish_info(json_data)

        #Converting the extracted data into table formatted CSV file using pandas
        if menu_data:
            save_to_csv(menu_data)
    else:
        print("File does not exist.")
        exit
    

    
                


