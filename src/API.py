import FILE
import requests

API = 'https://api.hypixel.net/'
UUID_API = 'https://playerdb.co/api/player/minecraft/'

def update_market_data():
    market_data = requests.get(API+"v2/skyblock/bazaar")
    FILE.write_json(market_data.json(),'./output/market_data.json')

def check_market_data():
    try:
        return FILE.get_json('./output/market_data.json')
    except Exception as e:
        with open("./output/logs.txt", "w") as logging:
            logging.write(str(e))
        print(f"[API Controller]: full_data file doesn't exist OR can't read from file...")

def get_player_bestiary_kills(API_KEY: str, UUID: str, PROFILE_CUTE_NAME: str):
    player_data = requests.get(API+f'v2/skyblock/profiles?uuid={UUID}&key={API_KEY}')

    for profile in player_data.json()['profiles']:
        if profile['cute_name'] == PROFILE_CUTE_NAME:
            player_data = profile['members'][UUID]['bestiary']['kills']

    FILE.write_json(player_data,f'./output/{UUID}.json')

def get_uuid_from_username(name):
    uuid = requests.get(UUID_API+f'{name}')
    return uuid.json()['data']['player']['raw_id']