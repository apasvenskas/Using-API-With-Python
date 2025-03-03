import requests

apiKey = "3763109844bb4720bcfd5dcca99b5a11"
url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=3763109844bb4720bcfd5dcca99b5a11"

request = requests.get(url)
content = request.text
print(content)