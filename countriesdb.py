import requests

class database:
    def getinfo(self, countryname: str) -> dict:
        url = f"https://restcountries.com/v3.1/name/{countryname}?fields=name,capital,region,flags"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            return data[0]  # Return the first matched country
        else:
            print("Country not found or error occurred.")
            return {}
