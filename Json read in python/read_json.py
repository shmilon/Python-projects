import requests

# Send a GET request to the API URL
response = requests.get('https://alquranbd.com/api/tafheem/sura/list')

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Access the response data (JSON)
    data = response.json()

    for item in data:
      id = item['id']
      name = item['name']
    
      print(id,name)


else:
    print('Error:', response.status_code)
