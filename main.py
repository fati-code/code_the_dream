import requests

BASE_URL = ('https://countries.dev')

def fetch_data(endpoint):
    url = BASE_URL + endpoint

    try:
        response = requests.get(url)

    except requests.exceptions.ConnectionError:
        print("Could not connect. Please check your internet connection.")
        return None

    if response.status_code != 200:
        print("Could not get the data. Please try again later.")
        return None

    else:
        return response.json()

def get_region():
    user_input = input("Enter a region (Africa, Americas, Asia, Europe, Oceania): ").strip().capitalize()
    if user_input == "":
        print("Need to enter a region")
        return None
    return user_input

def filter_by_region(countries,region):
    matches = []
    for country in countries:
        if country['region'] == region:
            matches.append(country)
            
    return matches

def display_countries(countries):
    for country in countries:
        print(f"Name: {country.get('name')}")
        print(f"Capital : {country.get('capital', 'N/A')}")
        print(f"Population : {country.get('population', 'N/A'):,}")
        print(f"Area : {country.get('area', 'N/A')}")
        print("-"* 30)
    
def main():

    countries = fetch_data("/countries")
    if countries is None:
        return

    region = get_region()
    if region is None:
        return
    
    matches = filter_by_region(countries,region)
    if len(matches) == 0:
        print(f"No countries found in {region}.")
        return

    display_countries(matches)

   
if __name__=="__main__":
    main()



