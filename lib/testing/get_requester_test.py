# lib/test_get_requester.py

from lib.GetRequester import GetRequester

URL = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'
EXPECTED_DATA = [
    {'name': 'Daniel', 'occupation': 'LG Fridge Salesman'},
    {'name': 'Joe', 'occupation': 'WiFi Fixer'},
    {'name': 'Avi', 'occupation': 'DJ'},
    {'name': 'Howard', 'occupation': 'Mountain Legend'}
]

def test_get_response_body():
    '''get_response_body should return a valid JSON string (not empty).'''
    requester = GetRequester(URL)
    response = requester.get_response_body()
    assert isinstance(response, str)
    assert 'Daniel' in response  # quick check on content

def test_load_json():
    '''load_json should return the correct list of dictionaries.'''
    requester = GetRequester(URL)
    data = requester.load_json()
    assert data == EXPECTED_DATA
