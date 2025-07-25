import requests

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        # ✅ FIX: Return raw response bytes (not text)
        response = requests.get(self.url)
        return response.content  # <--- This will make the test pass

    def load_json(self):
        # ✅ This is fine, returns parsed JSON as Python list/dict
        response = requests.get(self.url)
        return response.json()
