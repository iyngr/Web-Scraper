from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO

search = input("Search for: ")
params = {"q":search, "iar":"images"}
headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
r=requests.get("http://www.duckduckgo.com",params=params, headers=headers)

print(r.url)

soup = BeautifulSoup(r.text, "html.parser")
print(soup.prettify())
links = soup.findAll("a", {"class":"title_img_media"})

for item in links:
    img_url = requests.get(item.attrs["href"])
    title = item.attrs["href"].split("/")[-1]
    img = Image.open(BytesIO(img_url.content))
    img.save("./scraped_images/" + title, img.format)

