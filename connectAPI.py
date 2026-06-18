import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):

    url=f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    

    if response.status_code == 200:  # This 200 means the request has been succeded according to HTTPS Static Codes! (Just like 404 for url not found)

        pokemon_data = response.json()

        #print(pokemon_data) # If u type this line....output will be an abomination 😭 (A large dictionary which is hard to read 🥀)
        
        return pokemon_data
    
    else:
        print(f"Failed to retrieve the data {response.status_code}")

pokemon_name=input("Enter the name of the pokemon whose data u wanna know!: ")

pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"{pokemon_info["name"].capitalize()} is the name of the pokemon ")
    print(f"{pokemon_info["id"]} is the id of the pokemon ")
    print(f"{pokemon_info["height"]} is the height of the pokemon ")
    print(f"{pokemon_info["weight"]} is the weight of the pokemon ")