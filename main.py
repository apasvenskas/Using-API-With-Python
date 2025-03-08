import requests
from send_email import send_email

apiKey = "3763109844bb4720bcfd5dcca99b5a11"
url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=3763109844bb4720bcfd5dcca99b5a11&languege=en"

request = requests.get(url)
content = request.json()

body = ""
for article in content["articles"][0:20]:
   if article["title"] is not None:
      body = "Subject: Today's news" + "\n" + body + article["title"] + \
         "\n" + article["description"] + "\n" + article["url"] + 2*"\n" # Displaying the data and links

body = body.encode("utf-8")
print(body)
send_email(message=body)