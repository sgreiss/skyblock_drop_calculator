import API
import FUNCTIONS

def main():
    API_KEY = ''
    with open("hidden.txt", "r") as f:
        lines = f.readlines()
        API_KEY = lines[0].strip()
    API.get_player_bestiary_kills(API_KEY, API.get_uuid_from_username('Squeed_'), 'Watermelon')
    print(FUNCTIONS.calculate_chance(0.1, 203.74, 124.8, True))









if __name__ == "__main__":
    main()