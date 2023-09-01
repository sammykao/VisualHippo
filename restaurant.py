from bs4 import BeautifulSoup
import requests
from urllib.parse import quote
import re
# from image_score import vgg16, get_similarity_score
# from PIL import Image

class Restaurant:
    def __init__(self, name, rating, address, website, phone, hours, photo_link):
        self.name = name
        self.rating = rating
        self.address = address
        self.website = website
        self.phone = phone
        self.hours = hours
        self.photos_link = photo_link
        self.photos = []
        self.scores = []
    def show(self):
        print(f'Rating: {self.rating}\nCategory: {self.category}\nAddress: {self.address}')
        print(f'Website: {self.website}\nPhone: {self.phone}\nHours: {self.hours}\nPhotos: {self.photos}')
    def runScan(self, keyword):
        headers = { 
            "apikey": "ab42b860-4887-11ee-a680-17f586e73a01"
        }
        params = {
            "url": self.photos_link
        }
        response = requests.get('https://app.zenscrape.com/api/v1/get', headers=headers, params=params)
        soup = BeautifulSoup(response.text, 'html.parser')
        photoGrid = soup.find('div', {'class': 'media-landing_gallery'})
        for photo in photoGrid.find_all('img', {'class': 'photo-box-img'}):
            self.photos.append(photo['src'])
    # def performScores(self, control_image : Image):
    #     for link in self.photos:
    #         score, Rest_image = get_similarity_score(link, control_image)
    #         self.scores.append((score, Rest_image))
    #     self.scores.sort(key=lambda x:x[0], reverse=True)
    #     if len(self.scores > 5):
    #         self.scores = self.scores[0:5]
    

    