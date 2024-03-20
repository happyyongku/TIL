# %%
from pprint import pprint
import requests

params = {
        'ttbkey': API_KEY,
        'QueryType': 'ItemNewSpecial',
        'MaxResults': '50',
        'start': '1',
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': '20131101'
    }

response = requests.get(API_URL, params=params).json()

result = []
for item in response['item']:
    info = {
        'isbn': item['isbn'],
        'title': item['title'],
        'pubDate': item['pubDate'],
        'author': item['author'],
    }
    result.append(info)

pprint