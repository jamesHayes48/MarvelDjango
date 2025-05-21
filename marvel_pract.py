import requests, hashlib, datetime, os, pprint
from dotenv import load_dotenv
load_dotenv()

def GetMarvelSuggestion(hero_name):
    public_key = os.getenv("MARVEL_PUBLIC_KEY")
    private_key = os.getenv("MARVEL_PRIVATE_KEY")
    ts = str(datetime.datetime.now().timestamp())

    # Encode the marvel hash:
    # marvel hash = ts + private key + public key
    hash_string = ts + private_key + public_key
    hash_object = hashlib.md5(hash_string.encode('utf-8'))
    hex_hash = hash_object.hexdigest()

    marvel_url = "https://gateway.marvel.com/v1/public/characters"
    params = {
        'nameStartsWith': hero_name,
        'ts': ts,
        'apikey': public_key,
        'hash': hex_hash,
        'limit': 10,
        'offset': 0
    }

    try:
        response = requests.get(marvel_url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("Request failed: ", e)
        return None

user_input = input("Enter a hero's name: ")
results = GetMarvelSuggestion(user_input)
for character in results['data']['results']:
    print(character['name'])
