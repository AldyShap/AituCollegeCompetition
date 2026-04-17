import requests
import pandas as pd
import json

url = "https://restcountries.com"

def show_contries(continent):
    data_contries = []
    try:
        response = requests.get(f"{url}/v3.1/region/{continent}")

        if response.status_code == 404:
            print("Такого континента нету в базе")
            exit()

        if response.status_code != 200:
            print("Такого континента нету в базе")
            exit()

        res_json = response.json()
        
        print("=="*50)
        print(f"The contries in continent: {continent}")
        print("--"*50)

        for item in res_json:
            name = item["name"]["common"]
            capital = item.get("capital", ["Not have"])[0]
            population = item["population"]
            
            print(f"The country: {name}")
            print(f"The capital: {capital}")
            print(f"The population: {population}")
            print("--"*50)
            data_contries.append(
                {
                    "name": name,
                    "capital": capital,
                    "population": population
                }
            )
        return data_contries

    except Exception as e:
        print(f"Error: {e}")
        exit()

continent = input("Enter the continent (Asia, Europs, Africa, Oceania): ")

data = show_contries(continent)

# Asia, Africa, North America, South America, Antarctica, Europe, and Australia (or Oceania)

filename = continent.lower().replace(" ", "_").strip() + "_countries.json"

with open(filename, "w") as f:
    json.dump(data, f, indent=4)

print("=="*50)

print("Analys the data: ")

df = pd.DataFrame(data)


max_pop = df.loc[df["population"].idxmax()]
min_pop = df.loc[df["population"].idxmin()]

avg_pop = df["population"].mean()

print(f"The biggest population has: {max_pop}")
print(f"The smallest population has: {min_pop}")
print(f"The average population: {avg_pop}")

print("=="*50)

country = input("Enter the country: ")

try:
    response = requests.get(f"{url}/v3.1/name/{country}")
    res_json = response.json()
    if response.status_code == 404:
        print("The country is not found")
    
    country_of_city = res_json[0]["name"]["common"]
    capital = res_json[0]["capital"][0]
    continent_of_city = res_json[0]["continents"][0]
    population = res_json[0]["population"]
    print(f"The country: {country_of_city}")
    print(f"The city: {country}")
    print(f"The capital: {capital}")
    print(f"The number of population: {population}")
except Exception as e:
    print(f"Error: {e}")


