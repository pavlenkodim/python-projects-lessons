# Use urllib
import urllib.request

resource = urllib.request.urlopen('https://cdn.britannica.com/28/239528-050-D89C8118/reticulated-python-Malayopython-reticulatus.jpg')
out = open('image.png', 'wb')
out.write(resource.read())
out.close()

# Use request
import requests

response = requests.get('https://cdn.britannica.com/28/239528-050-D89C8118/reticulated-python-Malayopython-reticulatus.jpg')
out = open('image_req.png', 'wb')
out.write(response.content)
out.close()

# Use aiohttp
# import aiohttp ??

