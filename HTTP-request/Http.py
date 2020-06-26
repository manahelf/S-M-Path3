import requests
c= requests.get("https://realpython.com")
print(c.text)
print(c.url)
f= open('url Data.txt','W')
f.write(c.text)
