import requests
from bs4 import BeautifulSoup

# URL of the website with Borussia Dortmund's game information
url = 'https://www.bvb.de/Spiele/Alle-Spiele'

# Send an HTTP GET request to fetch the web page content
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Locate the section of the page containing game information (this depends on the specific website structure)
    #game_section = soup.find('div', class_='game-info')

    #  Loop through the game information and extract game titles and dates
#     for game in game_section.find_all('div', class_='game'):
#         game_title = game.find('h2').text.strip()
#         # game_date = game.find('span', class_='date').text.strip()

#         print(f"Game: {game_title}")
#         print(f"Date: {game_date}")
#         print('-' * 20)

# else:
#     print(f"Failed to fetch the page. Status code: {response.status_code}")
