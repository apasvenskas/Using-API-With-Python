import requests
from send_email import send_email

apiKey = "3763109844bb4720bcfd5dcca99b5a11"
url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=3763109844bb4720bcfd5dcca99b5a11"

request = requests.get(url)
content = request.json()

body = ""
for article in content["articles"]:
   body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
print(body)
send_email(message=body)