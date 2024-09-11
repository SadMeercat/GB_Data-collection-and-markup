import requests

# Замените на свой ключ API
FOURSQUARE_API_KEY = 'fsq3aVPr7MQ3CkqQXEgptJJ0Jwhn8CDITt2F6Io3gKpdcs8='

# Функция для запроса заведений по категории
def search_venues(category, location="Moscow", limit=10):
    url = "https://api.foursquare.com/v3/places/search"
    headers = {
        "Accept": "application/json",
        "Authorization": FOURSQUARE_API_KEY,
        "Accept-language": "ru"
    }
    params = {
        "query": category,
        "near": location,
        "limit": limit
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()['results']
    else:
        print(f"Ошибка: {response.status_code}")
        return None

# Функция для вывода информации о заведениях
def print_venues_info(venues):
    if venues:
        for venue in venues:
            name = venue['name']
            address = ', '.join(venue['location']['formatted_address']) if 'formatted_address' in venue['location'] else "Адрес не указан"
            rating = venue.get('rating', "Нет рейтинга")
            print(f"Название: {name}\nАдрес: {address}\nРейтинг: {rating}\n")
    else:
        print("Заведения не найдены.")

# Основная логика программы
def main():
    category = input("Введите категорию (например, кофейни, музеи, парки): ")
    location = input("Введите местоположение (например, Moscow): ")
    venues = search_venues(category, location)
    print_venues_info(venues)

if __name__ == "__main__":
    main()
