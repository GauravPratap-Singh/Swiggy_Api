import sys
import requests
import pandas as pd

# This is original code, this how it suppose to run but i am not able to find any swiggy documentation for api or any other source which have
#any detail regarding how to use swiggy api

def fetch_menu_data(restaurant_id):
    # API endpoint for fetching menu data
    url = f"https://www.swiggy.com/dapi/menu/pl?page-type=REGULAR_MENU&complete-menu=true&lat=18.56&lng=73.95&restaurantId={restaurant_id}"

    # Fetch menu data from the Swiggy API
    response = requests.get(url)
    if response.status_code == 200:
        menu_data = response.json()
        return menu_data
    else:
        print(f"Failed to fetch menu data. Status code: {response.status_code}")
        return None

def extract_menu_details(json_data):
    dishes = []
    cards = json_data["data"]["cards"]
    for card in cards:
        grouped_card = card.get("groupedCard")
        if grouped_card:
            card_group_map = grouped_card.get("cardGroupMap")
            if card_group_map:
                regular_cards = card_group_map.get("REGULAR")
                if regular_cards:
                    cards = regular_cards.get("cards")
                    for card in cards:
                        categories = card.get("categories")
                        if categories:
                            for category in categories:
                                title = category.get("title")
                                item_cards = category.get("itemCards")
                                if item_cards:
                                    for item_card in item_cards:
                                        dish = item_card.get("card")
                                        if dish:
                                            dish_info = {
                                                "name": dish.get("info").get("name"),
                                                "price": dish.get("info").get("price"),
                                                "description": dish.get("info").get("description"),
                                                "category": dish.get("info").get("category")
                                            }
                                            dishes.append(dish_info)
    return dishes

def save_to_csv(menu_items):
    # Convert the extracted data into a Pandas DataFrame
    df = pd.DataFrame(menu_items)

    # Save the DataFrame to a CSV file
    df.to_csv('menu_data.csv', index=False)
    print("Menu data saved to menu_data.csv")

if __name__ == "__main__":
    # Check if the restaurant_id is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py restaurant_id")
        sys.exit(1)

    restaurant_id = sys.argv[1]
    menu_data = fetch_menu_data(restaurant_id)

    if menu_data:
        menu_items = extract_menu_details(menu_data)
        save_to_csv(menu_items)
