import requests

House = {
    'id': 34940602,
    'name': 'perfect_peace_private_room_in_brooklyn',
    'host_id': 263282580,
    'host_name': 'caritas',
    'neighbourhood_group': 'brooklyn',
    'neighbourhood': 'bedford-stuyvesant',
    'latitude': 40.79593,
    'longitude': -73.9503,
    'room_type': 'private_room',
    'minimum_nights': 2,
    'number_of_reviews': 2,
    'last_review': '2019-05-26',
    'reviews_per_month': 1.25,
    'calculated_host_listings_count': 2,
    'availability_365': 171
}
url = 'http://localhost:9696/predict'
response = requests.post(url, json=House)

try:
    print(response.json())
except Exception as e:
    print("Response was not valid JSON:", response.text)