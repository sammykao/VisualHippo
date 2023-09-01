import requests
import haversine as hs
from haversine import Unit
import re
from restaurant import Restaurant
from bs4 import BeautifulSoup
import requests

# apiKey = ""
 

def test_scrape():
    scrapeowl_url = "https://api.scrapeowl.com/v1/scrape"

    #Object of the request
    object_of_data = {
        "api_key": "",
        "url": "https://www.yelp.com/biz_photos/tenoch-mexican-medford"
    }

    #Making http post request
    response = requests.post(scrapeowl_url, json=object_of_data).json()
    response = response["html"]
    soup = BeautifulSoup(response.text, 'html.parser')
    #Print the JSON response from API
  
def search(keyword, latitude, longitude):
    url = f'https://www.yelp.com/search?find_desc={keyword}&find_loc={latitude}%2C+{longitude}'
    links = getRestaurants(url)
    restaurants = []
    for link in links:
        restaurant = getdata(link, keyword)
        if restaurant == None:
            continue
        else:
            restaurant.runScan(keyword)
            print(restaurant.photos_link)
            restaurants.append(restaurant)
    restaurants.sort(key=lambda restaurant: len(restaurant.photos), reverse=True)
    return restaurants

def getRestaurants(url):
    headers = { 
        "apikey": ""
    }
    params = {
        "url": url
    }
    response = requests.get('https://app.zenscrape.com/api/v1/get', headers=headers, params=params)
    links = []
    soup = BeautifulSoup(response.text, 'html.parser')
    for a in soup.find_all('a', {'class': 'css-19v1rkv'}): 
    	if a['href'][0:5] == "/biz/":
            link = "https://www.yelp.com" + a['href']
            links.append(link)
    return links
def getdata(link, keyword):
    headers = { 
        "apikey": ""
    }
    params = {
        "url": link
    }
    response = requests.get('https://app.zenscrape.com/api/v1/get', headers=headers, params=params)
    soup = BeautifulSoup(response.text, 'html.parser')
    name = soup.find('h1', {'class': 'css-1se8maq'})
    if name == None:
        print("Couldn't find name at:", link)
        return None
    name = name.text
    rating = soup.find('span', {'class': 'css-1fdy0l5'}).text + " Stars"
    address = soup.find('p', {'class': 'css-qyp8bo'}).text
    website = soup.find('a', {'class': 'css-1idmmu3', 'target': '_blank'})
    if website == None:
        website = "None"
    else:
        website = website.text
    phone = soup.find_all('div', {'class': 'css-xp8w2v'})
    phone = phone[0].find_all('p', {'class': 'css-1p9ibgf'})
    if len(phone) < 3:
        phone = "None"
    else:
        phone = phone[1].text
    hours = []
    for day in soup.find_all('td', {'class': 'css-1hgawz4'}):
        day = day.find('p', {'class': 'css-1p9ibgf'})
        if day != None:
            hours.append(day.text)
        else:
            continue
    photosLink = "https://www.yelp.com/biz_photos/" + re.search(r'/biz/([^/?]+)', link).group(1) + "?caption=" + keyword
    restaurant = Restaurant(name, rating, address, ("https://www." + website), phone, hours, photosLink)
    return restaurant

# # def search(keyword, latitude, longitude):
# #     url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
# #     params = {
# #         'location': f'{latitude},{longitude}',
# #         'rankby': 'distance',
# #         'keyword': keyword,
# #         'key': apiKey
# #     }
# #     headers = {}
# #     print("retrieving")
# #     response = requests.get(url, params=params, headers=headers)
# #     # Print the response
# #     results = response.json()
# #     results = results["results"]
# #     for result in results:
# #         loc1 = (latitude, longitude)
# #         loc2 = (result["geometry"]["location"]["lat"], result["geometry"]["location"]["lng"])
# #         distance = round(hs.haversine(loc1, loc2), 1)
# #         name = result["name"]
# #         addy = result["vicinity"]
# #         print(distance, name, addy)
