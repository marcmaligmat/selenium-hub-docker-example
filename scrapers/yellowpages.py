import requests
from loguru import logger

proxies = {
    "http": "http://gpfc8:usas32wk@102.165.1.59:5432",
    "https": "http://gpfc8:usas32wk@102.165.1.59:5432",
}
# response = requests.get("http://api.privateproxy.me:10738", proxies=proxies)
# print(response.text)
# response.text = "102.165.1.59\\n"
url = "https://www.yellowpages.com/search?search_terms=landscaping&geo_location_terms=Fayetteville%2C+NC"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0"
}

r = requests.get(url, headers=headers, proxies=proxies)
logger.debug("Status code ", r.status_code)
