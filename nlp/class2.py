import requests

from bs4 import BeautifulSoup

url = 'https://www.w3schools.com/'

response = requests.get(url)

if response.status_code == 200:
    print("Successsssssssss")


soup = BeautifulSoup(response.content, 'html.parser')

t = soup.title
p = soup.p

print(t)
print(p)
print(response.status_code)
