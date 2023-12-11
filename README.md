# Python AI Food Analysis Project
- Visual Hippo is a python project where users can upload a picture of food and see restaurants near 
them that have that food, based off how similar the restaurants pictures are.


## You need:
- Flask, Tensorflow, BS4, VGG6 Pretrained Model
- ScrapingBee Account for Key authentication
- Replicate AI accoubt for key authentication
  
## Note:
- The project uses flask to connect back end to the front, and does not rlly implement a database in the MVC.
-  Thus, the runtime of the tool is pretty slow. When a user uploads an image, a bunch of scraping scripts are called
to scrape yelp for restaurants data and their images.
- Beautiful soup is used to parse the scraped html. However, due to IP blocking restrictions, the projects calls
  upon a scraper api to handle rotating proxies. That's the main bottleneck issue for the project. 
### live link:
- (https://www.visualeat.com/)

### Link to Replicate pretrained models for use in project/other projects:
- https://replicate.com/explore
