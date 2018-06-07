from bs4 import BeautifulSoup
import requests

url = requests.get('https://www.youtube.com/feed/trending')
soup = BeautifulSoup(url.text, 'html.parser')
video_list=[]

x = soup.find_all("a", class_="yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link ")
# print x
for each_x in x:
	print(each_x.prettify())
