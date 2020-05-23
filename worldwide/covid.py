import requests
import json
import time
import requests


class Covid():

    def __init__(self):

        self.x_rapidapi_host = "covid-19-data.p.rapidapi.com"
        self.x_rapidapi_key = "29ebf9fbadmshe4dd7086ac2bc74p14c987jsn441ea254509f"

        self.headers = {
            'x-rapidapi-host': self.x_rapidapi_host,
            'x-rapidapi-key': self.x_rapidapi_key
            }



    def covid_display_total(self):

        url = "https://covid-19-data.p.rapidapi.com/totals"
        querystring = {"format":"json"}
        response = requests.request("GET", url, headers=self.headers, params=querystring)

        return response.json()[0]


    def covid_display_country(self, country):

        url = "https://covid-19-data.p.rapidapi.com/report/country/name"
        querystring = {"date-format":"YYYY-MM-DD","format":"json","date":"2020-04-01","name":country}
        response = requests.request("GET", url, headers=self.headers, params=querystring)

        return response.json()[0]

    def covid_get_countries(self):

        url = "https://covid-19-data.p.rapidapi.com/help/countries"
        querystring = {"format":"json"}
        response = requests.request("GET", url, headers=self.headers, params=querystring)

        return response.json()

        

if __name__ == '__main__':
    c = Covid()
    print(c.covid_get_countries()[0])
