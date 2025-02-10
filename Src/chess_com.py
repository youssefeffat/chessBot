import requests
import time
import chess
import chess.svg
from IPython.display import display, SVG
from dotenv import load_dotenv
import os
# Load environment variables from .env file
load_dotenv()


# Lichess API Token
TOKEN = os.getenv("TOKEN")
print(TOKEN)

# API Headers
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

# Step 1: Create a new game
def create_game():
    url = "https://lichess.org/api/challenge/ai"
    data = {
        "level": 3,  # AI difficulty (1 to 8)
        "clock.limit": 300,  # 5 minutes per player
        "clock.increment": 0,  # No increment
        "color": "white"  # 'white', 'black', or 'random'
    }

    response = requests.post(url, headers=HEADERS, json=data)
    
    print("Response Status Code:", response.status_code)
    print("Response Content:", response.text)  # Debugging

    if response.status_code == 201:
        game_data = response.json()
        if "id" in game_data:
            game_id = game_data["id"]
            print(f"Game Created! Game ID: {game_id}")
            #print(f"Game Link: {game_data['url']}")
            return game_id
        else:
            print("❌ Unexpected response format:", game_data)
            return None
    else:
        print(f"❌ Failed to create game: {response.text}")
        return None

# Step 2: Make a move for White & Black
def make_move(game_id, move):
    url = f"https://lichess.org/api/board/game/{game_id}/move/{move}"
    response = requests.post(url, headers=HEADERS)
    
    if response.status_code == 200:
        print(f" Move '{move}' played successfully!")
    else:
        print(f" Failed to make move: {response.text}")

# Step 3: Fetch game state & Display
def display_board(fen):
    board = chess.Board(fen)
    display(SVG(chess.svg.board(board=board)))

def get_game_state(game_id):
    url = f"https://lichess.org/api/board/game/{game_id}/stream"
    response = requests.get(url, headers=HEADERS)
    print(response.status_code)
    if response.status_code == 200:
        game_data = response.json()
        #print(game_data)
        fen = game_data.get("state", {}).get("fen", "startpos")
        return fen
    else:
        print(f" Failed to fetch game state: {response.text}")
        return None

def check_game_exists(game_id):
    url = f"https://lichess.org/api/board/game/{game_id}"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        print(f"Game {game_id} exists and is active.")
        return True
    else:
        print(f"Game {game_id} not found! Status: {response.status_code}")
        return False

# Run the script
game_id = create_game()
time.sleep(10)  # Wait for game to be created

if game_id:
    moves = ["e2e4", "e7e5", "g1f3", "b8c6"]  # Example moves
    
    for move in moves:
        make_move(game_id, move)
        time.sleep(2)  # Wait before making the next move
        print("I'm in for")
        # Fetch & Display the board
        if check_game_exists(game_id):
            fen = get_game_state(game_id)
        else:
             print("Can't fetch game state because the game doesn't exist.")
        if fen:
            print("I'm in if")
            display_board(fen)


'''import requests

url = "https://api.chess.com/pub/player/chessbotproject/stats"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

x= requests.get(url,headers=headers)
print(x.json())
response = requests.get(url, headers=headers)

print("Status Code:", response.status_code)
print("Response Content:", response.text)'''
