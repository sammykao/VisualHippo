<b> Visual Hippo is a python project where users can upload a picture of food and see restaurants near 
them that have that food, based off how similar the restaurants pictures are. </b>

The project uses flask to connect back end to the front, and does not rlly implement a database in the MVC. 
Thus, the runtime of the tool is pretty slow. WHen a user uploads an image, a bunch of scraping scripts are called
to scrape yelp for restaurants data and their images. Beautiful soup is used to parse the scraped html. However, due to 
IP blocking restrictions, the projects calls upon a scraper api to handle rotating proxies. That's the main bottleneck issue
for the project. 
