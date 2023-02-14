import requests

# specify the search query
search_query = 'python'

# send request to Wikipedia API
response = requests.get(f'https://en.wikipedia.org/w/api.php?action=query&format=json&list=search&utf8=1&srsearch={search_query}')

# parse JSON response
data = response.json()

# extract search results
search_results = data['query']['search']

# print search results
for result in search_results:
    title = result['title']
    summary = result['snippet']
    print(f'{title}: {summary}\n')
