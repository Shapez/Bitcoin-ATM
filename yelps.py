from lxml import html
import requests

page = requests.get('http://www.yelp.com/search?find_loc=Downtown%2C+Los+Angeles%2C+CA#find_desc&cflt=food&attrs=ActiveDeal ')
tree = html.fromstring(page.text)

#this should create a list of places
place = tree.xpath('//meta[@name="description"]/text()')
#this should create a list of keywords
keywords = tree.xpath('//meta[@name="keywords"]/text()')

