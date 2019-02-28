from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup("span")
count = 0
for tag in tags:
    nums = tag.contents
    number = int(nums[0-1])
    count = count + number

print(count)

#http://py4e-data.dr-chuck.net/comments_194575.html
