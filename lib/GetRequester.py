# lib/GetRequester.py

import requests  # for sending HTTP requests
import json      # for parsing JSON data

class GetRequester:
    def __init__(self, url):
        self.url = url  # store the URL for requests

    def get_response_body(self):
        """Send a GET request to the stored URL and return the response body."""
        response = requests.get(self.url)
        return response.text  # returns raw response content as string

    def load_json(self):
        """Use get_response_body to get data and parse it as JSON."""
        response_body = self.get_response_body()
        return json.loads(response_body)  # convert string to Python dict or list
