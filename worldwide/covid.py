import requests
import json

import requests

x_rapidapi_host = "covid-19-data.p.rapidapi.com"
x_rapidapi_key = "29ebf9fbadmshe4dd7086ac2bc74p14c987jsn441ea254509f"

def covid_display_total():

    url = "https://covid-19-data.p.rapidapi.com/totals"

    querystring = {"format":"json"}

    headers = {
        'x-rapidapi-host': x_rapidapi_host,
        'x-rapidapi-key': x_rapidapi_key
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response
